import unittest
import os
from flask import current_app
from app import create_app
from datetime import date
from app.models.tipodocumento import TipoDocumento
from app.models.alumno import Alumno
from app.services import AlumnoService
from app.services import TipoDocumentoService
from app import db
class AlumnoTestCase(unittest.TestCase):

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

    def test_alumno_creation(self):
        alumno = self.__nuevoalumno()
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.nombre)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.tipo_documento.pasaporte, "nacnal")

    def test_crear(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        self.assertIsNotNone(alumno)
        self.assertIsNotNone(alumno.nombre)
        self.assertGreaterEqual(alumno.id, 1)
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.tipo_documento.pasaporte, "nacnal")

    def test_busqueda(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        r=AlumnoService.buscar_por_id(alumno.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Juan")
        self.assertEqual(r.apellido, "Pérez")

    def test_buscar_todos(self):
        alumno1 = self.__nuevoalumno()
        alumno2 = self.__nuevoalumno(nombre="Pedro", apellido="Gómez", nrodocumento="12345678", tipo_documento=None, fecha_nacimiento=date(1995,5,5), sexo="M", nro_legajo=654321, fecha_ingreso=date(2021,1,1), dni= "na", libreta_civica="l", libreta_enrolamiento="aci", pasaporte="nacn")
        AlumnoService.crear(alumno1)
        AlumnoService.crear(alumno2)
        alumnos = AlumnoService.buscar_todos()
        self.assertIsNotNone(alumnos)
        self.assertEqual(len(alumnos), 2)

    def test_actualizar(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        alumno.nombre = "Juan actualizado"
        alumno_actualizado = AlumnoService.actualizar(alumno.id, alumno)
        self.assertEqual(alumno_actualizado.nombre, "Juan actualizado")
    
    def test_borrar(self):
        alumno = self.__nuevoalumno()
        AlumnoService.crear(alumno)
        AlumnoService.borrar_por_id(alumno.id)
        resultado = AlumnoService.buscar_por_id(alumno.id)
        self.assertIsNone(resultado)



    def __nuevoalumno(self, nombre="Juan", apellido="Pérez", nrodocumento="46291002" ,tipo_documento=None, fecha_nacimiento=date(1990,1,1), sexo="M", nro_legajo=123456, fecha_ingreso=date(2020,1,1),
                      dni= "nacnal", libreta_civica="nacional", libreta_enrolamiento="naci", pasaporte="nacnal"):
        tipo_documento = TipoDocumento()
        tipo_documento.pasaporte = pasaporte
        tipo_documento.dni = dni
        tipo_documento.libreta_civica = libreta_civica
        tipo_documento.libreta_enrolamiento = libreta_enrolamiento
        TipoDocumentoService.crear(tipo_documento)
        
        alumno = Alumno()
        alumno.nombre =  nombre
        alumno.apellido = apellido
        alumno.nrodocumento = nrodocumento
        alumno.tipo_documento = tipo_documento
        alumno.fecha_nacimiento = fecha_nacimiento
        alumno.sexo = sexo
        alumno.nro_legajo = nro_legajo
        alumno.fecha_ingreso = fecha_ingreso
        return alumno
        