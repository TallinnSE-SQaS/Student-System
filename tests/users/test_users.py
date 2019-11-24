import unittest

from tests.utils import test_client


class TestUsers(unittest.TestCase):
    def test_login_with_valid_credentials_should_redirect_to_user_specific_page(self):
        credentials = {'username': 'student', 'password': 'some-password'}
        response = test_client.post('/users/login', data=credentials, follow_redirects=True)

        self.assertIn(b'Student Homepage', response.data)

    def test_login_with_invalid_credentials_should_show_error_message(self):
        credentials = {'username': 'anything is good', 'password': "doesn't matter"}
        response = test_client.post('/users/login', data=credentials, follow_redirects=True)

        self.assertIn(b'Invalid credentials', response.data)

    def test_student_successfully_enroll_in_a_course(self):
        credentials = {'username': 'student', 'password': 'some-password'}
        test_client.post('/users/login', data=credentials, follow_redirects=True)  # login first

        response = test_client.get('/courses/1')
        self.assertIn(b'Student count: 0', response.data)
        self.assertIn(b'You can enroll in this course.', response.data)

        response = test_client.post('/courses/1/enroll', follow_redirects=True)
        self.assertIn(b'Student Homepage', response.data)
        self.assertIn(b'Basic Course', response.data)

        response = test_client.get('/courses/1')
        self.assertIn(b'Student count: 1', response.data)
        self.assertIn(b'You are enrolled in this course.', response.data)
