from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Materia(db.Model):
    __tablename__ = 'materias'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), nullable=False, unique=False)


 