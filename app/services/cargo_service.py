from app.models import Cargo
from app.repositories import CargoRepository
from app.repositories import CategoriaCargoRepository, TipoDedicacionRepository


class CargoService:
     
    @staticmethod
    def crear(cargo):
        CargoRepository.crear(cargo)

    @staticmethod
    def borrar_por_id(id: int) -> bool:
        from app.repositories.cargo_repositorio import CargoRepository
        return CargoRepository.borrar_por_id(id)


    @staticmethod
    def buscar_por_id(id: int) -> Cargo:        
        return CargoRepository.buscar_por_id(id)

    @staticmethod
    def buscar_todos() -> list[Cargo]:
        return CargoRepository.buscar_todos()
    

    @staticmethod
    def actualizar(id: int, cargo: Cargo) -> Cargo:
        cargo_existente = CargoRepository.buscar_por_id(id)
        if not cargo_existente:
            return None
        cargo_existente.nombre = cargo.nombre
        cargo_existente.puntos = cargo.puntos
        # Buscar y asignar los objetos relacionados
        cargo_existente.categoria_cargo = CategoriaCargoRepository.buscar_por_id(cargo.categoria_cargo_id)
        cargo_existente.tipo_dedicacion = TipoDedicacionRepository.buscar_por_id(cargo.tipo_dedicacion_id)
        return CargoRepository.actualizar(cargo_existente)


