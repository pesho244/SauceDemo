Feature: Checkout process

  Background:
    Given the user is logged in as "env" with password "env"
    And the user opens the first product

  Scenario: Complete a purchase
    When the user adds the product to the cart
    And the user navigates to the cart
    And the user proceeds to checkout
    And the user fills in checkout information
    And the user finishes the order
    Then the user should see the message "Thank you for your order!"
