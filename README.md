# Full Stack Movie API Final Project

## Movie API

Movies companies need to manage their movies and actors to simplify the process of creating and managing movies.
This API allows an Executive Producer within the movie company to create movies, manage and assign actors to those movies and manage and assign movies to different genres.  

## About the Stack

### Backend

- The [`./backend`](./backend) directory contains a completed Flask and SQLAlchemy server that can manage and run API. 

### Frontend

- Frontend of the api isn't implemeted yet.


## Usage of API
- The API is hosted at https://fsnd-movie-api.herokuapp.com and if you want to run it locally, follow the instructions in [`./backend`](./backend/README.md).

- Follow the following steps to try the API:
    - Login into the system `https://fsnd-movie-api.herokuapp.com/` using one of the following emails:
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
        - `https://fsnd-movie-api.herokuapp.com/login-results#access_token={given_access_token}&expires_in=7200&token_type=Bearer`
    
    - Use [`Curl`](https://curl.haxx.se/) or [`Postman`](https://www.postman.com/) to send request to a specific endpoint with access_token included in the header of the request.

    - Use [`API_REFERENCE`](./backend/API_reference.md) for the guide to use endpoints.
