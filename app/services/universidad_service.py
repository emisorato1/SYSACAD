from app.models.universidad import Universidad
from app.repositories import UniversidadRepository

class UniversidadService:
    @staticmethod
    def crear_universidad(universidad: Universidad):
        """
        Crea una nueva universidad en la base de datos.
        :param universidad: Universidad a crear.
        :return: Universidad creada.
        """
        UniversidadRepository.crear(universidad)
    
    @staticmethod
    def buscar_por_id(id: int) -> Universidad:
        """
        Busca una universidad por su ID.
        :param universidad_id: ID de la universidad a buscar.
        :return: Universidad encontrada o None si no existe.
        """
        return UniversidadRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Universidad]:
        """
        Busca todas las universidades en la base de datos.
        :return: Lista de universidades.
        """
        return UniversidadRepository.buscar_todos()
    
    @staticmethod
    def actualizar_universidad(id: int, universidad: Universidad) -> Universidad:
        """
        Actualiza una universidad existente en la base de datos.
        :param id: ID de la universidad a actualizar.
        :param universidad: Universidad con los nuevos datos.
        :return: Universidad actualizada.
        """
        universidad_existente = UniversidadRepository.buscar_por_id(id)
        if not universidad_existente:
            return None
        universidad_existente.nombre = universidad.nombre
        universidad_existente.sigla = universidad.sigla
        return universidad_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Universidad:
        """
        Borra una universidad por su ID.
        :param id: ID de la universidad a borrar.
        :return: Objeto Universidad borrado o None si no se encuentra.
        """

        universidad = UniversidadRepository.borrar_por_id(id)
        if not universidad:
            return None
        return universidad
    