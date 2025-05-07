import unittest
from flask import current_app
from app import create_app
import os
from app.models.tipo_dedicacion import TipoDedicacion

class AppTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_tipo_dedicacion(self):
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Dedicacion simple"
        self.assertIsNotNone(tipo_dedicacion)
        self.assertEqual(tipo_dedicacion.nombre, "Dedicacion simple")

if __name__ == "__main__":
    unittest.main() 