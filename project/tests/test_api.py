import os
import unittest

from project.Main import app


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_main_page_error(self):
        response = self.app.get('/error', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_gestor_news(self):
        response = self.app.get('/news', follow_redirects=True, content_type='application/json')
        print(response.get_json())


if __name__ == "__main__":
    unittest.main()
