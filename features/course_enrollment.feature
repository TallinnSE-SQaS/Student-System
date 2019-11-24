Feature: Course enrollment
    As a student "testuser"

    Scenario: Student successfully enrolls to course
        Given I am logged in as username "student3" and password "some-password"
        And I have completed dependee course "Basic Programming"
        And "Advanced Programming" has not reached max capacity
        When I attempt to enroll in "Advanced Programming"
        Then "Advanced Programming" student count should increase by 1
        And "Advanced Programming" should show up on my time table

    Scenario: Student tries to enroll to a filled out course
        Given I am logged in as username "student3" and password "some-password"
        And I have completed dependee course "Basic Programming"
        And "Advanced Programming" has reached max capacity
        When I attempt to enroll in "Advanced Programming"
        Then I should see an error message that reads "This course has reached max capacity"
        And "Advanced Programming" student count should stay the same

    Scenario: Student tries to enroll in a course that requires another course
        Given I am logged in as username "student3" and password "some-password"
        And I have not completed dependee course "Basic Programming"
        And "Advanced Programming" has not reached max capacity
        When I attempt to enroll in "Advanced Programming"
        Then I should see an error message that reads "You must complete the course 'Basic Programming' first"
        And "Advanced Programming" student count should stay the same
