from flask import Flask
from .auth.views import  auth_namespace
from .hub.views import hub_namespace
from .cineflicksroom.views import chatroom_namespace
from .messages.views import messages_namespace
# from .movies.views import movie_namespace
from flask_restx import Api
from .config.config import config_dict
from .util import db

from .models.messages import Messages
from .models.hub import Hub
from .models.chatroom import ChatRoom
from .models.users import User
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from flask_migrate import Migrate
def create_app():
    app=Flask(__name__)
    app.config.from_object(config_dict['dev'])
    CORS(app)

    
    
    # initialize database
    db.init_app(app)
    jwt=JWTManager(app)

    migrate=Migrate(app, db)
    
    api=Api(app)
    

    # add our api blueprints

    api.add_namespace(auth_namespace)
    api.add_namespace(hub_namespace)
    api.add_namespace(chatroom_namespace)
    api.add_namespace(messages_namespace)


    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Messages':Messages,
            'ChatRoom':ChatRoom,
            'hub':Hub
        }
    return app