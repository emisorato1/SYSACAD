import unittest
import os
from flask import current_app
from app import create_app
from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad

class AutoridadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_especialidad_creation(self):
        especialidad = Especialidad()
        especialidad.tipo_especialidad = TipoEspecialidad()
        especialidad.tipo_especialidad.nombre = "Especialidad 1"
        especialidad.tipo_especialidad.nivel = "Avanzado"
        especialidad.nombre = "Ingeniería de Software"
        especialidad.letra = "IS"
        especialidad.observacion = "Observación de prueba"
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.tipo_especialidad)
        self.assertEqual(especialidad.tipo_especialidad.nombre, "Especialidad 1")
        self.assertEqual(especialidad.tipo_especialidad.nivel, "Avanzado")
        self.assertEqual(especialidad.nombre, "Ingeniería de Software")
        self.assertEqual(especialidad.letra, "IS")
        self.assertEqual(especialidad.observacion, "Observación de prueba")


if __name__ == "__main__":
    unittest.main()   