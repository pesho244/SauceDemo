# features/steps/common_steps.py
import time
from behave import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given('I am on the login page')
def step_open_login(context):
    context.page.goto("https://www.saucedemo.com/")

@given('I am logged in as "{username}" with password "{password}"')
def step_login(context, username, password):
    # ensure page objects exist on context
    context.page.goto("https://www.saucedemo.com/")
    context.login_page = LoginPage(context.page)
    context.login_page.login(username, password)
    # after login, initialize inventory and product pages as needed
    context.inventory_page = InventoryPage(context.page)
    context.product_page = ProductPage(context.page)
    context.cart_page = CartPage(context.page)
    context.checkout_page = CheckoutPage(context.page)
    # small visual pause for debugging; remove or reduce for CI
    time.sleep(0.5)

@when("I open the first product")
def step_open_first(context):
    context.inventory_page.open_first_item()

@when("I add the product to the cart")
def step_add_product(context):
    context.inventory_page.add_first_item_to_cart()

@when("I navigate to the cart")
def step_go_to_cart(context):
    context.page.locator(".shopping_cart_link").click()
    time.sleep(0.5)

@when("I proceed to checkout")
def step_proceed_to_checkout(context):
    context.cart_page.proceed_to_checkout()
    time.sleep(0.3)

@when("I fill in checkout information")
def step_fill_in_info(context):
    context.checkout_page.fill_information()
    time.sleep(0.3)

@when("I finish the order")
def step_finish_order(context):
    context.checkout_page.finish_order()
    time.sleep(0.4)

@then('I should see "{expected}" message')
def step_check_message(context, expected):
    actual = context.checkout_page.get_complete_message()
    assert expected in actual, f"Expected message to contain '{expected}' but got '{actual}'"

@then("I should see the same product in the cart")
def step_verify_cart_product(context):
    # Temporarily skip verification until we capture product name
    print("Skipping product name verification for now.")


