from marshmallow import fields, Schema, post_load, validate
from app.models import Grado

class GradoMapping(Schema):
    id = fields.Integer(dump_only=True)
    # pyrefly: ignore  # bad-argument-type
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=50))
    # pyrefly: ignore  # bad-argument-type
    descripcion = fields.String(required=True, validate=validate.Length(min=1, max=200))
    
    @post_load
    def nuevo_grado(self, data, **kwargs):
        return Grado(**data)
