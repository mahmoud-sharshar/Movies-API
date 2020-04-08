from flask import Flask, request, jsonify, abort
from models import setup_db, Movie, Actor, Genre
from datetime import date


app = Flask(__name__)
setup_db(app)

# movies endpoints
@app.route('/movies')
def get_movies():
    movies = Movie.query.all()
    formatted_movies = [movie.format() for movie in movies]
    return jsonify({
      'success':True,
      'movies':formatted_movies
    })

@app.route('/movies/<int:movie_id>')
def get_specific_movie(movie_id):
  return jsonify({
    'success':True,
    'selected_movie': Movie.query.get(movie_id).format()
  })

@app.route('/movies',methods=['POST'])
def add_movie():
  data  = request.get_json()
  try:
    # print(data['description'])
    # print(data['title'])
    # print(data['release_date'])
    # print(data['period'])
    date_parts = data['release_date'].split(':')
    # print(date_parts)
    release_date = date(int(date_parts[0]),int(date_parts[1]),int(date_parts[2]))
    # print(release_date)
    new_movie = Movie(data['title'],release_date,data['period'],data['description'])
  except:
    return abort(400)

  try:
    new_movie.insert()
    return jsonify({
      'success':True
    })
  except:
    abort(500)

@app.route('/movies/<int:movie_id>',methods=['DELETE'])
def delete_movie(movie_id):
  pass

@app.route('/movies/<int:movie_id>',methods=['PATCH'])
def update_movie(movie_id):
  pass

@app.route('/movies/<int:movie_id>/genres',methods=['GET'])
def retreive_movie_genres(movie_id):
  pass

# genres endpoints
# tested
@app.route('/genres',methods=['POST'])
def add_genre():
  data = request.get_json()
  try:
    new_genre = Genre(data['title'])
    if('description' in data):
      new_genre.description = data['description']
  except:
    abort(400)
  
  status = new_genre.insert()
  if(status=='success'):
    return jsonify({
      'success': True
    })
  else:
    abort(500)
# tested
@app.route('/genres',methods=["GET"])
def get_genres():
  genres = Genre.query.all()
  formatted_genres = []
  for genre in genres:
    formatted_genres.append(genre.format())
  
  return jsonify({
    'success':True,
    'genres':formatted_genres
  })

@app.route('/genres/<int:genre_id>/movies',methods=["GET"])
def retrieve_genre_movies(genre_id):
  pass

@app.route('/genres/<int:genre_id>')
def get_specific_genre(genre_id, methods=["GET"]):
  pass

@app.route('/genres/<int:genre_id>',methods=["DELETE"])
def delete_genre(genre_id):
  pass

@app.route('/genres/<int:genre_id>',methods=["PATCH"])
def update_genre(genre_id):
  pass



# Actor endpoints
@app.route('/actors',methods=["POST"])
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

@app.route('/actors',methods=["GET"])
def get_actors():
  actors = Actor.query.all()
  formatted_actors = [actor.format() for actor in actors]
  return jsonify({
    'success': True,
    'actors': formatted_actors
  })

@app.route('/actors/<int:actor_id>',methods=["GET"])
def get_apecific_actor(actor_id):
  actor = Actor.query.get(actor_id)
  if(actor == None):
    abort(404)
  else:
    return jsonify({
      'success': True,
      'actors': actor.format()
    })


@app.route('/actors/<int:actor_id>',methods=["DELETE"])
def delete_actor(actor_id):
  pass

@app.route('/actors/<int:actor_id>',methods=["PATCH"])
def update_actor(actor_id):
  pass

@app.route('/actors/<int:actor_id>/movies',methods=["GET"])
def get_actor_movies(actor_id):
  pass


# Movie_Genre endpoints



# acting Model endpoints



# error handling
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


if __name__ == '__main__':
  app.run()