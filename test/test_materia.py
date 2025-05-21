import unittest
import os
from flask import current_app
from app import create_app
from app.models.materia import Materia

class MateriaTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_materia_creation(self):
        materia = Materia()
        materia.nombre = "Matematicas"
        materia.codigo = "MAT101"
        materia.observacion = "Observacion de prueba"
        self.assertIsNotNone(materia)
        self.assertIsNotNone(materia.nombre)
        self.assertEqual(materia.nombre, "Matematicas")
        self.assertEqual(materia.codigo, "MAT101")
        self.assertEqual(materia.observacion, "Observacion de prueba")