# Full Stack Movie API Final Project

## Movie API

Movies companies need to manage their movies and actors to simplify the process of creating and managing movies.
This API allows an Executive Producer within the movie company to create movies, manage and assigne actors to those movies and manage and assign movies to different genres. 

## About the Stack

### Backend

The `./backend` directory contains a completed Flask and SQLAlchemy server that can manage and run API. 

### Frontend

- frontend of the api isn't implemeted yet.


## Usage of API
- The API is hosted at `https://fsnd-movie-api.herokuapp.com` and if you want to run it locally, follow the instructions in `./backend` README

- follow the following steps to try the API:
    - login into the system `https://fsnd-movie-api.herokuapp.com/` using one of the following emails:
        - For Executive Producer Role
            - Email: `company.executive.producer@movie.com`
            - Password: `FSNd2020` 
        - For Casting Assistant Role
            - Email: `company.casting.assistant@movie.com`
            - Password: `FSNd2020`
        - For Casting Director Role
            - Email: `company.casting.director@movie.com`
            - Password: `FSNd2020`
    
    -  Save access_token that appears in the returned url as following:
        - https://fsnd-movie-api.herokuapp.com/login-results#access_token=`{save this}`&expires_in=7200&token_type=Bearer
    
    - use curl or postman to send request to a specific endpoint with access_token included in the header of the request.

    - use API_REFERENCE for the guide to use endpoints.