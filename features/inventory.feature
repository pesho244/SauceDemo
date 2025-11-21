Feature: Inventory Page

  Background:
    Given the user is logged in as "env" with password "env"

  Scenario: Verify inventory page loads
    Then the user should see the title "Products"
    And the user should see more than 0 products

  Scenario: Open first product
    When the user opens the first product
    Then the user should see the product detail page
