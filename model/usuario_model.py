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

    @classmethod
    def atualizar_usuario(cls, buscar_usuario, usuario):
        try:
            buscar_usuario.nome = usuario['nome']
            buscar_usuario.email = usuario['email']
            buscar_usuario.genero = usuario['genero']
            buscar_usuario.ddi = usuario['ddi']
            buscar_usuario.ddd = usuario['ddd']
            buscar_usuario.telefone = usuario['telefone']
            db.session.commit()
            return buscar_usuario
        except BaseException as b:
            return None

    @classmethod
    def deletar_usuario(cls):
        try:
            usuario = cls.buscar_usuario_id(id)
            if usuario:
                db.session.delete(usuario)
                db.session.commit()
                return True
            return False
        except BaseException as b:
            return False

    @classmethod
    def buscar_usuario_id(cls, id):
        try:
            usuario = db.session.query(cls).filter_by(id=id).first()
            if usuario:
                return usuario
            return None
        except BaseException as e:
            return None
