Feature: Inventory Page

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"

  Scenario: Verify inventory page loads correctly
    Then I should see the title "Products"
    And there should be more than 0 products displayed

  Scenario: Open first product
    When I open the first product
    Then I should see the product detail page
