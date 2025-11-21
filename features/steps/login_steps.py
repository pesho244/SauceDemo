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
