from app.models import Departamento
from app.repositories import DepartamentoRepository

class DepartamentoService:

    @staticmethod
    def crear(departamento):
        """
        Crea un nuevo departamento en la base de datos.
        :param departamento: Objeto Departamento a crear.
        :return: Objeto Departamento creado.
        """
        DepartamentoRepository.crear(departamento)

    @staticmethod
    def buscar_por_id(id: int) -> Departamento:
        """
        Busca un departamento por su ID.
        :param id: ID del departamento a buscar.
        :return: Objeto Departamento encontrado o None si no se encuentra.
        """
        return DepartamentoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Departamento]:
        """
        Busca todos los tipos de documentos en la base de datos.
        :return: Lista de objetos TipoDocumento.
        """
        return DepartamentoRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, departamento: Departamento) -> Departamento:
        """
        Actualiza un departamento existente en la base de datos.
        :param id: ID del departamento a actualizar.
        :param departamento: Objeto Departamento con los nuevos datos.
        :return: Objeto Departamento actualizado.
        """
        departamento_existente = DepartamentoRepository.buscar_por_id(id)
        if not departamento_existente:
            return None
        departamento_existente.nombre = departamento.nombre
        return departamento_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Departamento:
        """
        Borra un departamento por su ID.
        :param id: ID del departamento a borrar.
        :return: Objeto Departamento borrado o None si no se encuentra.
        """
        departamento = DepartamentoRepository.borrar_por_id(id)
        if not departamento:
            return None
        return departamento