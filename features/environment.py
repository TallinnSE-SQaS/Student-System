from selenium.webdriver.chrome.webdriver import WebDriver

from application.users.models import User, Role
from application.courses.models import Course, CourseDependency, CourseEnrollment


def before_feature(context, feature):
    User.bulk_create([
        User(pk=1, username='student1', password='some-password', role=Role.Student),
        User(pk=2, username='student2', password='some-password', role=Role.Student),
        User(pk=3, username='student3', password='some-password', role=Role.Student),
        User(pk=4, username='professor', password='some-password', role=Role.Professor),
        User(pk=5, username='staff', password='some-password', role=Role.Staff),
    ])

    Course.bulk_create([
        Course(pk=1, name='Basic Programming', professor_id=4, capacity=2),
        Course(pk=2, name='Advanced Programming', professor_id=4, capacity=2),
        Course(pk=3, name='Documentation', professor_id=4, capacity=2),
    ])

    CourseDependency.create(pk=1, dependant=2, dependee=1)

    CourseEnrollment.bulk_create([
        CourseEnrollment(student_id=1, course=1),
        CourseEnrollment(student_id=3, course=1),
        CourseEnrollment(student_id=1, course=2),
        CourseEnrollment(student_id=2, course=3),
    ])

    context.base_url = 'http://localhost:5000'
    context.browser = WebDriver()


def after_feature(context, feature):
    for model in [User, CourseEnrollment, CourseDependency, Course]:
        model.drop_table()
        model.create_table()

    context.browser.close()


def before_scenario(context, scenario):
    if scenario.name == 'Student tries to enroll in a course that requires another course':
        CourseEnrollment.delete().where(CourseEnrollment.student == 3).execute()

    context.browser.get(context.base_url)


def after_scenario(context, scenario):
    context.browser.delete_all_cookies()
