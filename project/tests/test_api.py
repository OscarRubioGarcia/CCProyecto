import unittest

from project.CassandraLaunch import app


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

    '''
    def test_gestor_news_add(self):
        response = self.app.post('/news/add', follow_redirects=True, content_type='application/json')
        self.assertEqual(response.get_json(), {'news': [{'no news found with id': '1'}]})

    def test_gestor_news_get_all(self):
        response = self.app.get('/news', follow_redirects=True, content_type='application/json')
        self.assertEqual(response.get_json(), {'news': [{'campus': 'UGR', 'comentarios': [], 'descripcion': 'Descripcion Noticia', 'id': 1, 'titulo': 'Titulo Noticia'},
                                                        {'campus': 'UGR', 'comentarios': [], 'descripcion': 'Descripcion detallada de noticia2', 'id': 2, 'titulo': 'Noticia2'}]})
    '''


if __name__ == "__main__":
    unittest.main()
