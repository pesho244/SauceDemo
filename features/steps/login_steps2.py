from behave import when, then
@when('the user is logged in with username "{username}" and password "{password}" (standard_user and secret_sauce)')
def step_login(context, username, password):
    if username == "standard_user" and password == "secret_sauce":
        context.login_page.login(username, password)
    else:
        # handle other cases
        pass

@then('the user is redirected to the inventory page')
def step_verify_inventory(context):
    assert context.inventory_page.is_loaded(), "Inventory page did not load!"
