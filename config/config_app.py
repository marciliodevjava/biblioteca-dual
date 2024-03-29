from flask_restful import Api
from config.banco_de_dados import db
from config.jwt import jwt
from variaveis.variaveis_do_sistema import DATABASE_URI, SQLALCHEMY_DATABASE_URI, HEADER_NAME, HEADER_TYPE, SECRET, \
    TOKEN, TIME_TOKEN, SECRET_KEY, NONE, NM_ID_SESSAO


def config_app(api: Api):
    api.app.config[DATABASE_URI] = SQLALCHEMY_DATABASE_URI
    api.app.config[HEADER_NAME] = NM_ID_SESSAO
    api.app.config[HEADER_TYPE] = NONE
    api.app.config[SECRET] = SECRET_KEY
    api.app.config[TOKEN] = TIME_TOKEN

    db.init_app(api.app)
    jwt.init_app(api.app)
    return api