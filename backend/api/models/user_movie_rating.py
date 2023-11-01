from ..util import db
class UserMovieRating(db.Model):
    __tablename__ = 'user_movie_rating'

    rating_id = db.Column(db.Integer(), primary_key=True)
    # user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))
    # movie_id = db.Column(db.Integer(), db.ForeignKey('movie.movie_id'))
    rating = db.Column(db.Integer())
    created_at = db.Column(db.String())  # You can use a DateTime field

    # # Establish relationships with User and Movie
    # user = db.relationship('User', backref='user_movie_ratings', lazy=True)
    # movie = db.relationship('Movie', backref='movie_ratings', lazy=True)
