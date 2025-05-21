import unittest
import os
from flask import current_app
from app import create_app
from app.models import Grado
from app.services import GradoService
from app import db


class GradoTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
    
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_grado_creation(self):
        grado = self.__nuevogrado()
        self.assertIsNotNone(grado)
        self.assertEqual(grado.nombre, "Primero")
        self.assertIsNotNone(grado.descripcion, "Descripción del primer grado")

    def test_crear_grado(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)
        self.assertIsNotNone(grado)
        self.assertIsNotNone(grado.id)
        self.assertGreaterEqual(grado.id, 1)
        self.assertEqual(grado.nombre, "Primero")

    def test_grado_busqueda(self):
        grado = self.__nuevogrado()
        GradoService.crear_grado(grado)
        r=GradoService.buscar_por_id(grado.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Primero")
        self.assertEqual(r.descripcion, "Descripción del primer grado")

    
    def test_buscar_grados(self):
        grado1 = self.__nuevogrado()
        grado2 = self.__nuevogrado()
        GradoService.crear_grado(grado1)
        GradoService.crear_grado(grado2)
        grados = GradoService.buscar_todos()
        self.assertIsNotNone(grados)
        self.assertGreaterEqual(len(grados), 2)

    def test_actualizar_grado(self):
        grado= self.__nuevogrado()
        GradoService.crear_grado(grado)
        grado.nombre = "Segundo"
        grado.descripcion = "Descripción del segundo grado"

    def test_borrar_grado(self):
        universidad = self.__nuevogrado()
        GradoService.crear_grado(universidad)
        GradoService.borrar_por_id(universidad.id)
        resultado = GradoService.buscar_por_id(universidad.id)
        self.assertIsNone(resultado)

    def __nuevogrado(self):
        grado = Grado()
        grado.nombre = "Primero"
        grado.descripcion = "Descripción del primer grado"
        return grado