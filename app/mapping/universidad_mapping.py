from marshmallow import fields, Schema, post_load, validate, EXCLUDE
from app.models import Universidad

class UniversidadMapping(Schema):
    class Meta:
        unknown = EXCLUDE  # Ignora campos no definidos al deserializar

    hashid = fields.String(dump_only = True) 
    nombre = fields.String(required = True, validate = validate.Length(min=1, max=100))
    sigla = fields.String(required = True, validate = validate.Length(min=1, max=10))

    @post_load
    def nueva_universidad(self,data,**kwargs):
        return Universidad(**data)