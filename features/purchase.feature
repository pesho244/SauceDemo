Feature: Complete purchase flow

  Scenario: Add product to cart and finish checkout
    Given I am logged in as "standard_user" with password "secret_sauce"
    When I open the first product
    And I add the product to the cart
    And I navigate to the cart
    Then I should see the same product in the cart
    When I proceed to checkout
    And I fill in checkout information
    And I continue to overview
    Then I should see the same product in the overview
    When I finish the order
    Then I should see "Thank you for your order!" message
