Feature: Course Management
    As a professor "testprof"

    Scenario: Professor creates a starting point course
        Given that I am logged in as professor "testprof"
        And "Basic Programming" does not exist
        When I attempt to create a course "Basic Programming"
        Then course "Basic Programming" exixts
        And course "Basic Programming" has no dependents

    Scenario: Professor posts a new assessment into a course
        Given that I am logged in as professor "testprof"
        And course "Basic Programming" exists
        When I attempt to add a new assessment "Assessment 1" to course "Basic Programming"
        Then "Assessment 1" exists and is open
        And "Assessment 1" is associated with "Basic Programming"

    Scenario: Professor grades an assessment
        Given that I am logged in as professor "testprof"
        And course "Basic Programming" exists
        And "Assessment 1" exixts and is open
        And "Assessment 1" is associated with "Basic Programming"
        And "Assessment 1" has at least "1" submission
        When I attemp to grade "Assessment 1"
        Then "Assessment 1" is graded and closed
        And studnets who submitted "Assessment 1" are sent a notification
