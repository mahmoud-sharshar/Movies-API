import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from models import setup_db, Movie, Actor, Genre, Movie_Genre
from app import app
from auth_app import setup_auth0
from dotenv import load_dotenv


class MovieTestCase(unittest.TestCase):
    """This class represents the Movie test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.client = app.test_client
        self.database_path = os.getenv('DATABASE_URL_TEST')
        setup_db(app, self.database_path,True)
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.authorized_header = {
                "Authorization": "Bearer " + self.access_token
                }
    def tearDown(self):
        """Executed after reach test"""
       

    
    ##############################   Movie Model Enpoints tests   ############################################

    def test_non_valid_token_unauthorized_client(self):
        res = self.client().get('movies',headers={
                "Authorization": "Bearer " + "unauthorized"
                })
        data = res.get_json()
        self.assertEqual(res.status_code,401)
        self.assertFalse(data['success'])
    
    def test_show_all_movies(self):
        '''  test login '''
        res = self.client().get('/movies',headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])

    def test_add_new_movie_with_correct_parameters(self):
        res = self.client().post("/movies",json={
            'title': 'test_movie',
            'description': 'this is for test only',
            'period': '3h44m',
            'release_date': '2020-3-4'
        }, headers= self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_movie = Movie.query.filter(Movie.title=='test_movie').all()
        self.assertIsNotNone(inserted_movie)
        self.assertEqual(len(inserted_movie),1)
        inserted_movie[0].delete()
    
    def test_add_new_movie_with_incorrect_parameters(self):
        res = self.client().post("/movies",json={
            'title': 'test_movie',
            'description': 'this is for test only',
            'release_date': '2020:3:4'
        }, headers= self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,400)
        self.assertFalse(data['success'])
    
    def test_delete_existing_movie(self):
        self.client().post("/movies",json={
            'title': 'test_movie',
            'description': 'this is for test only',
            'period': '3h44m',
            'release_date': '2020-3-4'
        }, headers= self.authorized_header)
        inserted_movie = Movie.query.filter(Movie.title=='test_movie').all()[0]
        res = self.client().delete("/movies/{}".format(inserted_movie.id),headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    
    def test_delete_non_existing_movie(self):
        res = self.client().delete("/movies/2000000",headers= self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,404)
        self.assertFalse(data['success'])
    
    def test_update_non_existing_movie(self):
        res = self.client().patch("/movies/2000000",json={
            'title': "update test",
            'period': '3h23m'
        },headers= self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,404)
        self.assertFalse(data['success'])        

    def test_update_existing_movie_with_correct_parameters(self):
        self.client().post("/movies",json={
            'title': 'test_movie',
            'description': 'this is for test only',
            'period': '3h44m',
            'release_date': '2020-3-4'
        }, headers= self.authorized_header)
        inserted_movie = Movie.query.filter(Movie.title=='test_movie').all()[0]
        res = self.client().patch("/movies/{}".format(inserted_movie.id),json={
            'title': 'test_update',
            'period': '3h33m',
            'release_date': '1343-3-24',
            'description': 'test_update_description'
        },headers=self.authorized_header)
        data = res.get_json()
        updated_movie = Movie.query.filter(Movie.title=='test_update').all()
        self.assertIsNotNone(updated_movie)
        formated_movie = updated_movie[0].format()
        self.assertTrue(data['success'])
        self.assertEqual(res.status_code,200)
        self.assertEqual(updated_movie[0].title,'test_update')
        self.assertEqual(updated_movie[0].period,'3h33m')
        updated_movie[0].delete()
    

    ##############################  Actor Model Enpoints tests #####################################################
    
    def test_add_new_actor_with_correct_parameters(self):
        res = self.client().post("/actors",json={
            'name': "mahmoud sharshar",
            'age': '22',
            'gender': 'male',
            'bio': "nothing!!!!",
            'birthdate': '1998-5-29'
        }, headers = self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_actor = Actor.query.filter(Actor.name=='mahmoud sharshar').all()
        self.assertIsNotNone(inserted_actor)
        inserted_actor[0].delete()

    def test_add_new_actor_with_incorrect_parameters(self):
        res = self.client().post("/actors",json={
            'fullname': "mahmoud sharshar",
            'ae': '22',
            'gende': 'male',
            'biograph': "nothing!!!!",
            'birthdate': '1998-5-29'
        }, headers = self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,400)
        self.assertFalse(data['success'])        

    def test_show_all_actors(self):
        res = self.client().get("/actors",headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
    
    def test_delete_non_existing_actor(self):
        res = self.client().delete("/actors/2000000",headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,404)
        self.assertFalse(data['success'])
    
    def test_add_and_delete_actor_successfully(self):
        res = self.client().post("/actors",json={
            'name': "mahmoud sharshar",
            'age': '22',
            'gender': 'male',
            'bio': "nothing!!!!",
            'birthdate': '1998-5-29'
        }, headers = self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_actor = Actor.query.filter(Actor.name=='mahmoud sharshar').all()
        self.assertIsNotNone(inserted_actor)

        res2 = self.client().delete("/actors/{}".format(inserted_actor[0].id),headers=self.authorized_header)
        data = res2.get_json()
        self.assertEqual(res2.status_code,200)
        self.assertTrue(data['success'])

    def test_update_non_existing_actor(self):
        res = self.client().patch('/actors/4000000',headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,404)
        self.assertFalse(data['success'])
    
    def test_add_and_update_actor_successfully(self):
        res = self.client().post("/actors",json={
            'name': "mahmoud sharshar",
            'age': 22,
            'gender': 'male',
            'bio': "nothing!!!!",
            'birthdate': '1998-5-29'
        }, headers = self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_actor = Actor.query.filter(Actor.name=='mahmoud sharshar').all()
        self.assertIsNotNone(inserted_actor)

        res2 = self.client().patch("/actors/{}".format(inserted_actor[0].id),json={
            "name": 'update_actor',
            'age': 23,
            'gender': 'female',
        },headers=self.authorized_header)
        updated_actor = Actor.query.filter(Actor.name=='update_actor').all()[0]
        data = res2.get_json()
        self.assertEqual(res2.status_code,200)
        self.assertTrue(data['success'])
        self.assertEqual(updated_actor.name,'update_actor')
        self.assertEqual(updated_actor.age,23)
        self.assertEqual(updated_actor.gender,'female')
        inserted_actor[0].delete()

    ################################## Genre Model Endpoints tests #############################################

    def test_add_genre_with_correct_parameters(self):
        res = self.client().post("/genres",json={
            'name': 'test_genre',
            'description': 'test add genre'
        },headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_genre = Genre.query.filter(Genre.name=='test_genre').all()
        self.assertIsNotNone(inserted_genre)
        inserted_genre[0].delete()
    
    def test_add_genre_with_incorrect_parameters(self):
        res = self.client().post("/genres",json={
            'nonname': 'test_genre',
            'descripte': 'test add genre'
        },headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,400)
        self.assertFalse(data['success'])
    
    def test_add_and_delete_genre_successfully(self):
        res = self.client().post("/genres",json={
            'name': 'test_delete_genre',
            'description': 'test delete genre'
        },headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_genre = Genre.query.filter(Genre.name=='test_delete_genre').all()
        self.assertIsNotNone(inserted_genre)
        res_delete = self.client().delete('/genres/{}'.format(inserted_genre[0].id),headers=self.authorized_header)
        data = res_delete.get_json()
        self.assertEqual(res_delete.status_code,200)
        self.assertTrue(data['success'])

    def test_delete_non_existing_genre(self):
        res = self.client().delete("/genres/3000000000",headers=self.authorized_header)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code,404)
    
    def test_add_and_update_genre_successfully(self):
        res = self.client().post("/genres",json={
            'name': 'test_update_genre',
            'description': 'test update genre'
        },headers=self.authorized_header)
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertTrue(data['success'])
        inserted_genre = Genre.query.filter(Genre.name=='test_update_genre').all()
        self.assertIsNotNone(inserted_genre)
        res_update = self.client().patch('/genres/{}'.format(inserted_genre[0].id),json={
            'name':'updated_genre'
        },headers=self.authorized_header)
        data = res_update.get_json()
        self.assertEqual(res_update.status_code,200)
        self.assertTrue(data['success'])
        updated_genre = Genre.query.filter(Genre.name=='updated_genre').all()
        self.assertIsNotNone(updated_genre)
        updated_genre[0].delete()
    
    def test_update_non_existing_genre(self):
        res = self.client().patch("/genres/3000000000",json={
            'name':'not found'
        },headers=self.authorized_header)
        data = res.get_json()
        self.assertFalse(data['success'])
        self.assertEqual(res.status_code,404)


# Make the tests conveniently executable
if __name__ == "__main__":
    load_dotenv()
    setup_auth0()
    unittest.main()