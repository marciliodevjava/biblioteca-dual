from enumerate.message import UsuarioMessage
from model.usuario_model import UsuarioModel
from utils.encripty_pasword import Senha
from utils.formatador_dados import FormatadorDados


class UsuarioService:

    @classmethod
    def cadastrar_usuario(cls, usuario):
        nome = FormatadorDados.formatador_nome(usuario['nome'])
        email = FormatadorDados.formatador_email(usuario['email'])
        genero = FormatadorDados.formatador_genero(usuario['genero'])
        ddi = FormatadorDados.formatador_ddi(usuario['ddi'])
        ddd = FormatadorDados.formatador_ddd(usuario['ddd'])
        telefone = FormatadorDados.formatador_telefone(usuario['telefone'])
        senha = Senha.gerador_senha(usuario['senha'])
        usuario = UsuarioModel(nome, email, genero, ddi, ddd, telefone, senha)
        usuario = UsuarioModel.salvar_usuario(usuario)
        if usuario:
            return {
                'message': UsuarioMessage.USUARIO_CADASTRO_COM_SUCESSO.value,
                'usuario': usuario.json()
            }
        return {
            'message': UsuarioMessage.USUARIO_JA_EXISTE.value
        }

    @classmethod
    def buscar_usuario(cls, id):
        usuario = UsuarioModel.buscar_usuario_id(id)
        if usuario:
            return {
                'message': UsuarioMessage.USUARIO_BUSCADO_COM_SUCESSO.value,
                'usuario': usuario.json()
            }
        return None

    @classmethod
    def atualizar_usuario(cls, id, usuario):
        buscar_usuario = UsuarioModel.buscar_usuario_id(id)
        if usuario:
            buscar_usuario = UsuarioModel.atualizar_usuario(buscar_usuario, usuario)
            if buscar_usuario:
                return buscar_usuario.json()
            return None

    @classmethod
    def deletar_usuario(cls, id):
        usuario = UsuarioModel.deletar_usuario(id)
        return usuario
