import unittest
import os
from flask import current_app
from app import create_app
from app.models.orientacion import Orientacion
from app.models.especialidad import Especialidad
from app.models.tipo_especialidad import TipoEspecialidad
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
        especialidad = Especialidad()   
        tipo_especialidad = TipoEspecialidad()
        tipo_especialidad.nombre = "Especialidad 1"
        tipo_especialidad.nivel = "Avanzado"
        especialidad.nombre = "Ingeniería de Software"
        especialidad.letra = "IS"
        especialidad.observacion = "Observación de prueba"
        especialidad.tipo_especialidad = tipo_especialidad  
        orientacion.nombre = "Orientación de prueba"
        orientacion.especialidad = especialidad
        self.assertIsNotNone(orientacion)
        self.assertIsNotNone(orientacion.especialidad)
        self.assertIsNotNone(orientacion.especialidad.tipo_especialidad)
        self.assertEqual(orientacion.especialidad.tipo_especialidad.nombre, "Especialidad 1")
        self.assertEqual(orientacion.especialidad.tipo_especialidad.nivel, "Avanzado")
        self.assertEqual(orientacion.especialidad.nombre, "Ingeniería de Software")
        self.assertEqual(orientacion.especialidad.letra, "IS")
        self.assertEqual(orientacion.especialidad.observacion, "Observación de prueba")
        self.assertEqual(orientacion.nombre, "Orientación de prueba")

        ### HACER TEST DE LA ORIENTACION CON MATERIA Y PLAN ###


if __name__ == "__main__":
    unittest.main()