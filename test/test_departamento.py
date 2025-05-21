import unittest
import os
from flask import current_app
from app import create_app
from app.models.departamento import Departamento
from app.services import DepartamentoService
from app import db

class DepartamentoTestCase(unittest.TestCase):
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

    def test_departamento_creation(self):
        departamento = self.__nuevodepartamento()
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.nombre)
        self.assertEqual(departamento.nombre, "Matematicas")

    
    def test_crear(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        self.assertIsNotNone(departamento)
        self.assertIsNotNone(departamento.id)
        self.assertGreaterEqual(departamento.id, 1)
        self.assertEqual(departamento.nombre, "Matematicas")

    def test_busqueda(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        r=DepartamentoService.buscar_por_id(departamento.id)
        self.assertIsNotNone(r)
        self.assertEqual(r.nombre, "Matematicas")
        

    def test_buscar_todos(self):
        departamento1 = self.__nuevodepartamento()
        departamento2 = self.__nuevodepartamento("Fisica")
        DepartamentoService.crear(departamento1)
        DepartamentoService.crear(departamento2)
        departamentos = DepartamentoService.buscar_todos()
        self.assertIsNotNone(departamentos)
        self.assertEqual(len(departamentos), 2)

    def test_actualizar(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        departamento.nombre = "Matematicas actualizado"
        departamento_actualizado = DepartamentoService.actualizar(departamento.id, departamento)
        self.assertEqual(departamento_actualizado.nombre, "Matematicas actualizado")
    
    def test_borrar(self):
        departamento = self.__nuevodepartamento()
        DepartamentoService.crear(departamento)
        DepartamentoService.borrar_por_id(departamento.id)
        resultado = DepartamentoService.buscar_por_id(departamento.id)
        self.assertIsNone(resultado)
        
    def __nuevodepartamento(self , nombre = "Matematicas"):
        departamento = Departamento()
        departamento.nombre = nombre
        return departamento