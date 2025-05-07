import unittest
import os
from flask import current_app
from app import create_app
from app.models.tipo_especialidad import TipoEspecialidad

class TipoEspecialidadTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_tipo_especialidad_creation(self):
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = "Especialidad 1"
        tipo_especialidad.nivel = "Avanzado"
        self.assertIsNotNone(tipo_especialidad)
        self.assertEqual(tipo_especialidad.nombre, "Especialidad 1")


if __name__ == '__main__':
    unittest.main()