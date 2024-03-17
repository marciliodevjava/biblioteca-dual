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

    @classmethod
    def buscar_usuario(cls, id):
        pass

    @classmethod
    def atualizar_usuario(cls, id, usuario):
        pass

    @classmethod
    def deletar_usuario(cls, id):
        pass
