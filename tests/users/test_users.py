import unittest

from tests.utils import test_client


class TestUsers(unittest.TestCase):
    def test_login_with_valid_credentials_should_redirect_to_user_specific_page(self):
        credentials = {'username': 'student', 'password': 'some-password'}
        response = test_client.post('/users/login', data=credentials, follow_redirects=True)

        self.assertIn(b'Student Homepage', response.data)

    def test_login_with_invalid_credentials_should_show_error_message(self):
        credentials = {'username': 'student', 'password': "wrong"}
        response = test_client.post('/users/login', data=credentials, follow_redirects=True)

        self.assertIn(b'Invalid credentials', response.data)

        credentials = {'username': 'non-existent', 'password': "can even be empty"}
        response = test_client.post('/users/login', data=credentials, follow_redirects=True)

        self.assertIn(b'Invalid credentials', response.data)
