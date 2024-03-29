import datetime

BASE_PATH_HTTP = '/biblioteca'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}:{port}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario='root',
        senha='1234567890',
        servidor='127.0.0.1',
        port='3306',
        database='biblioteca'
    )

SECRET = 'JWT_SECRET_KEY'
SECRET_KEY = '123'
DATABASE_URI = 'SQLALCHEMY_DATABASE_URI'
HEADER_NAME = 'JWT_HEADER_NAME'
HEADER_TYPE = 'JWT_HEADER_TYPE'
NM_ID_SESSAO = "nmIdSessao"
TOKEN = 'JWT_ACCESS_TOKEN_EXPIRES'
TIME_TOKEN = datetime.timedelta(minutes=60)
NONE = None
