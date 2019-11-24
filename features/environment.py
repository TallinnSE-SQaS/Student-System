from selenium.webdriver.chrome.webdriver import WebDriver

from application.users.models import User, Role
from application.courses.models import Course, CourseDependency, CourseEnrollment


def before_scenario(context, scenario):
    User.bulk_create([
        User(pk=1, username='student1', password='some-password', role=Role.Student),
        User(pk=2, username='student2', password='some-password', role=Role.Student),
        User(pk=3, username='student3', password='some-password', role=Role.Student),
        User(pk=4, username='professor', password='some-password', role=Role.Professor),
        User(pk=5, username='staff', password='some-password', role=Role.Staff),
    ])

    Course.bulk_create([
        Course(pk=1, name='Basic Programming', professor_id=4, capacity=2, student_count=2),
        Course(pk=2, name='Advanced Programming', professor_id=4, capacity=2, student_count=1),
        Course(pk=3, name='Documentation', professor_id=4, capacity=2, student_count=1),
    ])

    CourseDependency.create(pk=1, dependant=2, dependee=1)

    CourseEnrollment.bulk_create([
        CourseEnrollment(student_id=1, course=1),
        CourseEnrollment(student_id=3, course=1),
        CourseEnrollment(student_id=1, course=2),
        CourseEnrollment(student_id=2, course=3),
    ])

    context.browser = WebDriver()
    context.browser.get('http://localhost:5000')


def after_scenario(context, scenario):
    for model in [User, CourseEnrollment, CourseDependency, Course]:
        model.drop_table()
        model.create_table()

    context.browser.close()
