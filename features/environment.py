from behave import fixture
from playwright.sync_api import sync_playwright
import time
import os
from datetime import datetime


def before_all(context):
    try:
        context.playwright = sync_playwright().start()
        context.browser = context.playwright.chromium.launch(headless=True)
        context.page = context.browser.new_page()
        print("Browser launched successfully in headless mode")
    except Exception as e:
        print(f"Error in before_all: {e}")
        raise


def after_all(context):
    try:
        if hasattr(context, 'browser') and context.browser:
            context.browser.close()
            print("Browser closed successfully")
        if hasattr(context, 'playwright') and context.playwright:
            context.playwright.stop()
            print("Playwright stopped successfully")
    except Exception as e:
        print(f"Error in after_all: {e}")


# TAKE SCREENSHOT ON EVERY FAILED STEP
def after_step(context, step):
    if step.status == "failed":
        os.makedirs("fe/screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # CLEAN FILE NAME (remove illegal Windows chars)
        filename = step.name.replace(" ", "_")
        for bad in ['"', "'", ":", "/", "\\", "*", "?", "<", ">", "|"]:
            filename = filename.replace(bad, "")

        path = f"fe/screenshots/{filename}_{timestamp}.png"

        if hasattr(context, "page"):
            context.page.screenshot(path=path)
            print(f"\n📸 Screenshot saved to: {path}\n")