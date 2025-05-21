import unittest
import os
from flask import current_app
from app import create_app
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.plan import Plan
from app.models.materia import Materia

class OrientacionTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_orientacion_creation(self):
        orientacion = Orientacion()
        orientacion.nombre = "Orientacion A"
        orientacion.observacion = "Observacion de prueba"
        orientacion.especialidad = Especialidad()
        orientacion.plan = Plan()
        orientacion.materia = Materia()

        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.nombre)
        self.assertEqual(orientacion.nombre, "Orientacion A")
        self.assertEqual(orientacion.observacion, "Observacion de prueba")