from flask_restful import Resource
from requests import request

from enumerate.message import UsuarioMessage
from form.usuario_shema import UsuarioShema
from service.usuario_service import UsuarioService


class UsuarioResource(Resource):

    def post(self):
        dados = UsuarioShema().load(request.json())
        usuario = UsuarioService.cadastrar_usuario(dados)
        if usuario.get('messsage').__eq__(UsuarioMessage.USUARIO_JA_EXISTE.value):
            return usuario, 200
        return usuario, 201

    def get(self, id):
        usuario = UsuarioService.buscar_usuario(id)
        if not usuario:
            return {
                'message': UsuarioMessage.USUARIO_NAO_ENCONTRADO.value
            }, 404
        return usuario, 200

    def put(self, id):
        pass

    def delete(self, id):
        pass
