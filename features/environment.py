from utils.browser import Browser
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage

def before_all(context):
    context.browser = Browser()
    context.page = context.browser.page
    context.login_page = LoginPage(context.page)
    context.inventory_page = InventoryPage(context.page)
    context.product_page = ProductPage(context.page)

def after_all(context):
    context.browser.close()
