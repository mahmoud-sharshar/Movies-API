#  Movie API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

it's recommended to work within a virtual environment whenever using Python for projects. This keeps the dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once the  virtual environment is setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages  within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM used to handle postgresql database. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 
- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup
- With Postgres running, create a new database for the application.
- Replace the value of `DATABASE_URL` variable in [`.env`](./.env) file with the database url of newly created database.

## Running the server Locally

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python app.py
```
or 
```bash
flask run
```
Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

## API REFERENCE

- Description of all endpoints and how to use them can be found in [`API_REFERENCE`](./API_reference.md).

## Testing
To run test cases in [`test_app.py`](./test_app.py), follow the following steps:
- With Postgres running, create a new database for testing.
- Replace the value of `DATABASE_URL_TEST` variable in [`.env`](./.env) file with the database url of newly created database.
- Sign in to the hosted application with the following credintials:
    - Email: `company.executive.producer@movie.com`
    - Password: `FSNd2020` 
- Save access_token after login and Replace the value of `ACCESS_TOKEN` variable in [`.env`](./.env) file with the saved access_token.
- From within the `backend` directory first ensure you are working using your created virtual environment.

- execute:

    ```bash
    python test_app.py
    ```
