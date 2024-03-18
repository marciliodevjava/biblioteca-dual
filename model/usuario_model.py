from config.banco_de_dados import db


class UsuarioModel(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    genero = db.Column(db.String(10), nullable=False)
    ddi = db.Column(db.Integer(), nullable=False)
    ddd = db.Column(db.Integer(), nullable=False)
    telefone = db.Column(db.Integer(), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __init__(self, nome, email, genero, ddi, ddd, telefone, senha):
        self.nome = nome
        self.email = email
        self.genero = genero
        self.ddi = ddi
        self.ddd = ddd
        self.telefone = telefone
        self.senha = senha

    def json(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'genero': self.genero,
            'ddi': self.ddi,
            'ddd': self.ddd,
            'telefone': self.telefone
        }

    @classmethod
    def salvar_usuario(cls, usuario):
        try:
            usuario = cls.buscar_usuario(usuario['email'])
            if usuario:
                return False
            db.session.add(usuario)
            db.session.commit()
            return usuario
        except BaseException:
            return None

    @classmethod
    def buscar_usuario(cls, email):
        try:
            usuario = db.session.query(cls).filter_by(email=email).first()
            if usuario:
                return usuario
            return None
        except BaseException as e:
            return None
