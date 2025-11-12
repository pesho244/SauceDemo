# be/services/sauce_service.py
from playwright.async_api import async_playwright
import asyncio

async def login_user(username: str, password: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com")

        await page.fill("#user-name", username)
        await page.fill("#password", password)
        await page.click("#login-button")
        await page.wait_for_url("**/inventory.html")

        await browser.close()
        return {"success": True, "message": "Login successful"}


async def get_product_details(name: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/inventory.html")

        item_locator = f"text={name}"
        await page.wait_for_selector(item_locator)
        element = await page.query_selector(item_locator)
        text = await element.inner_text()

        await browser.close()
        return {"name": name, "description": text}


async def add_to_cart(item_name: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.saucedemo.com/inventory.html")

        button_selector = f"text=Add to cart >> xpath=..//div[text()='{item_name}']"
        await page.wait_for_selector(button_selector)
        await page.click(button_selector)

        await browser.close()
        return {"success": True, "cart_count": 1, "item_added": item_name}
