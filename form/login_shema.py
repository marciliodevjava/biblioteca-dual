from marshmallow import Schema, fields

from enumerate.message import LoginFormulario


class LoginShema(Schema):
    login = fields.Str(required=True, error_messages={'required': LoginFormulario.O_CAMPO_NOME})
    senha = fields.Str(required=True, error_messages={'required': LoginFormulario.O_CAMPO_SENHA})
