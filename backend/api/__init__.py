from flask import Flask
from .auth.views import  auth_namespace
from .movies.views import movie_namespace
from flask_restx import Api
from .config.config import config_dict
from .util import db

from .models.movies import Movie
from .models.comments import Comment
from .models.user_movie_rating import UserMovieRating
from .models.usergenrepreference import UserGenrePreference
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
    api.add_namespace(movie_namespace)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'User':User,
            'Movie':Movie,
            'UserMovieRating':UserMovieRating,
            'UserGenrePreference':UserGenrePreference
        }
    return app