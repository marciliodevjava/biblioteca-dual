class UsuarioService:

    @classmethod
    def cadastrar_usuario(cls, usuario):
        nome = usuario['nome']
        email = usuario['email']
        genero = usuario['genero']
        ddi = usuario['ddi']
        ddd = usuario['ddd']
        telefone = usuario['telefone']
        senha = usuario['senha']

    @classmethod
    def buscar_usuario(cls, id):
        pass

    @classmethod
    def atualizar_usuario(cls, id, usuario):
        pass

    @classmethod
    def deletar_usuario(cls, id):
        pass
