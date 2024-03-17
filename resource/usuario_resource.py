from flask_restful import Resource
from requests import request

from form.usuario_shema import UsuarioShema
from service.usuario_service import UsuarioService


class UsuarioResource(Resource):

    def post(self):
        dados = UsuarioShema().load(request.json())
        usuario = UsuarioService.cadastrar_usuario(dados)

    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass
