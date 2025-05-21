from app.models import Facultad
from app.repositories import FacultadRepository

class FacultadService:
    """
    Servicio para gestionar las facultades.
    """
    @staticmethod
    def crear_facultad(facultad: Facultad):
        """
        Crea una nueva facultad en la base de datos.
        :param facultad: Facultad a crear.
        :return: Facultad creada.
        """
        FacultadRepository.crear(facultad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Facultad:
        """
        Busca una facultad por su ID.
        :param id: ID de la facultad a buscar.
        :return: Facultad encontrada o None si no se encuentra.
        """
        return FacultadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Facultad]:
        """
        Busca todas las facultades en la base de datos.
        :return: Lista de facultades.
        """
        return FacultadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_facultad(id: int, facultad: Facultad) -> Facultad:
        """
        Actualiza una facultad existente en la base de datos.
        :param id: ID de la facultad a actualizar.
        :param facultad: Objeto Facultad con los nuevos datos.
        :return: Objeto Facultad actualizada.
        """
        facultad_existente = FacultadRepository.buscar_por_id(id)
        if not facultad_existente:
            return None
        facultad_existente.nombre = facultad.nombre
        facultad_existente.abreviatura = facultad.abreviatura
        facultad_existente.directorio = facultad.directorio
        facultad_existente.sigla = facultad.sigla
        facultad_existente.codigopostal = facultad.codigopostal
        facultad_existente.ciudad = facultad.ciudad
        facultad_existente.domicilio = facultad.domicilio
        facultad_existente.telefono = facultad.telefono
        facultad_existente.contacto = facultad.contacto
        return facultad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Facultad:
        """
        Borra una facultad por su ID.
        :param id: ID de la facultad a borrar.
        :return: Objeto Facultad borrado o None si no se encuentra.
        """

        facultad = FacultadRepository.borrar_por_id(id)
        if not facultad:
            return None
        return facultad