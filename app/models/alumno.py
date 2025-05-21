from dataclasses import dataclass
from datetime import date
from app.models.tipodocumento import TipoDocumento
from app import db

@dataclass(init=False, repr=True, eq=True)
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    nombre = db.Column(db.String(50), nullable=False) 
    apellido = db.Column(db.String(50), nullable=False)
    nrodocumento= db.Column(db.String(50), nullable=False)
    tipo_documento_id = db.Column(db.Integer, db.ForeignKey('tipodocumentos.id'), nullable=False)
    tipo_documento = db.relationship('TipoDocumento', backref='alumnos', lazy=True)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(1), nullable=False) 
    nro_legajo = db.Column(db.Integer, nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False) 