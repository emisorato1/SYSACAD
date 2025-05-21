from app.models import Area
from app.repositories.area_repositorio import AreaRepository

 
 
class AreaService:
    """
    Clase de servicio para la entidad Area.
    """
    @staticmethod
    def crear(area: Area):
        AreaRepository.crear(area)

    
    @staticmethod
    def buscar_por_id(id: int) -> Area:
        return AreaRepository.buscar_por_id(id)
    
    @staticmethod
    def buscar_todos() -> list[Area]:
        return AreaRepository.buscar_todos()
    
    @staticmethod
    def actualizar(id: int, area: Area) -> Area:
        area_existente = AreaRepository.buscar_por_id(id)
        if not area_existente:
            return None
        area_existente.nombre = area.nombre
        return area_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Area:
        area = AreaRepository.borrar_por_id(id)
        if not area:
            return None
        return area
    