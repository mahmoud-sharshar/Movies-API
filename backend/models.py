import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


database_name = "movies"
database_path = "postgres://{}@{}/{}".format('postgres:20211998','localhost:5432', database_name)

db = SQLAlchemy()
migrate = Migrate()
def setup_db(app,database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    # db.create_all()
    migrate.init_app(app, db)
    

def insert_into_db(model:db.Model)->str:
    status = ""
    try:
        db.session.add(model)
        db.session.commit()
        status = "success"
    except:
        status = "failure"
        db.session.rollback()
    finally:
        db.session.close()
        return status

def update_db()->str:
    status = ""
    try:
        db.session.commit()
        status = "success"
    except:
        db.session.rollback()
        status = "failure"
    finally:
        db.session.close()
        return status   

def delete_record_from_db(model:db.Model)->str:
    status = ""
    try:
        db.session.delete(self)
        db.session.commit()
        status = "success"
    except:
        status = "failure"
        db.session.rollback()
    finally:
        db.session.close()
        return status

# Movie Model
class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable = False, unique = True)
    release_date = db.Column(db.DateTime)
    period = db.Column(db.String())
    description = db.Column(db.Text)
    video_link = db.Column(db.String())
    cover_image_link = db.Column(db.String())
    genres = db.relationship('Movie_Genre',backref='movie',lazy=True,cascade="save-update, merge, delete")
    actors = db.relationship('Acting',backref='movie',lazy=True,cascade="save-update, merge, delete")
    def __init__(self,title,release_date,period,description,video_link=None,cover_image_link=None):
        self.title = title
        self.release_date = release_date
        self.period = period
        self.video_link = video_link
        self.description = description
        self.cover_image_link = cover_image_link
    
    def insert(self)-> str:
        return insert_into_db(self)
    
    def update(self)-> str:
       return update_db()
    
    def delete(self)-> str:
        return delete_record_from_db(self)
    
    def format(self):
        movie_genres = []
        for genre in self.genres:
            movie_genres.append(Genre.query.get(genre.genre_id).name)
        return {
            'id':self.id,
            'title':self.title,
            'release_date':self.release_date,
            'period': self.period,
            'description':self.description,
            'video_link':self.video_link,
            'cover_image_link':self.cover_image_link,
            'genres': movie_genres
        }

    def set_categories(self):
        pass

    def add_category(self):
        pass

# Genre Model
class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),unique=True)
    description = db.Column(db.Text)
    movies_genre = db.relationship('Movie_Genre',backref='genre',lazy=True,cascade="save-update, merge, delete")
    def __init__(self,name:str,description=None):
        self.name = name
        self.description = description
    
    def insert(self)->str:
        return insert_into_db(self)

    def update(self)->str:
        return update_db()
    
    def delete(self)->str:
        return delete_record_from_db(self)
    
    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

    def associated_movies(self):
        movies = []
        for movie_genre in self.movies_genre:
            movie = Movie.query.get(movie_genre.movie_id)
            movies.appen(movie.format())
        return {
            'success': True,
            'movies': movies 
        }

    def add_movie_to_genre(self,movie_id:int):
        pass

# Movie_Category Model
class Movie_Genre(db.Model):
    __tablename__ = 'movies_genres'
    movie_id = db.Column(db.Integer,db.ForeignKey('movies.id'),primary_key=True)
    genre_id = db.Column(db.Integer,db.ForeignKey('genres.id'),primary_key=True)

    def __init__(self,movie_id:int,genre_id:int):
        self.movie_id = movie_id
        self.genre_id = genre_id
    
    def insert(self)->str:
        return insert_into_db(self)

    def update(self)->str:
        return update_db()
    
    def delete(self)->str:
        return delete_record_from_db(self)



# Actor Model
class Actor(db.Model):
    __tablename__ = 'actors'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer, nullable= False)
    gender = db.Column(db.String(), nullable=False)
    image_link = db.Column(db.String())
    biography = db.Column(db.String())
    birthdate = db.Column(db.DateTime)
    movies = db.relationship('Acting',backref='actor',lazy=True,cascade="save-update, merge, delete")

    def __init__(self,name:str,age:int,gender,biography,birthdate,image_link=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.image_link = image_link
        self.biography = biography
        self.birthdate = birthdate

    def insert(self)->str:
        return insert_into_db(self)

    def update(self)->str:
        return update_db()
    
    def delete(self)->str:
        return delete_record_from_db(self)

    def format(self):
        movies = []
        for role in self.movies:
            movies.append(Movie.query.get(role.movie_id).format())
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'bio': self.biography,
            'birthdate': self.birthdate,
            'image_link': self.image_link,
            'movies': movies
        }

# roles of actors
# Acting Model is acossiation table to represent many to many relation ship between Actor Model and Movie Model
class Acting(db.Model):
    __tablename__ = "acting"
    movie_id = db.Column(db.Integer,db.ForeignKey('movies.id'),primary_key=True)
    actor_id = db.Column(db.Integer,db.ForeignKey('actors.id'),primary_key=True)
    role_name = db.Column(db.String())

    def __init__(self,movie_id,actor_id,role_name=None):
        self.movie_id = movie_id
        self.actor_id = actor_id
        self.role_name = role_name
    
    def insert(self)->str:
        return insert_into_db(self)

    def update(self)->str:
        return update_db()
    
    def delete(self)->str:
        return delete_record_from_db(self)