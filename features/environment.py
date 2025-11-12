# from utils.browser import Browser
# from pages.login_page import LoginPage
# from pages.inventory_page import InventoryPage
# from pages.product_page import ProductPage
#
# def before_all(context):
#     context.browser = Browser()
#     context.page = context.browser.page
#     context.login_page = LoginPage(context.page)
#     context.inventory_page = InventoryPage(context.page)
#     context.product_page = ProductPage(context.page)
#
# def after_all(context):
#     context.browser.close()


from behave import fixture
from playwright.sync_api import sync_playwright
import time

def before_all(context):
    try:
        context.playwright = sync_playwright().start()
        # CRITICAL: Add headless=True for CI environment
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