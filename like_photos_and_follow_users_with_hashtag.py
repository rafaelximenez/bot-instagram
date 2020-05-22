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
    for hashtag in setup['hashtags']:
        bot.like_photos_and_follow_users_with_hashtag(hashtag, random.randint(13, 23))  # Altere aqui para a hashtag que você deseja usar.
