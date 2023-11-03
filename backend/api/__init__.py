from flask import Flask
from .auth.views import  auth_namespace
from .friends.views import friends_namespace
from .chatroom.views import chatroom_namespace
from .messages.views import messages_namespace
# from .movies.views import movie_namespace
from flask_restx import Api
from .config.config import config_dict
from .util import db

from .models.messages import Messages
from .models.friends import Friends
from .models.chatroom import ChatRoom
from .models.users import User
from flask_jwt_extended import JWTManager

from flask_migrate import Migrate
def create_app():
    app=Flask(__name__)
    app.config.from_object(config_dict['dev'])
    
    
    # initialize database
    db.init_app(app)
    jwt=JWTManager(app)

    migrate=Migrate(app, db)
    
    api=Api(app)
    

    # add our api blueprints

    api.add_namespace(auth_namespace)
    api.add_namespace(friends_namespace)
    api.add_namespace(chatroom_namespace)
    api.add_namespace(messages_namespace)


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Messages':Messages,
            'ChatRoom':ChatRoom,
            'Friends':Friends
        }
    return app