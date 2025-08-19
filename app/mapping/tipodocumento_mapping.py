from marshmallow import fields, Schema, post_load, validate
from app.models import TipoDocumento

class TipoDocumentoMapping(Schema):
    id = fields.Integer(dump_only=True)
    # pyrefly: ignore  # bad-argument-type
    dni = fields.Integer(required=True, validate=validate.Range(min=1000000, max=99999999))
    # pyrefly: ignore  # bad-argument-type
    libreta_civica = fields.String(required=True, validate=validate.Length(min=1, max=20))
    # pyrefly: ignore  # bad-argument-type
    libreta_enrolamiento = fields.String(required=True, validate=validate.Length(min=1, max=20))
    # pyrefly: ignore  # bad-argument-type
    pasaporte = fields.String(required=True, validate=validate.Length(min=1, max=20))


    @post_load
    def nueva_tipodocumento(self, data, **kwargs):
        return TipoDocumento(**data)
