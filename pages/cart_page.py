# pages/cart_page.py

class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator("[data-test='checkout']")

    def get_first_cart_item_title(self):
        """Return the title of the first product in the cart"""
        return self.cart_items.first.locator(".inventory_item_name").inner_text()

    def proceed_to_checkout(self):
        """Click the checkout button to continue"""
        self.checkout_button.click()
