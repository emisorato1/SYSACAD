from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class CategoriaCargo(db.Model):
    __tablename__ = 'categoriacargos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nombre: str = db.Column(db.String(30), nullable=False)