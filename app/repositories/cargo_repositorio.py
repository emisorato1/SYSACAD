from app import db 
from app.models import Cargo

class CargoRepository:

    @staticmethod
    def crear(cargo):
        db.session.add(cargo)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Cargo).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(Cargo).all()
    
    
    @staticmethod
    def actualizar(cargo) -> Cargo:
        Cargo_existente = db.session.merge(cargo)
        if not Cargo_existente:
            # pyrefly: ignore  # bad-return
            return None
        return Cargo_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        cargo = db.session.query(Cargo).filter_by(id=id).first()
        if not cargo:
            return False
        db.session.delete(cargo)
        db.session.commit()
        return True
