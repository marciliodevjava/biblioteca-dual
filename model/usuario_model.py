from config.banco_de_dados import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.Collumn(10), nullable=False)
    ddi = db.Column(db.Integer(4), nullable=False)
    ddd = db.Column(db.Integer(4), nullable=False)
    telefone = db.Column(db.Integer(9), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, genero, ddi, ddd, telefone, senha):
        self.nome = nome
        self.email = email
        self.genero = genero
        self.ddi = ddi
        self.ddd = ddd
        self.telefone = telefone
        self.senha = senha
