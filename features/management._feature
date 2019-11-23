Feature: User management
    As a general staff "userstaff"

    Scenario: Operator successfully registers a new student, professor, or other member of the general staff
        Given that I am logged in as general staff "userstaff"
        And user "user1" does not exist
        When I attempt to add new user "user1" with role "student"
        Then user "user1" exixts with role "student"

    Scenario: Operator successfully send invoice to a student
        Given that I am logged in as general staff "userstaff"
        And user "user1" exixts with role "student"
        When I attempt to send an invoice to user "user1"
        Then user "user1" recieves an invoice
