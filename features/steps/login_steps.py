from behave import when, then

@when('the user is logged in with username "{username}" and password "{password}"')
def step_login(context, username, password):

    if username == "env":
        username = context.username
    if password == "env":
        password = context.password

    context.login_page.login(username, password)

@then("the user should be redirected to the inventory page")
def step_verify_inventory(context):
    assert context.inventory_page.is_loaded(), "Inventory page did not load!"

@then('the user should see an error message "{error_text}"')
def step_verify_error(context, error_text):
    message = context.login_page.error_message.inner_text()
    assert error_text in message, f"Expected '{error_text}', got '{message}'"


# ---- WHEN STEPS ----

@when('the user enters username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)


@when("the user clicks the login button")
def step_click_login(context):
    context.login_page.click_login()

@then('the username field should not accept more than 15 characters')
def step_verify_username_length(context):
    entered_value = context.login_page.get_username_value()
    assert len(entered_value) <= 15, \
        f"Username length exceeded 15 characters: {len(entered_value)}"


@then('the password field should not accept more than 10 characters')
def step_verify_password_length(context):
    entered_value = context.login_page.get_password_value()
    assert len(entered_value) <= 10, \
        f"Password length exceeded 10 characters: {len(entered_value)}"


@then('the user should see a validation message "{error_text}"')
def step_verify_validation_message(context, error_text):
    message = context.login_page.get_validation_message()
    assert error_text in message, \
        f"Expected validation message '{error_text}', got '{message}'"


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.message = page.locator(".message")  # adjust selector!

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_message(self):
        return self.message.text_content()


def login_to_profile(context, username, password, expected_message):
    context.login_page.login(username, password)

    actual_message = context.login_page.get_message()
    assert expected_message in actual_message, \
        f"Expected '{expected_message}', got '{actual_message}'"


# for i in range(1, 22):
#     print(2)
#
# numebrs = [2 , 3, 4]
# total = 0
# for num in numbers:
#     total + = num
# print(total)
#
# numebrs = [2 , 3, 4]
# max_number = numberes[0]
# for num in numbers:
#     if num > max_number:
#         max_number = num
# print(max_number)

























