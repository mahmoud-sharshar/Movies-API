from flask import Flask, request, jsonify, abort
from models import setup_db, Movie, Actor



app = Flask(__name__)
setup_db(app)





if __name__ == '__main__':
  app.run()