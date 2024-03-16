from flask_restful import Api

from resource.usuario_resource import UsuarioResource


def config_routes_v0(api: Api):
    api.add_resource(UsuarioResource, '/cadastro', methods=['POST'], endpoint='cadastro_usuario')
    api.add_resource(UsuarioResource, '/cadastro', methods=['GET'], endpoint='buscar_usuario')
    api.add_resource(UsuarioResource, '/cadastro', methods=['PUT'], endpoint='atualizar_usuario')
    api.add_resource(UsuarioResource, '/cadastro', methods=['DELETE'], endpoint='deletar_usuario')

    return api
