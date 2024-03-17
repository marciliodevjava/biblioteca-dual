from marshmallow import Schema, fields

from enumerate.message import UsuarioFormulario


class UsuarioShema(Schema):
    nome = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_NOME})
    email = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_EMAIL})
    genero = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_GENERO})
    ddi = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_DDI})
    ddd = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_DDD})
    telefone = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_TELEFONE})
    senha = fields.Str(required=True, error_messages={'required': UsuarioFormulario.O_CAMPO_SENHA})
