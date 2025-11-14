# be/services/sauce_service.py

import os
import logging
from datetime import datetime

from playwright.async_api import async_playwright

SAUCE_URL = "https://www.saucedemo.com"

# Base paths (work when running from project root)
BE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BE_ROOT, "logs")
SCREENSHOT_DIR = os.path.join(BE_ROOT, "screenshots")
STATE_PATH = os.path.join(BE_ROOT, "state.json")

# Ensure folders exist
os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "api.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


async def _take_screenshot(page, label: str) -> str:
    """
    Helper: take screenshot on error and return the file path.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{label}_{timestamp}.png".replace(" ", "_")
    path = os.path.join(SCREENSHOT_DIR, filename)
    try:
        await page.screenshot(path=path, full_page=True)
        logger.info(f"Saved screenshot: {path}")
    except Exception as e:
        logger.error(f"Failed to save screenshot: {e}")
    return path


async def _load_context(p):
    """
    Helper: load browser context using saved login state.
    Raises if /login was not called before.
    """
    if not os.path.exists(STATE_PATH):
        raise RuntimeError("No saved session. Call /login first.")

    browser = await p.chromium.launch(headless=True)
    context = await browser.new_context(storage_state=STATE_PATH)
    page = await context.new_page()
    return browser, context, page


# ---------------------------------------------------------
# LOGIN: saves session cookies to state.json
# ---------------------------------------------------------
async def login_user(username: str, password: str):
    logger.info(f"Login started for user '{username}'")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto(SAUCE_URL, wait_until="networkidle")
            await page.fill("#user-name", username)
            await page.fill("#password", password)
            await page.click("#login-button")
            await page.wait_for_url("**/inventory.html", timeout=15000)

            # Save storage state for reuse
            await context.storage_state(path=STATE_PATH)
            logger.info("Login successful, session state saved.")
            return {"success": True, "message": "Login successful"}

        except Exception as e:
            logger.error(f"Login failed: {e}")
            screenshot = await _take_screenshot(page, "login_error")
            return {"success": False, "error": str(e), "screenshot": screenshot}

        finally:
            await browser.close()


# ---------------------------------------------------------
# GET PRODUCT DETAILS (uses saved session)
# ---------------------------------------------------------
async def get_product_details(name: str):
    logger.info(f"Get product details for '{name}'")

    async with async_playwright() as p:
        try:
            browser, context, page = await _load_context(p)
        except Exception as e:
            logger.error(f"Failed to load context in get_product_details: {e}")
            return {"success": False, "error": str(e)}

        try:
            await page.goto(f"{SAUCE_URL}/inventory.html", wait_until="networkidle")

            items = page.locator(".inventory_item").filter(has_text=name)
            if await items.count() == 0:
                logger.warning(f"Product '{name}' not found.")
                return {"success": False, "error": f"Product '{name}' not found"}

            title = await items.first.locator(".inventory_item_name").inner_text()
            desc = await items.first.locator(".inventory_item_desc").inner_text()
            price = await items.first.locator(".inventory_item_price").inner_text()

            logger.info(f"Product '{name}' found with price {price}")
            return {
                "success": True,
                "name": title,
                "description": desc,
                "price": price
            }

        except Exception as e:
            logger.error(f"Error in get_product_details: {e}")
            screenshot = await _take_screenshot(page, "product_error")
            return {"success": False, "error": str(e), "screenshot": screenshot}

        finally:
            await browser.close()


# ---------------------------------------------------------
# ADD TO CART (uses saved session)
# ---------------------------------------------------------
async def add_to_cart(item_name: str):
    logger.info(f"Add to cart: '{item_name}'")

    async with async_playwright() as p:
        try:
            browser, context, page = await _load_context(p)
        except Exception as e:
            logger.error(f"Failed to load context in add_to_cart: {e}")
            return {"success": False, "error": str(e)}

        try:
            await page.goto(f"{SAUCE_URL}/inventory.html", wait_until="networkidle")

            item = page.locator(".inventory_item").filter(has_text=item_name)
            if await item.count() == 0:
                logger.warning(f"Item '{item_name}' not found on inventory page.")
                return {"success": False, "error": f"Item '{item_name}' not found"}

            await item.first.locator("button:has-text('Add to cart')").click()
            logger.info(f"Item '{item_name}' added to cart.")
            return {"success": True, "item_added": item_name}

        except Exception as e:
            logger.error(f"Error in add_to_cart: {e}")
            screenshot = await _take_screenshot(page, "add_to_cart_error")
            return {"success": False, "error": str(e), "screenshot": screenshot}

        finally:
            await browser.close()


# ---------------------------------------------------------
# CHECKOUT FULL PROCESS (uses saved session)
# ---------------------------------------------------------
async def checkout_order(first: str, last: str, zip_code: str, item_name: str):
    logger.info(f"Checkout started for '{item_name}' for {first} {last} ({zip_code})")

    async with async_playwright() as p:
        try:
            browser, context, page = await _load_context(p)
        except Exception as e:
            logger.error(f"Failed to load context in checkout_order: {e}")
            return {"success": False, "error": str(e)}

        try:
            # Inventory page
            await page.goto(f"{SAUCE_URL}/inventory.html", wait_until="networkidle")

            # Add item to cart
            item = page.locator(".inventory_item").filter(has_text=item_name)
            if await item.count() == 0:
                logger.warning(f"Item '{item_name}' not found during checkout.")
                return {"success": False, "error": f"Item '{item_name}' not found"}

            await item.first.locator("button:has-text('Add to cart')").click()
            logger.info(f"Item '{item_name}' added to cart in checkout flow.")

            # Cart page
            await page.click(".shopping_cart_link")
            await page.wait_for_url("**/cart.html")

            # Checkout page
            await page.click("#checkout")
            await page.wait_for_url("**/checkout-step-one.html")

            # Fill data
            await page.fill("#first-name", first)
            await page.fill("#last-name", last)
            await page.fill("#postal-code", zip_code)
            await page.click("#continue")
            await page.wait_for_url("**/checkout-step-two.html")

            # Finish
            await page.click("#finish")
            await page.wait_for_url("**/checkout-complete.html")

            logger.info("Checkout completed successfully.")
            return {"success": True, "message": "Order completed successfully!"}

        except Exception as e:
            logger.error(f"Error in checkout_order: {e}")
            screenshot = await _take_screenshot(page, "checkout_error")
            return {"success": False, "error": str(e), "screenshot": screenshot}

        finally:
            await browser.close()