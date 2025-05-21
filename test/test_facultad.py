import unittest
import os
from flask import current_app
from app import create_app
from app.models.facultad import Facultad
from app.services.facultad_service import FacultadService
from app import db

class FacultadTestCase(unittest.TestCase):
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

    def test_facultad_creation(self):
        facultad = self.__nuevafacultad()
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.nombre)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias")
        self.assertEqual(facultad.abreviatura, "FCC")
        self.assertEqual(facultad.directorio, "/facultad/ciencias")

    def test_crear_facultad(self):
        facultad = self.__nuevafacultad()
        FacultadService.crear_facultad(facultad)
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias")

    def test_facultad_busqueda(self):
        facultad = self.__nuevafacultad()
        FacultadService.crear_facultad(facultad)    
        r=FacultadService.buscar_por_id(facultad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Facultad de Ciencias")
        self.assertEqual(r.abreviatura, "FCC")


    def test_buscar_facultades(self):
        facultad1 = self.__nuevafacultad()
        facultad2 = self.__nuevafacultad()
        FacultadService.crear_facultad(facultad1)
        FacultadService.crear_facultad(facultad2)
        facultades = FacultadService.buscar_todos()
        self.assertIsNotNone(facultades)
        self.assertEqual(len(facultades), 2)

    def test_actualizar_facultad(self):
        facultad= self.__nuevafacultad()
        FacultadService.crear_facultad(facultad)
        facultad.nombre = "Facultad de Ciencias Actualizada"
        facultad_actualizada = FacultadService.actualizar_facultad(facultad.id, facultad)
        self.assertEqual(facultad_actualizada.nombre, "Facultad de Ciencias Actualizada")

    def test_borrar_facultad(self):
        facultad = self.__nuevafacultad()
        FacultadService.crear_facultad(facultad)
        FacultadService.borrar_por_id(facultad.id)
        resultado = FacultadService.buscar_por_id(facultad.id)
        self.assertIsNone(resultado)
    
    def __nuevafacultad(self):
        facultad = Facultad()
        facultad.nombre = "Facultad de Ciencias"
        facultad.abreviatura = "FCC"
        facultad.directorio = "/facultad/ciencias"
        facultad.sigla = "FC"
        facultad.codigopostal = "12345"
        facultad.ciudad = "Ciudad"
        facultad.domicilio = "Calle 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Juan Perez"
        facultad.email = "1234@gmail.com"
        return facultad