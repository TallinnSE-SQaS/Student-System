Feature: Logging into the website

    As a user
    I want to login to the system

    Scenario: Student successfully logs in
        Given that I am a student
        And I am on the home page
        And I have valid credientials:
            | username | password |
            | testuser | testpass |
        When I enter my credientials into the login form
        And submit the form
        Then I should be redirected to the student homepage

    Scenario: Student fails to log in
        Given that I am a student
        And I am on the home page
        And I have invalid credientials:
            | username | password |
            | testuser | badpass |
        When I enter my credientials into the login form
        And submit the form
        Then I should be remain on the homepage
        And I should see an error message
