from app.services.alumno_crud_service import AlumnoCRUDService
from app.services.certificate_service import CertificateService

class AlumnoService:
    @staticmethod
    def crear(alumno):
        return AlumnoCRUDService.crear(alumno)

    @staticmethod
    def buscar_por_id(id: int):
        return AlumnoCRUDService.buscar_por_id(id)

    @staticmethod
    def buscar_todos():
        return AlumnoCRUDService.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, alumno):
        return AlumnoCRUDService.actualizar(id, alumno)
        
    @staticmethod
    def borrar_por_id(id: int):
        return AlumnoCRUDService.borrar_por_id(id)
    
    @staticmethod
    def generar_certificado_alumno_regular(id: int, tipo: str):
        return CertificateService.generar_certificado_alumno_regular(id, tipo)
