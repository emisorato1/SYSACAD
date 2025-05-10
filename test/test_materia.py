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
        materia.nombre = "Matemáticas"
        materia.codigo = "MAT101"
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matemáticas")
        self.assertEqual(materia.codigo, "MAT101")

if __name__ == "__main__":
    unittest.main()