from marshmallow import fields, Schema, post_load, validate
from app.models import Grupo


class GrupoMapping(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(
        # pyrefly: ignore  # bad-argument-type
        required=True, validate=validate.Length(min=1, max=50))

    @post_load
    def nuevo_grupo(self, data, **kwargs):
        return Grupo(**data)
