Feature: Logging into the website

    As a user
    I want to login to the system

    Scenario: Student successfully logs in
        Given that I am a student
        And I am on the home page
        And my credentials are username "student1" and password "some-password"
        When I enter my credentials into the login form
        And I submit the form
        Then I should be redirected to the student homepage

    Scenario: Student fails to log in
        Given that I am a student
        And I am on the home page
        And my invalid credentials are username "student1" and password "bad-password"
        When I enter my credentials into the login form
        And I submit the form
        Then I should remain on the logged-out homepage
        And I should see an error message that reads "Invalid credentials"
