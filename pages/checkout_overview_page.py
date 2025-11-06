from playwright.sync_api import Page

class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.item_name = page.locator(".inventory_item_name")
        self.finish_button = page.locator("#finish")

    def get_item_name(self):
        return self.item_name.text_content()

    def finish_order(self):
        self.finish_button.click()
