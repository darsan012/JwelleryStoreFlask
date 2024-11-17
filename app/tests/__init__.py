import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # setting up the instance of app for testing
        self.app = app.test_client()
        self.app.testing = True
    # testing /home route with the status code 200
    def test_get_home_status_code(self):
        # send request to the /home route
        response = self.app.get('/home')

        # check for status code
        self.assertEqual(200, response.status_code)

    # testing /home for post request, which must send status code 405
    def test_post_home_status_code(self):
        # send request to the /home route
        response = self.app.post('/home')

        # check for status code
        self.assertEqual(405, response.status_code)