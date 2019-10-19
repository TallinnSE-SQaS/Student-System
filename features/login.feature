Feature: General login

   As a user
   When I go to the home page
   I want to be able to login

   Scenario: Logging in via the home page (form)
    Given that I am not logged in to the SS
    And I am user with details
        | username | password | access_level |
        | johndoe  | pass     | student      |
        | teach    | pasword  | professor    |
        | grace    | userpass | admin        |
    And I go to the SS home page
    And I enter my login details into the login form
    When I submit the login form
    Then I should be redirected to my home page with the relevant information
