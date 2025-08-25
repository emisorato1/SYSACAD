from marshmallow import fields, Schema, post_load, validate
from app.models import TipoDedicacion

class TipoDedicacionMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=validate.Length(min=1, max=100))
    observacion = fields.String(required=True, validate=validate.Length(min=1, max=200))

    @post_load
    def nueva_tipodedicacion(self, data, **kwargs):
        return TipoDedicacion(**data)
