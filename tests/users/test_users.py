import unittest

from tests.utils import test_client


class TestUsers(unittest.TestCase):
    def test_login_with_valid_credentials_should_redirect_to_user_specific_page(self):
        credentials = {'username': 'student', 'password': 'some-password'}
        response = test_client.post('/users/login', data=credentials, follow_redirects=True)

        self.assertIn(b'Student Homepage', response.data)

        test_client.get('/users/logout', follow_redirects=True)
