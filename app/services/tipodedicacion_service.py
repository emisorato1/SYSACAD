from app.models import TipoDedicacion
from app.repositories import TipoDedicacionRepository

class TipoDedicacionService:

    @staticmethod
    def crear(tipodedicacion):
        return TipoDedicacionRepository.crear(tipodedicacion)
    
    @staticmethod
    def buscar_por_id(id: int) -> TipoDedicacion:
        # pyrefly: ignore  # bad-return
        return TipoDedicacionRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[TipoDedicacion]:
        return TipoDedicacionRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, tipodedicacion: TipoDedicacion) -> TipoDedicacion:
        tipodedicacion_existente = TipoDedicacionRepository.buscar_por_id(id)
        if not tipodedicacion_existente:
            # pyrefly: ignore  # bad-return
            return None
        tipodedicacion_existente.nombre = tipodedicacion.nombre
        tipodedicacion_existente.observacion = tipodedicacion.observacion
        return tipodedicacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return TipoDedicacionRepository.borrar_por_id(id)
    
