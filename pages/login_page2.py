class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("user-name")
        self.password_field = page.locator("password-name")
        self.login_button = page.locator("login-button")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com")

    def login_actions(self):
        self.username_field.fill("standard_user")
        self.password_field.fill("secret_sauce")
        self.login_button.click()

