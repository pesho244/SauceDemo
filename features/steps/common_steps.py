import time
from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given('the user is on the login page')
def step_open_login(context):
    context.page.goto(context.config["urls"]["base"])

@given('the user is logged in as "{username}" with password "{password}"')
def step_login(context, username, password):

    # IF credentials in feature file = keyword "env" → use environment variables instead
    if username == "env":
        username = context.username
    if password == "env":
        password = context.password

    context.page.goto(context.config["urls"]["base"])
    context.login_page = LoginPage(context.page)
    context.login_page.login(username, password)

    context.inventory_page = InventoryPage(context.page)
    context.product_page = ProductPage(context.page)
    context.cart_page = CartPage(context.page)
    context.checkout_page = CheckoutPage(context.page)

    time.sleep(0.5)

from behave import given, when

@given("the user opens the first product")
@when("the user opens the first product")
def step_open_first(context):
    context.inventory_page.open_first_item()


@when("the user adds the product to the cart")
def step_add_product(context):
    context.inventory_page.add_first_item_to_cart()

@when("the user navigates to the cart")
def step_go_to_cart(context):
    context.page.locator(".shopping_cart_link").click()
    time.sleep(0.5)

@when("the user proceeds to checkout")
def step_proceed_to_checkout(context):
    context.cart_page.proceed_to_checkout()
    time.sleep(0.3)

@when("the user fills in checkout information")
def step_fill_in_info(context):
    context.checkout_page.fill_information()
    time.sleep(0.3)

@when("the user finishes the order")
def step_finish(context):
    context.checkout_page.finish_order()
    time.sleep(0.4)

@then('the user should see the message "{expected}"')
def step_check_message(context, expected):
    actual = context.checkout_page.get_complete_message()
    assert expected in actual, f"Expected '{expected}', got '{actual}'"
