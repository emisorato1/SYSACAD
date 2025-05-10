from dataclasses import dataclass
from app import db


@dataclass(init=False, repr=True, eq=True)
class Facultad(db.Model):
    __tablename__ = "facultades"
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ############## Atributos de la facultad ##############
    nombre : str = db.Column(db.String(100), nullable=False)
    abreviatura : str = db.Column(db.String(10), nullable=False)
    directorio : str = db.Column(db.String(100), nullable=False)
    sigla : str = db.Column(db.String(10), nullable=False)
    codigoPostal : str = db.Column(db.String(10), nullable=True)
    ciudad : str = db.Column(db.String(50), nullable=False)
    domicilio : str = db.Column(db.String(100), nullable=False)
    telefono : str = db.Column(db.String(20), nullable=False)
    contacto :  str = db.Column(db.String(100), nullable=False)
    email : str = db.Column(db.String(100), nullable=False)