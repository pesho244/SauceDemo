import time
from playwright.sync_api import expect

class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator(".title")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_icon = page.locator(".shopping_cart_link")

    def wait_until_loaded(self):
        # Wait for the page title and inventory list to appear
        expect(self.title).to_be_visible(timeout=15000)
        expect(self.inventory_items.first).to_be_visible(timeout=15000)
        time.sleep(1)  # optional visual delay

    def open_first_item(self):
        # Wait for inventory to load, then click on first product’s title link
        self.wait_until_loaded()
        self.inventory_items.first.locator("[data-test*='title-link']").click()

    def add_first_item_to_cart(self):
        # Once on the product detail page, click the Add to Cart button
        self.page.wait_for_selector("button[data-test^='add-to-cart']")
        self.page.locator("button[data-test^='add-to-cart']").click()

    def go_to_cart(self):
        self.cart_icon.click()
