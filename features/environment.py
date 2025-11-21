from behave import fixture
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
import yaml

def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)

def before_all(context):
    context.config = load_config()

    # Load credentials from environment variables
    context.username = os.getenv(context.config["credentials"]["username_env"])
    context.password = os.getenv(context.config["credentials"]["password_env"])

    if not context.username or not context.password:
        raise Exception("❌ Missing required environment variables SAUCE_USERNAME / SAUCE_PASSWORD")

    # Detect CI to force headless there
    is_ci = os.getenv("CI") == "true"

    browser_cfg = context.config["browser"]
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=True if is_ci else browser_cfg["headless"],
        slow_mo=browser_cfg["slowmo"]
    )
    context.page = context.browser.new_page()


def after_all(context):
    # Make sure cleanup never fails the run (especially in CI)
    try:
        # Try closing page if it exists
        page = getattr(context, "page", None)
        if page is not None:
            try:
                page.close()
            except Exception:
                pass

        # Try closing browser if it exists
        browser = getattr(context, "browser", None)
        if browser is not None:
            try:
                browser.close()
            except Exception:
                pass

        # Try stopping Playwright if it exists
        pw = getattr(context, "playwright", None)
        if pw is not None:
            try:
                pw.stop()
            except Exception:
                pass

    except Exception:
        # Swallow absolutely everything in teardown
        # so behave doesn't mark scenario as cleanup_error
        pass


def after_step(context, step):
    if step.status == "failed":
        try:
            page = getattr(context, "page", None)
            if page is None:
                return

            os.makedirs("fe/screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Clean filename for Windows
            filename = step.name
            for bad in ['"', "'", ":", "/", "\\", "*", "?", "<", ">", "|"]:
                filename = filename.replace(bad, "")
            filename = filename.replace(" ", "_")

            path = f"fe/screenshots/{filename}_{timestamp}.png"

            page.screenshot(path=path)
            print(f"\n📸 Screenshot saved to: {path}\n")

        except Exception as e:
            # Do NOT fail test if screenshot fails
            print(f"⚠️ Failed to capture screenshot: {e}")
