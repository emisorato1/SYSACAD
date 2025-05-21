from app.models import Grado
from app.repositories import GradoRepository

class GradoService:

    @staticmethod
    def crear_grado(grado: Grado):
        """
        Crea un nuevo cargo en la base de datos.
        :param cargo: Objeto Cargo a crear.
        :return: Objeto Cargo creado.
        """
        GradoRepository.crear(grado)
    
    @staticmethod
    def buscar_por_id(id: int) -> Grado:
        """
        Busca un grado por su ID.
        :param id: ID del grado a buscar.
        :return: Objeto Grado encontrado o None si no se encuentra.
        """
        return GradoRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Grado]:
        """
        Busca todos los grados en la base de datos.
        :return: Lista de objetos Grado.
        """
        return GradoRepository.buscar_todos()
    
    @staticmethod
    def actualizar_grado(grado: Grado):
        """
        Actualiza un grado en la base de datos.
        :param grado: Objeto Grado a actualizar.
        :return: Objeto Grado actualizado.
        """
        grado_existente = GradoRepository.buscar_por_id(grado.id)
        if not grado_existente:
            return None
        grado_existente.nombre = grado.nombre       
        grado_existente.descripcion = grado.descripcion
        return grado_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Grado:
        """
        Borra un grado por su ID.
        :param id: ID del grado a borrar.
        :return: Objeto Grado borrado o None si no se encuentra.
        """
        grado = GradoRepository.borrar_por_id(id)
        if not grado:
            return None
        return grado