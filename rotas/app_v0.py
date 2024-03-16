from flask_restful import Api

from resource.usuario_resource import UsuarioResource
from variaveis.variaveis_do_sistema import BASE_PATH_HTTP


def config_routes_v0(api: Api):
    api.add_resource(UsuarioResource, f'{BASE_PATH_HTTP}/cadastro', methods=['POST'], endpoint='cadastro_usuario')
    api.add_resource(UsuarioResource, f'{BASE_PATH_HTTP}/cadastro/<int:id>', methods=['GET'], endpoint='buscar_usuario')
    api.add_resource(UsuarioResource, f'{BASE_PATH_HTTP}/cadastro/<int:id>', methods=['PUT'], endpoint='atualizar_usuario')
    api.add_resource(UsuarioResource, f'{BASE_PATH_HTTP}/cadastro/<int:id>', methods=['DELETE'], endpoint='deletar_usuario')

    return api
