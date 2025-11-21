from behave import fixture
from playwright.sync_api import sync_playwright
import time
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

    # Determine CI mode
    is_ci = os.getenv("CI") == "true"

    # Launch browser
    browser_cfg = context.config["browser"]
    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(
        headless=True if is_ci else browser_cfg["headless"],
        slow_mo=browser_cfg["slowmo"]
    )

    context.page = context.browser.new_page()

def after_all(context):
    # Prevent cleanup errors from failing CI
    try:
        if getattr(context, "browser", None):
            try:
                context.browser.close()
            except Exception:
                pass

        if getattr(context, "playwright", None):
            try:
                context.playwright.stop()
            except Exception:
                pass

    except Exception:
        pass  # swallow everything

def after_step(context, step):
    if step.status == "failed":
        os.makedirs("fe/screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Clean filename for Windows
        filename = step.name
        for bad in ['"', "'", ":", "/", "\\", "*", "?", "<", ">", "|"]:
            filename = filename.replace(bad, "")
        filename = filename.replace(" ", "_")

        path = f"fe/screenshots/{filename}_{timestamp}.png"

        context.page.screenshot(path=path)
        print(f"\n📸 Screenshot saved to: {path}\n")