import unittest
import os
from flask import current_app
from app import create_app
from app.models.grupo import Grupo

class GrupoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_grupo_creation(self):
        grupo = Grupo()
        grupo.nombre = "Grupo A"
        self.assertIsNotNone(grupo)
        self.assertIsNotNone(grupo.nombre)
        self.assertEqual(grupo.nombre, "Grupo A")