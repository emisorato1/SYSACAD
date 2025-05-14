import unittest
import os
from flask import current_app
from app import create_app
from app.models.materia import Materia

from app.services import MateriaService
from app import db

class MateriaTestCase(unittest.TestCase):

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
    
    def test_materia_creation(self):
        materia = Materia()
        materia.nombre = "Matemáticas"
        materia.codigo = "MAT101"
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matemáticas")
        self.assertEqual(materia.codigo, "MAT101")

         
    def test_crear_materia(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        self.assertIsNotNone(materia)
        self.assertIsNotNone(materia.id)
        self.assertGreaterEqual(materia.id, 1)
        self.assertEqual(materia.nombre, "Matemáticas")
        
    def test_materia_busqueda(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        MateriaService.buscar_por_id(materia.id)
        self.assertIsNotNone(materia)
        self.assertEqual(materia.nombre, "Matemáticas")
        self.assertEqual(materia.codigo, "MAT101")
    
    def test_buscar_materias(self):
        materia1 = self.__nuevaMateria()
        materia2 = self.__nuevaMateria()
        MateriaService.crear_materia(materia1)
        MateriaService.crear_materia(materia2)
        materias = MateriaService.buscar_todos()
        self.assertIsNotNone(materias)
        self.assertEqual(len(materias), 2)

        
    def test_actualizar_materia(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        materia.nombre = "Matemáticas Avanzadas"
        materia_actualizada = MateriaService.actualizar_materia(materia.id, materia)
        self.assertEqual(materia_actualizada.nombre, "Matemáticas Avanzadas")
        
    def test_borrar_materia(self):
        materia = self.__nuevaMateria()
        MateriaService.crear_materia(materia)
        db.session.delete(materia)
        db.session.commit()
        materia_borrada = MateriaService.borrar_por_id(materia.id)
        self.assertIsNone(materia_borrada)
        
    def __nuevaMateria(self):
        materia = Materia()
        materia.nombre = "Matemáticas"
        materia.codigo = "MAT101"
        return materia


if __name__ == "__main__":
    unittest.main()