from app.models import TipoDocumento
from app.repositories import TipoDocumentoRepository

class TipoDocumentoService:

    @staticmethod
    def crear(tipodocumento):
        """
        Crea un nuevo tipo de documento en la base de datos.
        :param tipodocumento: Objeto TipoDocumento a crear.
        :return: Objeto TipoDocumento creado.
        """
        TipoDocumentoRepository.crear(tipodocumento)

    @staticmethod
    def buscar_por_id(id: int) -> TipoDocumento:
        """
        Busca un tipo de documento por su ID.
        :param id: ID del tipo de documento a buscar.
        :return: Objeto TipoDocumento encontrado o None si no se encuentra.
        """
        return TipoDocumentoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[TipoDocumento]:
        """
        Busca todos los tipos de documentos en la base de datos.
        :return: Lista de objetos TipoDocumento.
        """
        return TipoDocumentoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, tipodocumento: TipoDocumento) -> TipoDocumento:
        """
        Actualiza un tipo de documento existente en la base de datos.
        :param id: ID del tipo de documento a actualizar.
        :param tipodocumento: Objeto TipoDocumento con los nuevos datos.
        :return: Objeto TipoDocumento actualizado o None si no se encuentra.
        """
        tipodocumento_existente = TipoDocumentoRepository.buscar_por_id(id)
        if not tipodocumento_existente:
            return None
        tipodocumento_existente.dni = tipodocumento.dni
        tipodocumento_existente.libreta_civica = tipodocumento.libreta_civica
        tipodocumento_existente.libreta_enrolamiento = tipodocumento.libreta_enrolamiento
        tipodocumento_existente.pasaporte = tipodocumento.pasaporte
        return tipodocumento_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> TipoDocumento:
        """
        Borra un tipo de documento por su ID.
        :param id: ID del tipo de documento a borrar.
        :return: True si se borra correctamente, False si no se encuentra.
        """
        tipodocumento = TipoDocumentoRepository.borrar_por_id(id)
        if not tipodocumento:
            return None
        return tipodocumento