Feature: Product Page

  Background:
    Given I am logged in as "standard_user" with password "secret_sauce"
    And I open the first product

  Scenario: Verify product details
    Then the product should have a title
    And the product should have a description
