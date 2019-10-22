Feature: Enrolling into Courses

    As a student
    When I visit a course page
    I want to be able to enroll into the course by clicking a button
    Or read a "can't enroll" message based on different conditions

    Scenario: Successfully enrolling in a course
        Given I am logged in as a student
        And I visit the page of a course called "Basic Course"
        And the course does not depend on other courses
        And the capacity of the course is 60
        And the number of enrolled students is 40
        When I click on "Enroll"
        Then I should be enrolled in the course
        And the number of enrolled students should be 41

    Scenario: Failing to enroll in a filled out course
        Given I am logged in as a student
        And I visit the page of a course called "Basic Course"
        And the course does not depend on other courses
        And the capacity of the course is 60
        And the number of enrolled students is 60
        Then I should see a message that reads, "Course capacity reached."
        And the "Enroll" button should be disabled

    Scenario: Failing to enroll in a course due to dependee courses
        Given I am logged in as a student
        And I visit the page of a course called "Advanced Course"
        And the course depends on "Basic Course"
        Then I should see a message that reads, "You need to complete Basic Course before enrolling into Advanced Course"
        And the "Enroll" button should be disabled
