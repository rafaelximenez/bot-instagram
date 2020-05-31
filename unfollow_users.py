#*-* coding: utf-8 *-*
import random
import json
from features import Instagram

if __name__ == "__main__":
    # Dados para autenticação e hashtags
    settings = open('setup.json').read()
    setup = json.loads(settings)

    i = 0
    for username in setup['username']:
        # Entre com o usuário e senha aqui
        bot = Instagram(setup['username'][i], setup['password'][i])  
        bot.login()

        # Ler usuários do arquivo
        users = open(str(setup['username'][i]) + '.txt').read()
        for user in users.split('\n'):
            bot.unfollow_user(user)
        i += 1
    