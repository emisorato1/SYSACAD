import datetime
from io import BytesIO
from app.models import Alumno
from app.repositories import AlumnoRepository
from app.services.documentos_office_service import obtener_tipo_documento

class CertificateService:
    @staticmethod
    def generar_certificado_alumno_regular(id: int, tipo: str) -> BytesIO:
        alumno = AlumnoRepository.buscar_por_id(id)
        if not alumno:
            return None
        
        context = CertificateService._obtener_contexto_alumno(alumno)
        documento = obtener_tipo_documento(tipo)
        if not documento:
            return None
            
        if tipo in ('odt', 'docx'):
            plantilla = 'certificado_plantilla'
        else:
            plantilla = 'certificado_pdf'

        return documento.generar(
            carpeta='certificado',
            plantilla=plantilla,
            context=context
        )
    
    @staticmethod
    def _obtener_contexto_alumno(alumno: Alumno) -> dict:
        especialidad = alumno.especialidad
        facultad = especialidad.facultad
        universidad = facultad.universidad
        return {
            "alumno": alumno,
            "especialidad": especialidad,
            "facultad": facultad,
            "universidad": universidad,
            "fecha": CertificateService._obtener_fechaactual()
        }
    
    @staticmethod
    def _obtener_fechaactual():
        fecha_actual = datetime.datetime.now()
        fecha_str = fecha_actual.strftime('%d de %B de %Y')
        return fecha_str
