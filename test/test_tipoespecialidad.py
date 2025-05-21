import unittest
import os
from flask import current_app
from app import create_app
from app.models import TipoEspecialidad
from app.services import TipoEspecialidadService
from app import db


class TipoEspecialidadTestCase(unittest.TestCase):
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

    def test_tipoespecialidad_creation(self):
        tipoespecialidad = self.__nuevotipoespecialidad()
        self.assertIsNotNone(tipoespecialidad)
        self.assertIsNotNone(tipoespecialidad.nombre, "Cardiología")
        self.assertIsNotNone(tipoespecialidad.nivel, "Avanzado")
        


    def test_crear(self):
        tipoespecialidad = self.__nuevotipoespecialidad()
        TipoEspecialidadService.crear(tipoespecialidad)
        self.assertIsNotNone(tipoespecialidad)
        self.assertIsNotNone(tipoespecialidad.id)
        self.assertGreaterEqual(tipoespecialidad.id, 1)    
        self.assertEqual(tipoespecialidad.nombre, "Cardiología")
        self.assertEqual(tipoespecialidad.nivel, "Avanzado")

    def test_busqueda(self):
        tipoespecialidad = self.__nuevotipoespecialidad()
        TipoEspecialidadService.crear(tipoespecialidad)
        r=TipoEspecialidadService.buscar_por_id(tipoespecialidad.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, tipoespecialidad.nombre)
    
    def test_buscar_todos(self):
        tipoespecialidad1 = self.__nuevotipoespecialidad()
        tipoespecialidad2 = self.__nuevotipoespecialidad("pediatria", "Basico")
        TipoEspecialidadService.crear(tipoespecialidad1)
        TipoEspecialidadService.crear(tipoespecialidad2)
        tipoespecialidad = TipoEspecialidadService.buscar_todos()
        self.assertIsNotNone(tipoespecialidad)
        self.assertGreaterEqual(len(tipoespecialidad), 2)

    def test_actualizar(self):
        tipoespecialidad = self.__nuevotipoespecialidad()
        TipoEspecialidadService.crear(tipoespecialidad)
        tipoespecialidad.nombre = "Neurología"
        tipoespecialidad.nivel = "Intermedio"
        tipoespecialidad_actualizado = TipoEspecialidadService.actualizar(tipoespecialidad.id, tipoespecialidad)
        self.assertEqual(tipoespecialidad_actualizado.nombre, "Neurología")
        self.assertEqual(tipoespecialidad_actualizado.nivel, "Intermedio")

    def test_borrar(self):
        tipoespecialidad = self.__nuevotipoespecialidad()
        TipoEspecialidadService.crear(tipoespecialidad)
        TipoEspecialidadService.borrar_por_id(tipoespecialidad.id)
        resultado =  TipoEspecialidadService.buscar_por_id(tipoespecialidad.id)
        self.assertIsNone(resultado)
    

    def __nuevotipoespecialidad(self, nombre="Cardiología", nivel="Avanzado"):
        tipoespecialidad = TipoEspecialidad()
        tipoespecialidad.nombre = nombre
        tipoespecialidad.nivel = nivel
        return tipoespecialidad