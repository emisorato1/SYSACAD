from app import db
from app.models import Plan

class PlanRepository:
    @staticmethod
    def crear(plan):
        db.session.add(plan)
        db.session.commit()
      

    def buscar_por_id(id: int):
        return db.session.query(Plan).filter_by(id=id).first()
    
    def buscar_todos():
        return db.session.query(Plan).all()
    
    def actualizar(plan: Plan) -> Plan:
        plan_existente = db.session.merge(plan)
        if not plan_existente:
            # pyrefly: ignore  # bad-return
            return None
        return plan_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> bool:
        plan = db.session.query(Plan).filter_by(id=id).first()
        if not plan:
            return False
        db.session.delete(plan)
        db.session.commit()
        return True
