class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self.first_name = page.locator("[data-test='firstName']")
        self.last_name = page.locator("[data-test='lastName']")
        self.postal_code = page.locator("[data-test='postalCode']")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_message = page.locator(".complete-header")

    def fill_information(self, first="John", last="Doe", postal="12345"):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()

    def get_complete_message(self):
        return self.complete_message.inner_text()
