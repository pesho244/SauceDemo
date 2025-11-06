class ProductPage:
    def __init__(self, page):
        self.page = page
        self.product_title = page.locator(".inventory_details_name")
        self.product_desc = page.locator(".inventory_details_desc")
        self.back_button = page.locator("#back-to-products")

    def get_title(self):
        return self.product_title.inner_text()

    def get_description(self):
        return self.product_desc.inner_text()

    def go_back(self):
        self.back_button.click()
