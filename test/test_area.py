import unittest
import os
from flask import current_app
from app import create_app
from app.models.area import Area

class AreaTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_area_creation(self):
        area = Area()
        area.nombre = "matematica"
        self.assertIsNotNone(area)
        self.assertIsNotNone(area.nombre)
        self.assertEqual(area.nombre, "matematica")