Feature: General login

   As a user
   When I go to the home page
   I want to be able to login

   Scenario: Logging in via the home page (form)
    Given that I am not logged in to the Student System
    And I am user with details
        | username | password | access_level |
        | johndoe  | pass     | student      |
        | teach    | pasword  | professor    |
        | grace    | userpass | admin        |
    And I go to the Student System home page
    And I enter my login details into the login form
    When I submit the login form
    Then I should be redirected to my home page with the relevant information


   Scenario: Failed log in with wrong credentials
    Given that I am not logged in to the Student System
    And I am user with details
        | username | password | access_level |
        | johndoe  | pass     | student      |
    And I go to the Student System home page
    And I try to login with username "johndoe" and password "wrong_pass"
    When I submit the login form
    Then I should be back on the home page with an error message that reads "Invalid credentials"
