from enum import Enum
from variaveis.variaveis_enum import TOKEN, LOGIN

class MessageToken(Enum):
    TOKEN_LOGIN_NOVAMENTE = f'Faça {LOGIN} novamente para obter um novo {TOKEN}'
    TOKEN_EXPIRADO = f'O {TOKEN} está expirado.'


class ErroServidorMessage(Enum):
    ERRO_OCORREU_ERRO_INTERNO_SERVIDOR = 'Ocorreu um erro interno no servidor.'
    ERRO_INTERNO_SERVIDOR = 'Erro interno no servidor'