from behave import then

@then('the user should see the title "{title}"')
def step_verify_title(context, title):
    assert context.inventory_page.title.inner_text() == title

@then("the user should see more than 0 products")
def step_count_products(context):
    assert context.inventory_page.get_item_count() > 0

@then("the user should see the product detail page")
def step_verify_product_detail(context):
    assert context.product_page.get_title() != "", "Product title missing!"
