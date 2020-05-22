#*-* coding: utf-8 *-*
import random
import json
from features import Instagram

if __name__ == "__main__":
    # Dados para autenticação e hashtags
    settings = open('setup.json').read()
    setup = json.loads(settings)

    # Entre com o usuário e senha aqui
    bot = Instagram(setup['username'], setup['password'])  
    bot.login()

    # Ler usuários do arquivo
    users = open('following.txt').read()
    for user in users.split('\n'):
        bot.unfollow_user(user)
    