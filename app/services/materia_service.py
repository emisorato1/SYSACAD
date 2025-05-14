from app.models import Materia
from app.repositories.materia_repositorio import MateriaRepository


 
class MateriaService:
    """
    Clase de servicio para la entidad Materia.
    """
    @staticmethod
    def crear_materia(materia: Materia):
        """
        Crea una nueva materia en la base de datos.
        :param materia: Objeto Materia a crear.
        :return: Objeto Materia creado.
        """
        MateriaRepository.crear(materia)
    
    @staticmethod
    def buscar_por_id(id: int) -> Materia:
        """
        Busca una materia por su ID.
        :param id: ID de la materia a buscar.
        :return: Objeto Materia encontrado o None si no se encuentra.
        """
        return MateriaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Materia]:
        """
        Busca todas las materias en la base de datos.
        :return: Lista de objetos Materia.
        """
        return MateriaRepository.buscar_todos()
    
    @staticmethod
    def actualizar_materia(id: int, materia: Materia) -> Materia:
        """
        Actualiza una materia existente en la base de datos.
        :param id: ID de la materia a actualizar.
        """
        materia_existente = MateriaRepository.buscar_por_id(id)
        if not materia_existente:
            return None
        materia_existente.nombre = materia.nombre
        materia_existente.codigo = materia.codigo
        return materia_existente
        
    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        """
        Borra una materia por su ID.
        :param id: ID de la materia a borrar.
        """
        materia = MateriaRepository.buscar_por_id(id)
        if not materia:
            return None
        return materia
    
        