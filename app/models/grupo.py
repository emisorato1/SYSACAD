from dataclasses import dataclass
from app import db

@dataclass(init=False, repr=True, eq=True)
class Grupo(db.Model):
    __tablename__ = 'grupos'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(20),nullable = False)