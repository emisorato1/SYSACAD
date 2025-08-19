from app import db
from app.models import TipoDedicacion

class TipoDedicacionRepository:

    @staticmethod
    def crear(tipodedicacion):
        db.session.add(tipodedicacion)
        db.session.commit()
    
    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(TipoDedicacion).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        return db.session.query(TipoDedicacion).all()
    
    @staticmethod
    def actualizar(tipodedicacion) -> TipoDedicacion:
        tipodedicacion_existente = db.session.merge(TipoDedicacion)
        if not tipodedicacion_existente:
            # pyrefly: ignore  # bad-return
            return None
        # pyrefly: ignore  # bad-return
        return tipodedicacion_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        tipodedicacion = db.session.query(TipoDedicacion).filter_by(id=id).first()
        if not tipodedicacion:
            return False
        db.session.delete(tipodedicacion)
        db.session.commit()
        return True
