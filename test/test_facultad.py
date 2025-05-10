import unittest
from flask import current_app
from app import create_app
from app.models.facultad import Facultad
from app.services import FacultadService
from app import db
import os

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
        facultad = self.__nuevaFacultad()
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")
        self.assertEqual(facultad.abreviatura, "FCE")
        
    def test_crear_facultad(self):
        facultad = self.__nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        self.assertIsNotNone(facultad)
        self.assertIsNotNone(facultad.id)
        self.assertGreaterEqual(facultad.id, 1)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")
        
    def test_facultad_busqueda(self):
        facultad = self.__nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        FacultadService.buscar_por_id(facultad.id)
        self.assertIsNotNone(facultad)
        self.assertEqual(facultad.nombre, "Facultad de Ciencias Exactas")
        self.assertEqual(facultad.abreviatura, "FCE")
    
    def test_buscar_facultades(self):
        facultad1 = self.__nuevaFacultad()
        facultad2 = self.__nuevaFacultad()
        FacultadService.crear_facultad(facultad1)
        FacultadService.crear_facultad(facultad2)
        facultades = FacultadService.buscar_todos()
        self.assertIsNotNone(facultades)
        self.assertEqual(len(facultades), 2)
        
    def test_actualizar_facultad(self):
        facultad = self.__nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        facultad.nombre = "Facultad de Ciencias Naturales"
        facultad_actualizada = FacultadService.actualizar_facultad(facultad.id, facultad)
        self.assertEqual(facultad_actualizada.nombre, "Facultad de Ciencias Naturales")
        
    def test_borrar_facultad(self):
        facultad = self.__nuevaFacultad()
        FacultadService.crear_facultad(facultad)
        db.session.delete(facultad)
        db.session.commit()
        facultad_borrada = FacultadService.borrar_por_id(facultad.id)
        self.assertIsNone(facultad_borrada)
        
    def __nuevaFacultad(self):
        facultad=Facultad()
        facultad.nombre = "Facultad de Ciencias Exactas"
        facultad.abreviatura = "FCE"
        facultad.directorio = "Ciencias Exactas"
        facultad.sigla = "FCE"
        facultad.codigo_postal = "12345"
        facultad.ciudad = "La Plata"
        facultad.domicilio = "Calle 123"
        facultad.telefono = "123456789"
        facultad.contacto = "Juan Perez"
        facultad.email ="abc@gmail.com"
        return facultad

if __name__ == "_main_":
    unittest.main()
    