import unittest
import os
from flask import current_app
from app import create_app
from app.models import Autoridad, Cargo
from app.models.categoria_cargo import CategoriaCargo
from app.models.tipo_dedicacion import TipoDedicacion 

class AutoridadTestCase(unittest.TestCase):
 
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_autoridad_creation(self):
        autoridad = Autoridad()
        cargo = Cargo()
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Dedicacion simple"
        cargo.nombre = "Decano"
        cargo.puntos = 100
        self.__new_object(autoridad, cargo, tipo_dedicacion)
        self.assertIsNotNone(autoridad)
        self.assertEqual(autoridad.nombre, "Juan Perez")
        self.assertIsNotNone(autoridad.cargo)
        self.assertIsNotNone(autoridad.cargo.tipo_dedicacion)
        self.assertEqual(autoridad.cargo.nombre, "Decano")
        self.assertEqual(autoridad.telefono, "123456789")
        self.assertEqual(autoridad.email, "abc@gmail.com")
        self.assertIsNotNone(autoridad.cargo.categoria_cargo)
        self.assertEqual(autoridad.cargo.categoria_cargo.nombre, "Categoria 1")

    def __new_object(self, autoridad, cargo, tipo_dedicacion):
        cargo.categoria_cargo = CategoriaCargo()
        cargo.categoria_cargo.nombre = "Categoria 1"
        cargo.tipo_dedicacion = tipo_dedicacion
        autoridad.nombre = "Juan Perez"
        autoridad.cargo = cargo
        autoridad.telefono = "123456789"
        autoridad.email = "abc@gmail.com"


if __name__ == "__main__":
    unittest.main()