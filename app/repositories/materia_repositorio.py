from app import db
from app.models import Materia
 
class MateriaRepository:
    """
    Clase de repositorio para la entidad Materia.  
    """
    @staticmethod
    def crear(materia):
        '''
        Crea una nueva materia en la base de datos.   
        '''
        db.session.add(materia)
        db.session.commit()
        
    @staticmethod
    def buscar_por_id(id: int):
        """
        Busca una materia por su ID.
        """
        return db.session.query(Materia).filter_by(id=id).first()
    
    @staticmethod
    def buscar_todos():
        """
        Busca todas las materias en la base de datos.
        """
        return db.session.query(Materia).all()
    
    @staticmethod
    def actualizar_materia(materia) -> Materia:
        """
        Actualiza una materia existente en la base de datos.
        """
        materia_existente = db.session.merge(materia)
        if not materia_existente:
            return None
        return materia_existente
    
    @staticmethod
    def borrar_por_id(id: int) -> Materia:
        """
        Borra una materia por su ID.
        """
        materia = db.session.query(Materia).filter_by(id=id).first()
        if not materia:
            return None
        db.session.delete(materia)
        db.session.commit()
        return materia
