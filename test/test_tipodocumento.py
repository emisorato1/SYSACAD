import unittest
import os
from flask import current_app
from app import create_app
from app.models.tipodocumento import TipoDocumento
from app.services import TipoDocumentoService
from app import db

class TipoDocumentoTestCase(unittest.TestCase):
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

    def test_tipodocumento_creation(self):
        tipodocumento = self.__nuevotipodoumento()
        self.assertIsNotNone(tipodocumento)
        self.assertIsNotNone(tipodocumento.dni)
        self.assertEqual(tipodocumento.dni, "DNI")
        self.assertEqual(tipodocumento.libreta_civica, "12345678")
        self.assertEqual(tipodocumento.libreta_enrolamiento, "87654321")

    def test_crear(self):
        tipodocumento = self.__nuevotipodoumento()
        TipoDocumentoService.crear(tipodocumento)
        self.assertIsNotNone(tipodocumento)
        self.assertIsNotNone(tipodocumento.id)
        self.assertGreaterEqual(tipodocumento.id, 1)
        self.assertEqual(tipodocumento.dni, "DNI")

    def test_busqueda(self):
        tipodocumento = self.__nuevotipodoumento()
        TipoDocumentoService.crear(tipodocumento)
        r=TipoDocumentoService.buscar_por_id(tipodocumento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.dni, "DNI")
        self.assertEqual(r.libreta_civica, "12345678")

    def test_buscar_todos(self):
        tipodocumento1 = self.__nuevotipodoumento()
        tipodocumento2 = self.__nuevotipodoumento("DNI2", "23456789", "98765432", "CD123456")
        TipoDocumentoService.crear(tipodocumento1)
        TipoDocumentoService.crear(tipodocumento2)
        documentos = TipoDocumentoService.buscar_todos()
        self.assertIsNotNone(documentos)
        self.assertEqual(len(documentos), 2)

    def test_actualizar(self):
        tipodocumento = self.__nuevotipodoumento()
        TipoDocumentoService.crear(tipodocumento)
        tipodocumento.dni = "DNI actualizado"
        tipodocumento_actualizado = TipoDocumentoService.actualizar(tipodocumento.id, tipodocumento)
        self.assertEqual(tipodocumento_actualizado.dni, "DNI actualizado")
    
    def test_borrar(self):
        tipodocumento = self.__nuevotipodoumento()
        TipoDocumentoService.crear(tipodocumento)
        TipoDocumentoService.borrar_por_id(tipodocumento.id)
        resultado = TipoDocumentoService.buscar_por_id(tipodocumento.id)
        self.assertIsNone(resultado)


    def __nuevotipodoumento(self, dni="DNI", libreta_civica="12345678", libreta_enrolamiento="87654321", pasaporte="AB123456"):
        tipodocumento = TipoDocumento()
        tipodocumento.dni = dni
        tipodocumento.libreta_civica = libreta_civica
        tipodocumento.libreta_enrolamiento = libreta_enrolamiento
        tipodocumento.pasaporte = pasaporte
        return tipodocumento