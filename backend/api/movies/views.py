from flask_restx import Namespace, fields, Resource
from flask import request
from ..models.movies import Movie
from http import HTTPStatus
from flask_jwt_extended import jwt_required

movie_namespace=Namespace("movies", "movies apis")






movie_model = movie_namespace.model('Movie', {
    'movie_id': fields.Integer(readOnly=True, description='The unique identifier of a movie'),
    'title': fields.String(required=True, description='The title of the movie'),
    'description': fields.String(description='Description of the movie'),
    'release_year': fields.Integer(description='Release year of the movie'),
    'genre': fields.String(description='Genre of the movie'),
    'director': fields.String(description='Director of the movie'),
    'rating': fields.Float(description='Rating of the movie'),
    'runtime': fields.Integer(description='Runtime of the movie'),
    'poster': fields.String(description='URL or path to the movie poster')
})

@movie_namespace.route('/')
class MovieList(Resource):
    @movie_namespace.marshal_list_with(movie_model)
    @jwt_required()
    def get(self):
        movies = Movie.query.all()
        return movies, HTTPStatus.OK
    
    @movie_namespace.expect(movie_model)
    @movie_namespace.marshal_with(movie_model, code=201)
    @jwt_required()
    def post(self):
        data = request.get_json()
        movie = Movie(**data)
        movie.save()
        return movie, HTTPStatus.CREATED

@movie_namespace.route('/<int:id>')
class MovieResource(Resource):
    @movie_namespace.marshal_with(movie_model)
    @jwt_required()
    def get(self, id):
        movie = Movie.query.get(id)
        if movie:
            return movie, HTTPStatus.OK
        return {"error":f"Movie, {id}, not found"}, HTTPStatus.NOT_FOUND
