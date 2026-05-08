from behave import then

@then("the product should have a title")
def step_title(context):
    assert context.product_page.get_title() != ""

@then("the product should have a description")
def step_desc(context):
    assert context.product_page.get_description() != ""
