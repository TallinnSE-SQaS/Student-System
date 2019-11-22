Feature: Course enrollment
    As a student "testuser"

    Scenario: Student successfully enrolls to course
        Given that I am logged in as a Student "testuser"
        And I have completed dependent course "Course 1.1"
        And "Course 2.2" has not reached max capacity
        When I attempt to enroll in "Course 2.2"
        Then "Course 2.2" student count should increase by "1"
        And "Course 2.2" show up on my time table
    
    Scenario: Student tries to enroll to a filled out course
        Given that I am logged in as a Student "testuser"
        And I have completed dependent course "Course 1.1"
        And "Course 2.2" has reached max capacity
        When I attempt to enroll in "Course 2.2"
        Then "Course 2.2" student count should stay the same
        And I should recieve an error message

    Scenario: Student tries to enroll in a course that requires another course
        Given that I am logged in as a Student "testuser"
        And I have not completed dependent course "Course 1.1"
        And "Course 2.2" has not reached max capacity
        When I attempt to enroll in "Course 2.2"
        Then "Course 2.2" student count should stay the same
        And I should recieve an error message

Feature: Course Management
    As a professor "testprof"
    
    Scenario: Professor creates a starting point course
        Given that I am logged in as professor "testprof"
        And "Course 0.1" does not exist
        When I attempt to create a course "Course 0.1"
        Then course "Course 0.1" exixts
        And course "Course 0.1" has no dependents

    Scenario: Professor posts a new assessment into a course
        Given that I am logged in as professor "testprof"
        And course "Course 0.1" exists
        When I attempt to add a new assessment "Ass 1" to course "Course 0.1"
        Then "Ass 1" exists and is open
        And "Ass 1" is associated with "Course 0.1"
    
    Scenario: Professor grades an assessment
        Given that I am logged in as professor "testprof"
        And course "Course 0.1" exists
        And "Ass 1" exixts and is open
        And "Ass 1" is associated with "Course 0.1"
        And "Ass 1" has at least "1" submission
        When I attemp to grade "Ass 1"
        Then "Ass 1" is graded and closed
        And studnets who submitted "Ass 1" are sent a notification

    