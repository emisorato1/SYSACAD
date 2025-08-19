from app.models import TipoDocumento
from app.repositories import TipoDocumentoRepository

class TipoDocumentoService:

    @staticmethod
    def crear(tipodocumento):
        TipoDocumentoRepository.crear(tipodocumento)

    @staticmethod
    def buscar_por_id(id: int) -> TipoDocumento:
        # pyrefly: ignore  # bad-return
        return TipoDocumentoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[TipoDocumento]:
        return TipoDocumentoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, tipodocumento: TipoDocumento) -> TipoDocumento:
        tipodocumento_existente = TipoDocumentoRepository.buscar_por_id(id)
        if not tipodocumento_existente:
            # pyrefly: ignore  # bad-return
            return None
        tipodocumento_existente.dni = tipodocumento.dni
        tipodocumento_existente.libreta_civica = tipodocumento.libreta_civica
        tipodocumento_existente.libreta_enrolamiento = tipodocumento.libreta_enrolamiento
        tipodocumento_existente.pasaporte = tipodocumento.pasaporte
        return tipodocumento_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        return TipoDocumentoRepository.borrar_por_id(id)
