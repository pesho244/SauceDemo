Feature: Product Page

  Background:
    Given the user logged in as "standard_user" with password "secret_sauce"
    And the user opens the first product

  Scenario: Verify product details
    Then the product should have a title
    And the product should have a description
