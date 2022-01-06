from instapy import InstaPy
from instapy import smart_run
from os import environ

session = InstaPy(username=environ['INSTAGRAM_USERNAME'], password=environ['INSTAGRAM_PASSWORD'])

def participate_draw(config):
    with smart_run(session):
        session.set_do_like(
            enabled=config["like"]["enable"], 
            percentage=config["like"]["percentage"]
        )
        
        session.set_do_comment(
            enabled=config["comment"]["enable"], 
            percentage=config["comment"]["percentage"]
        )
        
        session.set_comments(["teste!", "Bot!"])
        
        session.set_do_follow(
            enabled=config["follow"]["enable"], 
            percentage=config["follow"]["percentage"]
        )
        
        session.set_user_interact(
            amount=config["user_interact"]["amount"], 
            randomize=config["user_interact"]["randomize"], 
            percentage=config["user_interact"]["percentage"], 
            media=config["user_interact"]["media"]
        )

        session.interact_by_URL(
            urls=config["url_interact"]["urls"], 
            randomize=config["url_interact"]["randomize"], 
            interact=config["url_interact"]["interact"]
        )

config = {
    "like": {"enable": True, "percentage": 100}, 
    "comment": {"enable": True, "percentage": 100},
    "follow": {"enable": False, "percentage": 100},
    "user_interact": {"amount": 6, "randomize": False, "percentage": 100, "media": "Photo"},
    "url_interact": {"urls": ["https://www.instagram.com/p/CXMtqyylLm4/"], "randomize": True, "interact": True},
}

participate_draw(config)