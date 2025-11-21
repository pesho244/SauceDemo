Feature: Login functionality

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user is logged in with username "env" and password "env"
    Then the user should be redirected to the inventory page

  Scenario: Login with invalid password
    Given the user is on the login page
    When the user is logged in with username "standard_user" and password "wrong_pass"
    Then the user should see an error message "Epic sadface: Username and password do not match any user in this service"

  Scenario: Login with locked out user
    Given the user is on the login page
    When the user is logged in with username "locked_out_user" and password "env"
    Then the user should see an error message "Epic sadface: Sorry, this user has been locked out."
