import bcrypt


class Senha:
    @classmethod
    def gerador_senha(senha):
        return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    @classmethod
    def check_senha(usuario_senha, senha_banco):
        return bcrypt.checkpw(usuario_senha.encode('utf-8'), senha_banco.encode('utf-8'))
