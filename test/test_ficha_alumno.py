import unittest
import os
from unittest.mock import patch, MagicMock
from app import create_app, db
from app.services.servicio_ficha_alumno import ServicioFichaAlumno
from test.instancias import nuevoalumno, nuevaespecialidad, nuevafacultad, nuevauniversidad

class FichaAlumnoTestCase(unittest.TestCase):
    
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        
        self.universidad = nuevauniversidad()
        self.facultad = nuevafacultad(universidad=self.universidad)
        self.especialidad = nuevaespecialidad(facultad=self.facultad)
        self.alumno = nuevoalumno(especialidad=self.especialidad)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_obtener_ficha_alumno_json(self):
        ficha = ServicioFichaAlumno.obtener_ficha_alumno_json(self.alumno.id)
        
        self.assertIsNotNone(ficha)
        self.assertEqual(ficha['nro_legajo'], self.alumno.nro_legajo)
        self.assertEqual(ficha['apellido'], self.alumno.apellido)
        self.assertEqual(ficha['nombre'], self.alumno.nombre)
        self.assertEqual(ficha['especialidad'], self.especialidad.nombre)
        self.assertEqual(ficha['facultad'], self.facultad.nombre)
        self.assertEqual(ficha['universidad'], self.universidad.nombre)

    def test_obtener_ficha_alumno_inexistente(self):
        ficha = ServicioFichaAlumno.obtener_ficha_alumno_json(99999)
        self.assertIsNone(ficha)

    def test_generar_ficha_alumno_pdf(self):
        with patch('app.services.documentos_office_service.PDFDocument.generar') as mock_pdf:
            mock_pdf.return_value = MagicMock()
            
            resultado = ServicioFichaAlumno.generar_ficha_alumno_pdf(self.alumno.id)
            
            self.assertIsNotNone(resultado)
            mock_pdf.assert_called_once()

    def test_generar_ficha_alumno_pdf_inexistente(self):
        resultado = ServicioFichaAlumno.generar_ficha_alumno_pdf(99999)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
