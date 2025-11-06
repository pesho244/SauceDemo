Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I login with username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page

  Scenario: Login with invalid password
    Given I am on the login page
    When I login with username "standard_user" and password "wrong_pass"
    Then I should see an error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Login with locked out user
    Given I am on the login page
    When I login with username "locked_out_user" and password "secret_sauce"
    Then I should see an error message "Epic sadface: Sorry, this user has been locked out."
