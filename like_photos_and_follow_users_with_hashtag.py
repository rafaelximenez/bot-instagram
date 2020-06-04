#*-* coding: utf-8 *-*
import random
import json
from features import Instagram

if __name__ == "__main__":
    # Dados para autenticação e hashtags
    settings = open('setup.json').read()
    setup = json.loads(settings)

    i = 0
    # Entre com o usuário e senha aqui
    for username in setup['username']:
        bot = Instagram(setup['username'][i], setup['password'][i])  
        bot.login()
        for hashtag in setup['hashtags'][i]:
            bot.like_photos_and_follow_users_with_hashtag(hashtag, random.randint(10, 18))  # Altere aqui para a hashtag que você deseja usar.
        bot.quit_driver()
        i += 1