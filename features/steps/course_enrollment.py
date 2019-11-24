import re

from behave import given, when, then, use_step_matcher

from application.courses.models import Course, CourseEnrollment, CourseDependency


use_step_matcher('re')


@given(r'I am logged in as username "(?P<username>[^"]+)" and password "(?P<password>[^"]+)"')
def step_impl(context, username, password):
    context.browser.find_element_by_id('username').send_keys(username)
    context.browser.find_element_by_id('password').send_keys(password)
    context.browser.find_element_by_id('submit').click()


@given(r'I have completed dependee course "(?P<course>[^"]+)"')
def step_impl(context, course):
    assert course in context.browser.page_source


@given(r'"(?P<course>[^"]+)" has not reached max capacity')
def step_impl(context, course):
    c: Course = Course.select().where(Course.name == course).first()
    context.course_url = '%s/courses/%d' % (context.base_url, c.pk)
    context.browser.get(context.course_url)

    course_data = context.browser.find_element_by_class_name('lead')
    student_count = int(re.search(r'Student count: (\d+)', course_data.text)[1])
    capacity = int(re.search(r'Capacity: (\d+)', course_data.text)[1])

    assert student_count < capacity

    context.student_count = student_count
    context.capacity = capacity


@when(r'I attempt to enroll in "(?P<course>[^"]+)"')
def step_impl(context, course):
    context.browser.find_element_by_css_selector('#enroll').click()


@then(r'"(?P<course>[^"]+)" student count should increase by 1')
def step_impl(context, course):
    context.browser.get(context.course_url)

    course_data = context.browser.find_element_by_class_name('lead')
    student_count = int(re.search(r'Student count: (\d+)', course_data.text)[1])

    assert student_count == context.student_count + 1


@then(r'"(?P<course>[^"]+)" should show up on my time table')
def step_impl(context, course):
    context.browser.get(context.base_url)
    assert course in context.browser.page_source


@given(r'"(?P<course>[^"]+)" has reached max capacity')
def step_impl(context, course):
    c: Course = Course.select().where(Course.name == course).first()
    context.course_url = '%s/courses/%d' % (context.base_url, c.pk)
    context.browser.get(context.course_url)

    course_data = context.browser.find_element_by_class_name('lead')
    student_count = int(re.search(r'Student count: (\d+)', course_data.text)[1])
    capacity = int(re.search(r'Capacity: (\d+)', course_data.text)[1])

    assert student_count == capacity

    context.student_count = student_count
    context.capacity = capacity


@then(r'"(?P<course>[^"]+)" student count should stay the same')
def step_impl(context, course):
    context.browser.get(context.course_url)

    course_data = context.browser.find_element_by_class_name('lead')
    student_count = int(re.search(r'Student count: (\d+)', course_data.text)[1])

    assert student_count == context.student_count


@given(r'I have not completed dependee course "(?P<course>[^"]+)"')
def step_impl(context, course):
    assert course not in context.browser.page_source
