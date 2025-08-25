import unittest
import os
from flask import current_app
from app import create_app
from app import db
from app.mapping import UniversidadMapping
from test.instancias import nuevauniversidad

class IndexTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_obtener_por_id(self):
        client = self.app.test_client(use_cookies=True)
        u = nuevauniversidad()

        resp = client.get(f'/api/v1/universidad/{u.hashid}')
        self.assertEqual(resp.status_code, 200)

        data = resp.get_json()
        self.assertIsNotNone(data)
        self.assertEqual(data["hashid"], u.hashid)
        self.assertEqual(data["nombre"], u.nombre)
        self.assertEqual(data["sigla"], u.sigla)

    def test_obtener_todos(self):
        client = self.app.test_client(use_cookies=True)
        universidad1 = nuevauniversidad()
        universidad2 = nuevauniversidad()
        universidad_mapping = UniversidadMapping()
        response = client.get('http://localhost:5000/api/v1/universidad')
        universidades = universidad_mapping.load(response.get_json(), many=True)
        self.assertEqual(len(universidades), 2)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.get_json())    

        
