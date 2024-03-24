from enum import Enum

from variaveis.variaveis_enum import TOKEN, LOGIN


class MessageToken(Enum):
    TOKEN_LOGIN_NOVAMENTE = f'Faça {LOGIN} novamente para obter um novo {TOKEN}'
    TOKEN_EXPIRADO = f'O {TOKEN} está expirado.'


class ErroServidorMessage(Enum):
    ERRO_OCORREU_ERRO_INTERNO_SERVIDOR = 'Ocorreu um erro interno no servidor.'
    ERRO_INTERNO_SERVIDOR = 'Erro interno no servidor'


class UsuarioMessage(Enum):
    USUARIO_DELETADO_COM_SUCESSO = 'Usuário deletado com sucesso.'
    USUARIO_NAO_FOI_DELETADO = 'Usuário não foi deletado com sucesso.'
    USUARIO_ATUALIZADO_COM_SUCESSO = 'Usuário atualizado com sucesso.'
    USUARIO_NAO_ENCONTRADO = 'Usuário não encontrado.'
    USUARIO_BUSCADO_COM_SUCESSO = 'Usuário buscado com sucesso.'
    USUARIO_CADASTRO_COM_SUCESSO = 'Usuario cadastrado com sucesso.'
    USUARIO_JA_EXISTE = 'Usuario já existe na base de dados.'


class UsuarioFormulario(Enum):
    O_CAMPO_SENHA = 'O campo senha não foi enviado.'
    O_CAMPO_TELEFONE = 'O campo telefoone não foi enviado.'
    O_CAMPO_DDD = 'O campo ddd não foi enviado.'
    O_CAMPO_DDI = 'O campo ddi não foi enviado.'
    O_CAMPO_GENERO = 'O campo genero não foi enviado.'
    O_CAMPO_EMAIL = 'O campo email não foi enviado.'
    O_CAMPO_NOME = 'O campo nome não foi enviado.'


class LoginFormulario(Enum):
    O_CAMPO_SENHA = 'O campo login não foi enviado.'
    O_CAMPO_NOME = 'O campo senha não foi enviado.'
