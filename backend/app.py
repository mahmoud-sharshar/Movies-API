import os
from flask import Flask, request, jsonify, abort, session, Response, redirect
from models import setup_db, Movie, Actor, Genre, Movie_Genre
from datetime import date
from auth_app import AuthError, requires_auth, setup_auth0, API_AUDIENCE
from flask import session
import requests
AUTH0_CALLBACK_URL= 'http://127.0.0.1:5000/login-results'



app = Flask(__name__)
setup_db(app)


app.config.update(SECRET_KEY=os.urandom(24))


# auth0 = setup_auth0(app)

@app.route('/')
@app.route('/login')
def login():
  return redirect("https://fsnd-shar-2.auth0.com/authorize?audience=movies&response_type=token&client_id=4yHgzJtE95g2335MHeRP5xESVp3a51Xc&redirect_uri=http://127.0.0.1:5000/login-results")
 


@app.route('/login-results')
def login_result():
  return jsonify({
      "success":True
      })

################################################################################################
#####################################  Movie Model Endpoints  ##################################

# Endpoint to retreive all movies in the system
@app.route('/movies',methods=["GET"])
@requires_auth('get:movies')                
def get_movies():
    movies = Movie.query.all()
    formatted_movies = [movie.format() for movie in movies]
    return jsonify({
      'success':True,
      'movies':formatted_movies
    })

# Endpoint to retreive a specific movie with it's id
@app.route('/movies/<int:movie_id>',methods=["GET"])
@requires_auth('get:movies')
def get_specific_movie(movie_id):
  movie =  get_movie_if_exist(movie_id)
  return jsonify({
    'success':True,
    'selected_movie': movie.format()
  })

# Endpoint to add a new movie
@app.route('/movies',methods=['POST'])
@requires_auth('post:movies')
def add_movie():
  data  = request.get_json()
  try:
    date_parts = data['release_date'].split('-')
    release_date = date(int(date_parts[0]),int(date_parts[1]),int(date_parts[2]))
    new_movie = Movie(data['title'],release_date,data['period'],data['description'])
    if('video_link' in data):
      new_movie.video_link = video_link
    if('cover_image_link' in data):
      new_movie.cover_image_link = data['cover_image_link']
  except:
    abort(400)


  success = new_movie.insert()
  if(success):
    inserted_movie = Movie.query.filter(Movie.title == data['title']).all()[0].format()
    return jsonify({
      'success':True,
      'new_movie': inserted_movie
    })
  else:
    abort(500)

# Enpoint to delete a movie with it's id
@app.route('/movies/<int:movie_id>',methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movie(movie_id):
  movie = get_movie_if_exist(movie_id)
  deleted_movie = movie.format()
  success = movie.delete()
  if(success):
    return jsonify({
        'success': True,
        "deleted_movie": deleted_movie
    })
  else:
    abort(500)

# Endpoint to update movie, given it's id
@app.route('/movies/<int:movie_id>',methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(movie_id):
  movie = get_movie_if_exist(movie_id)
  data = request.get_json()
  if('title' in data):
    movie.title = data['title']
  if('period' in data):
    movie.period = data['period']
  if('description' in data):
    movie.description = data['description']
  if('release_date' in data):
    try:
      date_parts = data['release_date'].split('-')
      release_date = date(int(date_parts[0]),int(date_parts[1]),int(date_parts[2]))
      movie.release_date = release_date
    except:
      abort(400)
  success = movie.update()
  updated_movie = Movie.query.get(movie_id)
  if(success):
    return jsonify({
    'success':True,
    'updated movie': updated_movie.format()
    })
  else:
    abort(500)

# Endpoint to get genres of movie with it's id
@app.route('/movies/<int:movie_id>/genres',methods=['GET'])
@requires_auth('get:movie-genres')
def get_movie_genres(movie_id):
  movie = get_movie_if_exist(movie_id)
  genres = movie.get_genres()
  formated_genres = [genre.format() for genre in genres]
  return jsonify({
    'success': True,
    'genres' : formated_genres,
    'movie': movie.format()
  }) 

# Endpoint to get actors of movie with it's id
@app.route('/movies/<int:movie_id>/actors',methods=['GET'])
@requires_auth('get:movie-actors')
def get_movie_actors(movie_id):
  movie = get_movie_if_exist(movie_id)
  actors = movie.get_actors()
  formatted_actors = [actor.format() for actor in actors]
  return jsonify({
    'success': True,
    'actors': formatted_actors
  })

# Endpoint to accosiate a movie to specific genre
@app.route('/movies/<int:movie_id>/genres',methods=["POST"])
@requires_auth('post:genre-to-movie')
def associate_genre_to_movie(movie_id):
  movie = get_movie_if_exist(movie_id)
  data = request.get_json()
  try:
    genre = Genre.query.get(data['genre_id'])
    if(genre is None):
      abort(404)
    success = movie.add_genre(data['genre_id'])
    if(success):
      return jsonify({
        'success':True
      })
    else:
      return jsonify({
        'success': True,
        'message': 'genre is alreay associated with this movie'
      })
  except:
    abort(400)

# Endpoint to add actor to movie
@app.route('/movies/<int:movie_id>/actors',methods=['POST'])
@requires_auth('post:actor-to-movie')
def add_actor_to_movie(movie_id):
  movie = get_movie_if_exist(movie_id)
  data = request.get_json()
  try:
    actor = Actor.query.get(data['actor_id'])
    if(actor is None):
      abort(404)
    success = movie.add_actor(int(data['actor_id']))
    # print(success)
    if(success):
      return jsonify({
        'success': success
      })
    else:
      return jsonify({
        'success': True,
        'message': 'actor is alreay exist in this movie'
      })
  except:
    abort(400)


#######################################################################################################
######################################### Genre Model Endpoint  #######################################

# Endpoint to add a new genre to the system
@app.route('/genres',methods=['POST'])
@requires_auth('post:genres')
def add_genre():
  data = request.get_json()
  try:
    new_genre = Genre(data['name'])
    if('description' in data):
      new_genre.description = data['description']
  except:
    abort(400)
    
  success = new_genre.insert()
  if(success):
    inserted_genre = Genre.query.filter_by(name= data['name']).all()[0].format()
    return jsonify({
      'success': True,
      'new_genre': inserted_genre
    })
  else:
    abort(500)

# Endpoint to retreive all existance genres
@app.route('/genres',methods=["GET"])
@requires_auth('get:genres')
def get_genres():
  genres = Genre.query.all()
  formatted_genres = []
  for genre in genres:
    formatted_genres.append(genre.format())
  
  return jsonify({
    'success':True,
    'genres':formatted_genres
  })

# Endpoint to retreive all accosiated movies to a given genre
@app.route('/genres/<int:genre_id>/movies',methods=["GET"])
@requires_auth('get:genre-movies')
def retrieve_genre_movies(genre_id):
  genre = get_genre_if_exist(genre_id)
  movies = genre.associated_movies()
  return jsonify({
    'success': True,
    'movies': movies
  })
 
# Endpoint to retreive a genre, given it's id
@app.route('/genres/<int:genre_id>')
@requires_auth('get:genres')
def get_specific_genre(genre_id, methods=["GET"]):
  genre = get_genre_if_exist(genre_id)
  return jsonify({
    'success': True,
    'selected_genre': genre.format()
  })

# Endpoint to delete a genre with it's id
@app.route('/genres/<int:genre_id>',methods=["DELETE"])
@requires_auth('delete:genres')
def delete_genre(genre_id):
  genre = get_genre_if_exist(genre_id)
  deleted_genre = genre.format()
  success = genre.delete()
  if(success):
    return jsonify({
      'success': True,
      'deleted_genre': deleted_genre
    })
  else:
    abort(500)

# Endpoint to update a genre
@app.route('/genres/<int:genre_id>',methods=["PATCH"])
@requires_auth('patch:genres')
def update_genre(genre_id):
  genre = get_genre_if_exist(genre_id)
  data = request.get_json()
  if('name' in data):
    genre.name = data['name']
  if('description' in data):
    genre.description = data['description']
  success = genre.update()
  if(success):
    updated_genre = get_genre_if_exist(genre_id)
    return jsonify({
      'success': True,
      'updated_genre': updated_genre.format()
    })
  else:
    abort(500)


######################################################################################################################
#######################################  Actor Model Endpoints  ######################################################

# Endpoint to add new actor to the system
@app.route('/actors',methods=["POST"])
@requires_auth('post:actors')
def add_actor():
  data = request.get_json()
  try:
    birthdate_parts = data['birthdate'].split("-")
    birthdate = date(int(birthdate_parts[0]),int(birthdate_parts[1]),int(birthdate_parts[2]))
    new_actor = Actor(data['name'],data['age'],data['gender'],data['bio'],birthdate)
  except:
    abort(400)

  try:
    new_actor.insert()
    return jsonify({
      'success': True
    })
  except:
    abort(500)

# Endpoint to get all actors in the system
@app.route('/actors',methods=["GET"])
@requires_auth('get:actors')
def get_actors():
  actors = Actor.query.all()
  formatted_actors = [actor.format() for actor in actors]
  return jsonify({
    'success': True,
    'actors': formatted_actors
  })

# Endpoint to get an actor
@app.route('/actors/<int:actor_id>',methods=["GET"])
@requires_auth('get:actors')
def get_apecific_actor(actor_id):
  actor = get_actor_if_exist(actor_id)
  return jsonify({
    'success': True,
    'actors': actor.format()
  })

# Endpoint to delete actor
@app.route('/actors/<int:actor_id>',methods=["DELETE"])
@requires_auth('delete:actors')
def delete_actor(actor_id):
  actor = get_actor_if_exist(actor_id)
  deleted_actor = actor.format()
  success = actor.delete()
  if(success):
    return jsonify({
      'success': True,
      'deleted_actor': deleted_actor
    })
  else:
    abort(500)

# Endpoint to update information of a given actor
@app.route('/actors/<int:actor_id>',methods=["PATCH"])
@requires_auth('patch:actors')
def update_actor(actor_id):
  actor = get_actor_if_exist(actor_id)
  data = request.get_json()
  if('name' in data):
    actor.name = data['name']
  if('bio' in data):
    actor.name = data['bio']
  if('birthdate' in data):
    try:
      birthdate_parts = data['birthdate'].split("-")
      birthdate = date(int(birthdate_parts[0]),int(birthdate_parts[1]),int(birthdate_parts[2]))
      actor.birthdate = birthdate
    except:
      abort(400)
  if('age' in data):
    actor.age = data['age']
  if('gender' in data):
    actor.gender = data['gender']
  
  success = actor.update()
  updated_actor = get_actor_if_exist(actor_id)
  if(success):
    return jsonify({
      'success': True,
      'updated_actor': updated_actor.format()
    })

@app.route('/actors/<int:actor_id>/movies',methods=["GET"])
@requires_auth('get:actor-movies')
def get_actor_movies(actor_id):
  actor = get_actor_if_exist(actor_id)
  movies = actor.get_movies()
  return jsonify({
    'success': True,
    'movies': movies
  })

###############################################################################################################
####################################### Helper Functions ######################################################

def get_movie_if_exist(movie_id):
  movie = Movie.query.get(movie_id)
  if(movie is None):
    abort(404)
  return movie

def get_genre_if_exist(genre_id):
  genre = Genre.query.get(genre_id)
  if(genre is None):
    abort(404)
  return genre

def get_actor_if_exist(actor_id):
  actor = Actor.query.get(actor_id)
  if(actor == None):
    abort(404)
  return actor

################################################################################################################
############################################### Error Handling #################################################
@app.errorhandler(404)
def not_found_404(error):
  return jsonify({
      'success':False,
      'message':"Resource Not Found",
      'error':404
    }),404

@app.errorhandler(500)
def server_error_500(error):
  return jsonify({
      'success':False,
      'message':"server error",
      'error':500
    }),500

@app.errorhandler(405)
def method_not_allowed(error):
  return jsonify({
      "success":False,
      "message": "Method Not Alowed",
      "error": 405
    }),405

@app.errorhandler(400)
def  bad_request(error):
  return jsonify({
      "success":False,
      "message": "Bad request",
      "error": 400
    }),400

@app.errorhandler(422)
def unprocessable_entity(error):
  return jsonify({
      "success":False,
      "message": "unprocessable entity",
      "error": 422
    }),422

@app.errorhandler(AuthError)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 401,
                    "message": "unAuthoraized"
                    }), 401
            

#################################################################################################################
########################################### Main ###############################################################
if __name__ == '__main__':
  app.run()