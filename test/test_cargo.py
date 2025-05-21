import unittest
import os
from flask import current_app
from app import create_app
from app.models.cargo import Cargo
from app.models.categoriacargo import CategoriaCargo
from app.models.tipodedicacion import TipoDedicacion

class CargoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_cargo_creation(self):
        cargo = Cargo()
        cargo.nombre = "profesor"
        cargo.puntos = 10
        categoria_cargo = CategoriaCargo()
        categoria_cargo.nombre = "Categoria 1"
        cargo.categoria_cargo = categoria_cargo
        tipo_dedicacion = TipoDedicacion()
        tipo_dedicacion.nombre = "Tipo 1"
        cargo.tipo_dedicacion = tipo_dedicacion
        self.assertIsNotNone(cargo)
        self.assertIsNotNone(cargo.nombre)
        self.assertEqual(cargo.nombre, "profesor")
        self.assertEqual(cargo.puntos, 10)
        self.assertEqual(cargo.categoria_cargo.nombre, "Categoria 1")
        self.assertEqual(cargo.tipo_dedicacion.nombre, "Tipo 1")