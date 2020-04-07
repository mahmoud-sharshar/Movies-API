import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from SQLAlchemy import Column, String, Integer, DateTime, PrimaryKeyConstraint, ForeignKey


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
    categories = db.relationship('Movie_Category',backref='movie',lazy=True,cascade="save-update, merge, delete")
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
        categories = []
        for category in self.categories:
            categories.append(category.category_name)
        return {
            'id':self.id,
            'title':self.title,
            'release_date':self.release_date,
            'period': self.period,
            'description':self.description,
            'video_link':self.video_link,
            'cover_image_link':self.cover_image_link,
            'categories': categories
        }

    def set_categories(self):
        pass

    def add_category(self):
        pass

# Category Model
class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(),unique=True)
    description = db.Column(db.Text)
    movies = db.relationship('Movie_Category',backref='category',lazy=True,cascade="save-update, merge, delete")
    def __init__(self,title:str,description=None):
        self.title = title
        self.description = description
    
    def insert(self)->str:
        return insert_into_db(self)

    def update(self)->str:
        return update_db()
    
    def delete(self)->str:
        return delete_record_from_db(self)

# Movie_Category Model
class Movie_Category(db.Model):
    __tablename__ = 'movies_category'
    movie_id = db.Column(db.Integer,db.ForeignKey('movies.id'),primary_key=True)
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'),primary_key=True)

    def __init__(self,movie_id:int,category:str):
        self.movie_id = movie_id
        self.category_name = category
    
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