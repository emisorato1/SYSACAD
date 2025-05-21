import unittest
import os
from flask import current_app
from app import create_app
from app.models.especialidad import Especialidad
from app.services import EspecialidadService
from app import db

class EspecialidadTestCase(unittest.TestCase):
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

    def test_especialidad_creation(self):
        especialidad = self.__nuevaespecialidad()
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.nombre)
        self.assertEqual(especialidad.nombre, "Matematicas")
        self.assertEqual(especialidad.letra, "A")
        self.assertEqual(especialidad.observacion, "Observacion de prueba")


    def test_crear(self):
        especialidad= self.__nuevaespecialidad()
        EspecialidadService.crear(especialidad)
        self.assertIsNotNone(especialidad)
        self.assertIsNotNone(especialidad.id)
        self.assertGreaterEqual(especialidad.id,1)
        self.assertEqual(especialidad.nombre, "Matematicas")

    def test_busqueda(self):
        especialidad = self.__nuevaespecialidad()
        EspecialidadService.crear(especialidad)
        r=EspecialidadService.buscar_por_id(especialidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematicas")
        self.assertEqual(r.letra, "A")

    def test_buscar_todos(self):
        especialidad1 = self.__nuevaespecialidad()
        especialidad2 = self.__nuevaespecialidad()
        EspecialidadService.crear(especialidad1)
        EspecialidadService.crear(especialidad2)
        especialidades = EspecialidadService.buscar_todos()
        self.assertIsNotNone(especialidades)
        self.assertEqual(len(especialidades),2)

    def test_actualizar(self):
        especialidad = self.__nuevaespecialidad()
        EspecialidadService.crear(especialidad)
        especialidad.nombre = "matematica actualizada"
        especialidad_actualizada = EspecialidadService.actualizar(especialidad.id, especialidad)
        self.assertEqual(especialidad_actualizada.nombre, "matematica actualizada")

    def test_borrar(self):
        especialidad = self.__nuevaespecialidad()
        EspecialidadService.crear(especialidad)
        EspecialidadService.borrar_por_id(especialidad.id)
        resultado = EspecialidadService.buscar_por_id(especialidad.id)
        self.assertIsNone(resultado)

    def __nuevaespecialidad(self):
        especialidad = Especialidad()
        especialidad.nombre = "Matematicas"
        especialidad.letra = "A"
        especialidad.observacion = "Observacion de prueba"
        return especialidad