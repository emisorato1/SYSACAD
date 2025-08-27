from app.services.alumno_crud_service import AlumnoCRUDService
from app.services.documentos_office_service import obtener_tipo_documento

class ServicioFichaAlumno:
    @staticmethod
    def obtener_ficha_alumno_json(id: int):
        alumno = AlumnoCRUDService.buscar_por_id(id)
        if not alumno:
            return None
        
        return {
            "nro_legajo": alumno.nro_legajo,
            "apellido": alumno.apellido,
            "nombre": alumno.nombre,
            "nrodocumento": alumno.nrodocumento,
            "tipo_documento": alumno.tipo_documento.dni if alumno.tipo_documento else None,
            "fecha_nacimiento": str(alumno.fecha_nacimiento),
            "sexo": alumno.sexo,
            "fecha_ingreso": str(alumno.fecha_ingreso),
            "especialidad": alumno.especialidad.nombre if alumno.especialidad else None,
            "facultad": alumno.especialidad.facultad.nombre if alumno.especialidad and alumno.especialidad.facultad else None,
            "universidad": alumno.especialidad.facultad.universidad.nombre if alumno.especialidad and alumno.especialidad.facultad and alumno.especialidad.facultad.universidad else None
        }
    
    @staticmethod
    def generar_ficha_alumno_pdf(id: int):
        alumno = AlumnoCRUDService.buscar_por_id(id)
        if not alumno:
            return None
        
        context = ServicioFichaAlumno._obtener_contexto_ficha(alumno)
        documento = obtener_tipo_documento('pdf')
        if not documento:
            return None
        
        return documento.generar(
            carpeta='ficha_alumno',
            plantilla='ficha_alumno',
            context=context
        )
    
    @staticmethod
    def _obtener_contexto_ficha(alumno):
        return {
            "alumno": alumno,
            "especialidad": alumno.especialidad,
            "facultad": alumno.especialidad.facultad if alumno.especialidad else None,
            "universidad": alumno.especialidad.facultad.universidad if alumno.especialidad and alumno.especialidad.facultad else None
        }
