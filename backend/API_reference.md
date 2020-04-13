# API Reference
## introduction

This API is designed to manage movies company that is responsible for creating movies and managing and assigning actors to those movies.

##  Getting Started
#### Base URL 
 The backend app is hosted at  `??????????????????`. 
#### Authentication 
- This API allows access to three roles to a specific enpoints based on permissions assigned to them.
- in the request, it must be login to the system before the request and put jwt access token to authorization header in the request to gain access to the system.
- Roles
	- Casting Assistant
	    - Can view actors, movies and genres
    -Casting Director
        - All permissions a Casting Assistant has and…
        - Add or delete an actor from the database
        - Modify actors, movies or genres
    - Executive Producer
        - All permissions a Casting Director has and…
        - Add or delete a movie from the database.
        - Add or delete a genre from the database.


##  Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": `error_status_code`,
    "message": `error_message`
}
```
The API will return five error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 500: Server error
- 405: Method Not Alowed
- 422: Not Processable
- 401: unauthorized

sample error response:
```
{
    "success": False, 
    "error": 404,
    "message": Resource Not Found
}
```

## Endpoints 
#### GET `\`
- General
    - login to the system
- sample
    - Base url:  `curl http://????/` 
	- localhost: `curl http://127.0.0.1:5000/`

#### GET `\login`
- General
    - login to the system
- sample
    - Base url:  `curl http://????/login` 
	- localhost: `curl http://127.0.0.1:5000/login`

### Movie Endpoints

#### GET `/movies`
- General 
	- Fetches all movies in the system.
	- Request Arguments: None
	- Returns: success value and a list of movies objects formatted in a readable way.
	- Authorization: all roles can access this endpoint and access token must be specified in the header ot the request. 
- Sample: 
	- Base url:  `curl http://????/movies -X GET -H "Authorization:Barear {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies -X GET -H "Authorization:Barear {access_token}`
```
{
    "movies": [
        {
            "cover_image_link": null,
            "description": "One night per year, the government sanctions a 12-hour period in which citizens can commit any crime they wish -- including murder -- without fear of punishment or imprisonment. Leo, a sergeant who lost his son, plans a vigilante mission of revenge during the mayhem. However, instead of a death-dealing avenger, he becomes the unexpected protector of four innocent strangers who desperately need his help if they are to survive the night.",
            "genres": [
                "Action",
                "Comedy",
                "Horror",
                "Adventure"
            ],
            "id": 1,
            "period": "1h 44m",
            "release_date": "Fri, 18 Jul 2014 00:00:00 GMT",
            "title": "The Purge: Anarchy",
            "video_link": null
        },
        {
            "cover_image_link": null,
            "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
            "genres": [],
            "id": 2,
            "period": "2h 33m",
            "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
            "title": "The Final Scream",
            "video_link": null
        },
        {
            "cover_image_link": null,
            "description": "A Foreign Service Officer in London tries to prevent a terrorist attack set to hit New York, but is forced to go on the run when she is framed for crimes she did not commit.",
            "genres": [],
            "id": 3,
            "period": "2h 33m",
            "release_date": "Sun, 18 Jul 2021 00:00:00 GMT",
            "title": "Survivor",
            "video_link": null
        },
        {
            "cover_image_link": null,
            "description": "this is for demo only",
            "genres": [],
            "id": 5,
            "period": "4h23m",
            "release_date": "Thu, 16 May 1963 00:00:00 GMT",
            "title": "updated dummy movie 1",
            "video_link": null
        }
    ],
    "success": true
}
```

#### GET `/movies/<int:movie_id>`
- Genrel 
	- Fetches specific movie with its id.
	- Request Arguments: None
	- Returns: success value and a selected movie object in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/movies/1 -X GET -H "Authorization:Barear {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies/1 -X GET -H "Authorization:Barear {access_token}`
```
{
  "selected_movie": {
    "cover_image_link": null,
    "description": "One night per year, the government sanctions a 12-hour period in which citizens can commit any crime they wish -- including murder -- without fear of punishment or imprisonment. Leo, a sergeant who lost his son, plans a vigilante mission of revenge during the mayhem. However, instead of a death-dealing avenger, he becomes the unexpected protector of four innocent strangers who desperately need his help if they are to survive the night.",
    "genres": [
      "Action",
      "Comedy",
      "Horror",
      "Adventure"
    ],
    "id": 1,
    "period": "1h 44m",
    "release_date": "Fri, 18 Jul 2014 00:00:00 GMT",
    "title": "The Purge: Anarchy",
    "video_link": null
  },
  "success": true
}
```

#### GET `/movies/<int:movie_id>/genres`
- Genrel 
	- Fetches all genres associated with a specific movie with its id.
	- Request Arguments: None
	- Returns: success value, selected movie information and all genres objects of this movie in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/movies/1/genres -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies/1/genres -X GET -H "Authorization:Bearer {access_token}" `
```
{
  "genres": [
    {
      "description": "This major genre type includes films that have tremendous impact, continuous high energy, lots of physical stunts and activity, possibly extended chase scenes, races, rescues, battles, martial arts, mountains and mountaineering, destructive disasters (floods, explosions, natural disasters, fires, etc.), fights, escapes, non-stop motion, spectacular rhythm and pacing, and adventurous heroes - all designed for pure audience escapism with the action sequences at the core of the film.",
      "id": 1,
      "name": "Action"
    },
    {
      "description": " Comedies are light-hearted dramas, crafted to amuse, entertain, and provoke enjoyment. The comedy genre humorously exaggerates the situation, the language, action, and characters. Comedies observe the deficiencies, foibles, and frustrations of life, providing merriment and a momentary escape from day-to-day life. They usually have happy endings, although the humor may have a serious or pessimistic side.",
      "id": 2,
      "name": "Comedy"
    },
    {
      "description": "Films are unsettling films designed to frighten and panic, cause dread and alarm, and to invoke our hidden worst fears, often in a terrifying, shocking finale, while captivating and entertaining us at the same time in a cathartic experience. Horror films effectively center on the dark side of life, the forbidden, and strange and alarming events. They deal with our most primal nature and its fears: our nightmares, our vulnerability, our alienation, our revulsions, our terror of the unknown, our fear of death and dismemberment, loss of identity, or fear of sexuality.",
      "id": 3,
      "name": "Horror"
    },
    {
      "description": "Films are exciting stories, with new experiences or exotic locales. Adventure films are very similar to the action film genre, in that they are designed to provide an action-filled, energetic experience for the film viewer. Rather than the predominant emphasis on violence and fighting that is found in action films, however, the viewer of adventure films can live vicariously through the travels, conquests, explorations, creation of empires, struggles and situations that confront the main characters, actual historical figures or protagonists.",
      "id": 4,
      "name": "Adventure"
    }
  ],
  "movie": {
    "cover_image_link": null,
    "description": "One night per year, the government sanctions a 12-hour period in which citizens can commit any crime they wish -- including murder -- without fear of punishment or imprisonment. Leo, a sergeant who lost his son, plans a vigilante mission of revenge during the mayhem. However, instead of a death-dealing avenger, he becomes the unexpected protector of four innocent strangers who desperately need his help if they are to survive the night.",
    "genres": [
      "Action",
      "Comedy",
      "Horror",
      "Adventure"
    ],
    "id": 1,
    "period": "1h 44m",
    "release_date": "Fri, 18 Jul 2014 00:00:00 GMT",
    "title": "The Purge: Anarchy",
    "video_link": null
  },
  "success": true
}
```

#### GET `/movies/<int:movie_id>/actors`
- Genrel 
	- Fetches all actors works in a specific movie with its id.
	- Request Arguments: None
	- Returns: success value and all actors information in this movie in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/movies/2/actors -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies/2/actors -X GET -H "Authorization:Bearer {access_token}" `
```
{
  "actors": [
    {
      "age": 44,
      "bio": "An Ukrainian-born actress, an American supermodel, musician, and fashion designer. Over her career, she has appeared in a number of science fiction and action themed films, for which music channel VH1 has referred to her as the reigning queen of kick-butt.",
      "birthdate": "Wed, 17 Dec 1975 00:00:00 GMT",
      "gender": "female",
      "id": 1,
      "image_link": null,
      "movies": [
        {
          "cover_image_link": null,
          "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
          "genres": [],
          "id": 2,
          "period": "2h 33m",
          "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
          "title": "The Final Scream",
          "video_link": null
        }
      ],
      "name": "Milla Jovovich"
    },
    {
      "age": 58,
      "bio": "Mark Anthony McDermott (born October 26, 1961), better known by his professional name of Dylan McDermott, is an American actor, known for his role as lawyer and law firm head Bobby Donnell on the television legal drama The Practice and his role in the series Dark Blue as Lt. Carter Shaw.",
      "birthdate": "Thu, 26 Oct 1961 00:00:00 GMT",
      "gender": "male",
      "id": 2,
      "image_link": null,
      "movies": [
        {
          "cover_image_link": null,
          "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
          "genres": [],
          "id": 2,
          "period": "2h 33m",
          "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
          "title": "The Final Scream",
          "video_link": null
        }
      ],
      "name": "Dylan McDermott"
    },
    {
      "age": 66,
      "bio": "Pierce Brendan Brosnan, OBE (16 May 1953) is an Irish actor, film producer and environmentalist who holds Irish and American citizenship.",
      "birthdate": "Sat, 16 May 1953 00:00:00 GMT",
      "gender": "male",
      "id": 3,
      "image_link": null,
      "movies": [
        {
          "cover_image_link": null,
          "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
          "genres": [],
          "id": 2,
          "period": "2h 33m",
          "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
          "title": "The Final Scream",
          "video_link": null
        }
      ],
      "name": "Pierce Brosnan"
    }
  ],
  "success": true
}
```

#### DELETE `/movies/<int:movie_id>`
- Genrel
	- Deletes the movie of the given ID if it exists.
	- Request Arguement: None
	- Returns: succes value and deleted movie information.
	- Authorization: Executive Producer only can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/movies/{movie_id} -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies/{movie_id} -X GET -H "Authorization:Bearer {access_token}"`
```
{
  "deleted_movie": {
    "cover_image_link": null,
    "description": "A Foreign Service Officer in London tries to prevent a terrorist attack set to hit New York, but is forced to go on the run when she is framed for crimes she did not commit.",
    "genres": [],
    "id": 3,
    "period": "2h 33m",
    "release_date": "Sun, 18 Jul 2021 00:00:00 GMT",
    "title": "Survivor",
    "video_link": null
  },
  "success": true
}
```

#### POST `/movies`
- Genrel
	- creates new movie with specified arguements.
	- Request Arguements: title, period, description, release_date, cover_image_link(optional), video_link(optional).
	- Returns: success value and newly inserted movie.
- sample: 
	- Base url; `curl http://?????/movies -X POST -H "Content-Type: application/json, Authorization:Bearer {access_token}" -d '{"title": "Demo", "period": "2h33m", "release_date": "2020-4-22", "description": "this is demo for adding movie"}'`
	- localhost: `curl http://127.0.0.1:5000/movies -X POST -H "Content-Type: application/json,Authorization:Bearer {access_token} " -d '{"title": "Demo", "period": "2h33m", "release_date": "2020-4-22", "description": "this is demo for adding movie"}'`
```
{
  "new_movie": {
    "cover_image_link": null,
    "description": "this is demo for adding movie",
    "genres": [],
    "id": 6,
    "period": "2h33m",
    "release_date": "Wed, 22 Apr 2020 00:00:00 GMT",
    "title": "Demo",
    "video_link": null
  },
  "success": true
}
```

#### POST `/movies/<int:movie_id>/genres`
- Genrel
	- associate a movie to a specific genre that previously added in the system.
	- Request Arguements: genre_id (must be a valid id of existing genre).
	- Returns: success value.
- sample: 
	- Base url; `curl http://?????//movies/2/genres -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{"genre_id": 1}'`
	- localhost: `curl http://127.0.0.1:5000/movies/2/genres -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{"genre_id": 1}' `
```
{
    "success": true
}
```

#### POST `/movies/<int:movie_id>/actors`
- Genrel
	- add a actor to a movie such that actor is existent in the system.
	- Request Arguements: actor_id (must be a valid id of existing actor).
	- Returns: success value.
- sample: 
	- Base url; `curl http://?????//movies/2/actors -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{"genre_id": 1}'`
	- localhost: `curl http://127.0.0.1:5000/movies/2/actors -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{"genre_id": 1}' `
    - if the actor is not exist in this movie
    ```
    {
        "success": true
    }
    ```
    - it the actor is already exist in this movie
    ```
    {
    "message": "actor is alreay exist in this movie",
    "success": true
    }
    ```

#### PATCH `/movies/<int:movie_id>`
- Genrel
	- modify information of existing movie with specified parameters.
	- Request Arguement: title, period, release_date, description, video_link, cover_image_link(all arguements are optional).
	- Returns: success value and updated movie information.
    - Authorization: Executive Producer can only access this endpoint and access token must be specified in the header of the request. 
- Sample : `
	- Base url `curl http://????/movies/{movie_id} -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{ "title": "demo", "period": "2h32m", "release_date": "2020-3-4", "description": "this is demo!"}'`
	- localhost:  `curl http://127.0.0.1:5000/movies/{movie_id} -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{ "title": "demo", "period": "2h32m", "release_date": "2020-3-4", "description": "this is demo!"}'`
```
{
  "success": true,
  "updated movie": {
    "cover_image_link": null,
    "description": "this is demo!",
    "genres": [],
    "id": 6,
    "period": "2h32m",
    "release_date": "Wed, 04 Mar 2020 00:00:00 GMT",
    "title": "demo",
    "video_link": null
  }
}
```

### Actor Endpoints
#### GET `/actors`
- Genrel
	- bring all actors that was added in the system.
	- Request Arqument: None
	- Returns: success value, list of actors objects in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header ot the request. 
- Sample: 
	- Base url:  `curl http://????/actors-X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies -X GET -H "Authorization:Bearer {access_token}`
```
{
    "actors": [
        {
            "age": 44,
            "bio": "An Ukrainian-born actress, an American supermodel, musician, and fashion designer. Over her career, she has appeared in a number of science fiction and action themed films, for which music channel VH1 has referred to her as the reigning queen of kick-butt.",
            "birthdate": "Wed, 17 Dec 1975 00:00:00 GMT",
            "gender": "female",
            "id": 1,
            "image_link": null,
            "movies": [
                {
                    "cover_image_link": null,
                    "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
                    "genres": [],
                    "id": 2,
                    "period": "2h 33m",
                    "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
                    "title": "The Final Scream",
                    "video_link": null
                }
            ],
            "name": "Milla Jovovich"
        },
        {
            "age": 58,
            "bio": "Mark Anthony McDermott (born October 26, 1961), better known by his professional name of Dylan McDermott, is an American actor, known for his role as lawyer and law firm head Bobby Donnell on the television legal drama The Practice and his role in the series Dark Blue as Lt. Carter Shaw.",
            "birthdate": "Thu, 26 Oct 1961 00:00:00 GMT",
            "gender": "male",
            "id": 2,
            "image_link": null,
            "movies": [
                {
                    "cover_image_link": null,
                    "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
                    "genres": [],
                    "id": 2,
                    "period": "2h 33m",
                    "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
                    "title": "The Final Scream",
                    "video_link": null
                }
            ],
            "name": "Dylan McDermott"
        },
        {
            "age": 66,
            "bio": "Pierce Brendan Brosnan, OBE (16 May 1953) is an Irish actor, film producer and environmentalist who holds Irish and American citizenship.",
            "birthdate": "Sat, 16 May 1953 00:00:00 GMT",
            "gender": "male",
            "id": 3,
            "image_link": null,
            "movies": [
                {
                    "cover_image_link": null,
                    "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
                    "genres": [],
                    "id": 2,
                    "period": "2h 33m",
                    "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
                    "title": "The Final Scream",
                    "video_link": null
                }
            ],
            "name": "Pierce Brosnan"
        },
        {
            "age": 22,
            "bio": "my bio is beautiful!!!!!!!!",
            "birthdate": "Fri, 29 May 1998 00:00:00 GMT",
            "gender": "male",
            "id": 6,
            "image_link": null,
            "movies": [],
            "name": "mahmoud Hamed"
        }
    ],
    "success": true
}
```

#### GET `/actors/<int:actor_id>`
- Genrel 
	- Fetches specific actor with its id.
	- Request Arguments: None
	- Returns: success value and a selected actor object with his movies in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/actors/1 -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/actors/1 -X GET -H "Authorization:Bearer {access_token}`
```
{
  "actors": {
    "age": 44,
    "bio": "An Ukrainian-born actress, an American supermodel, musician, and fashion designer. Over her career, she has appeared in a number of science fiction and action themed films, for which music channel VH1 has referred to her as the reigning queen of kick-butt.",
    "birthdate": "Wed, 17 Dec 1975 00:00:00 GMT",
    "gender": "female",
    "id": 1,
    "image_link": null,
    "movies": [
      {
        "cover_image_link": null,
        "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
        "genres": [
          "Action",
          "Comedy"
        ],
        "id": 2,
        "period": "2h 33m",
        "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
        "title": "The Final Scream",
        "video_link": null
      },
      {
        "cover_image_link": null,
        "description": "One night per year, the government sanctions a 12-hour period in which citizens can commit any crime they wish -- including murder -- without fear of punishment or imprisonment. Leo, a sergeant who lost his son, plans a vigilante mission of revenge during the mayhem. However, instead of a death-dealing avenger, he becomes the unexpected protector of four innocent strangers who desperately need his help if they are to survive the night.",
        "genres": [
          "Action",
          "Comedy",
          "Horror",
          "Adventure"
        ],
        "id": 1,
        "period": "1h 44m",
        "release_date": "Fri, 18 Jul 2014 00:00:00 GMT",
        "title": "The Purge: Anarchy",
        "video_link": null
      }
    ],
    "name": "Milla Jovovich"
  },
  "success": true
}
```

#### GET `/actors/<int:actor_id>/movies`
- Genrel 
	- Fetches all movies of particular actor with its id.
	- Request Arguments: None
	- Returns: success value and all movies information of this actor in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/actors/2/movies -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/actors/2/movies -X GET -H "Authorization:Bearer {access_token}" `
```
{
  "movies": [
    {
      "cover_image_link": null,
      "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
      "genres": [
        "Action",
        "Comedy"
      ],
      "id": 2,
      "period": "2h 33m",
      "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
      "title": "The Final Scream",
      "video_link": null
    },
    {
      "cover_image_link": null,
      "description": "One night per year, the government sanctions a 12-hour period in which citizens can commit any crime they wish -- including murder -- without fear of punishment or imprisonment. Leo, a sergeant who lost his son, plans a vigilante mission of revenge during the mayhem. However, instead of a death-dealing avenger, he becomes the unexpected protector of four innocent strangers who desperately need his help if they are to survive the night.",
      "genres": [
        "Action",
        "Comedy",
        "Horror",
        "Adventure"
      ],
      "id": 1,
      "period": "1h 44m",
      "release_date": "Fri, 18 Jul 2014 00:00:00 GMT",
      "title": "The Purge: Anarchy",
      "video_link": null
    }
  ],
  "success": true
}
```

#### DELETE `/actors/<int:actor_id>`
- Genrel
	- Deletes the actor of the given ID if it exists.
	- Request Arguement: None
	- Returns: succes value and deleted actor information.
	- Authorization: Executive Producer and Casting Director can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/actors/{actor_id} -X DELETE -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/movies/{movie_id} -X DELETE -H "Authorization:Bearer {access_token}`
```
{
  "deleted_actor": {
    "age": 22,
    "bio": "my bio is beautiful!!!!!!!!",
    "birthdate": "Fri, 29 May 1998 00:00:00 GMT",
    "gender": "male",
    "id": 6,
    "image_link": null,
    "movies": [],
    "name": "mahmoud Hamed"
  },
  "success": true
}
```

#### POST `/actors`
- Genrel
	- add new actor with specified parameters.
	- Request Arguement: name, age, gender, bio, birthdate, image_link(optional).
	- Returns: success value.
    - Authorization: Executive Producer and Casting Director can access this endpoint and access token must be specified in the header of the request. 
- Sample : `
	- Base url `curl http://????/actors -X POST -H "Content-Type: application/json" -d '{ "name": "mahmoud Hamed", "age": "22", "gender": "male", "bio": "my bio is beautiful!", "birthdate": "1998-5-29"}'`
	- localhost:  `curl http://127.0.0.1:5000/actors -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{ "name": "mahmoud Hamed", "age": "22", "gender": "male", "bio": "my bio is beautiful!", "birthdate": "1998-5-29"}'`
```
{
    'success': True
}
```

#### PATCH `/actors/<int:actor_id>`
- Genrel
	- modify information of existing actor with specified parameters.
	- Request Arguement: name, age, gender, bio, birthdate, image_link(all arguements are optional).
	- Returns: success value and updated actor information.
    - Authorization: Executive Producer and Casting Director can access this endpoint and access token must be specified in the header of the request. 
- Sample : `
	- Base url `curl http://????/actors/{actor_id} -X POST -H "Content-Type: application/json" -d '{ "name": "mahmoud Hamed", "age": "22", "gender": "male", "bio": "my bio is beautiful!", "birthdate": "1998-5-29"}'`
	- localhost:  `curl http://127.0.0.1:5000/actors/{actor_id} -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{ "name": "mahmoud Hamed", "age": "22", "gender": "male", "bio": "my bio is beautiful!", "birthdate": "1998-5-29"}'`
```
{
  "success": true,
  "updated_actor": {
    "age": 22,
    "bio": "my bio is beautiful!!!!!!!!",
    "birthdate": "Fri, 29 May 1998 00:00:00 GMT",
    "gender": "male",
    "id": 7,
    "image_link": null,
    "movies": [],
    "name": "my bio is beautiful!"
  }
}
```

### Genre Endpoints

#### GET `/genres`
- Genrel
	- bring all genres that was added in the system.
	- Request Arqument: None
	- Returns: success value, list of genres objects in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header ot the request. 
- Sample: 
	- Base url:  `curl http://????/genres -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/genres-X GET -H "Authorization:Bearer {access_token}`
```
{
    "genres": [
        {
            "description": "This major genre type includes films that have tremendous impact, continuous high energy, lots of physical stunts and activity, possibly extended chase scenes, races, rescues, battles, martial arts, mountains and mountaineering, destructive disasters (floods, explosions, natural disasters, fires, etc.), fights, escapes, non-stop motion, spectacular rhythm and pacing, and adventurous heroes - all designed for pure audience escapism with the action sequences at the core of the film.",
            "id": 1,
            "name": "Action"
        },
        {
            "description": " Comedies are light-hearted dramas, crafted to amuse, entertain, and provoke enjoyment. The comedy genre humorously exaggerates the situation, the language, action, and characters. Comedies observe the deficiencies, foibles, and frustrations of life, providing merriment and a momentary escape from day-to-day life. They usually have happy endings, although the humor may have a serious or pessimistic side.",
            "id": 2,
            "name": "Comedy"
        },
        {
            "description": "Films are unsettling films designed to frighten and panic, cause dread and alarm, and to invoke our hidden worst fears, often in a terrifying, shocking finale, while captivating and entertaining us at the same time in a cathartic experience. Horror films effectively center on the dark side of life, the forbidden, and strange and alarming events. They deal with our most primal nature and its fears: our nightmares, our vulnerability, our alienation, our revulsions, our terror of the unknown, our fear of death and dismemberment, loss of identity, or fear of sexuality.",
            "id": 3,
            "name": "Horror"
        },
        {
            "description": "Films are exciting stories, with new experiences or exotic locales. Adventure films are very similar to the action film genre, in that they are designed to provide an action-filled, energetic experience for the film viewer. Rather than the predominant emphasis on violence and fighting that is found in action films, however, the viewer of adventure films can live vicariously through the travels, conquests, explorations, creation of empires, struggles and situations that confront the main characters, actual historical figures or protagonists.",
            "id": 4,
            "name": "Adventure"
        },
        {
            "description": "this is for demo only",
            "id": 11,
            "name": "dummy"
        },
        {
            "description": "this is for demo only",
            "id": 12,
            "name": "dummy 2"
        },
        {
            "description": "this is for demo only",
            "id": 13,
            "name": "dummy 3"
        }
    ],
    "success": true
}
```



#### GET `/genres/<int:genre_id>/movies`
- Genrel 
	- Fetches all movies of particular genre with its id.
	- Request Arguments: None
	- Returns: success value and all movies information of this genre in json format.
	- Authorization: all roles can access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/genres/2/movies -X GET -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/genres/2/movies -X GET -H "Authorization:Bearer {access_token}" `
```
{
  "movies": {
    "movies": [
      {
        "cover_image_link": null,
        "description": "One night per year, the government sanctions a 12-hour period in which citizens can commit any crime they wish -- including murder -- without fear of punishment or imprisonment. Leo, a sergeant who lost his son, plans a vigilante mission of revenge during the mayhem. However, instead of a death-dealing avenger, he becomes the unexpected protector of four innocent strangers who desperately need his help if they are to survive the night.",
        "genres": [
          "Comedy",
          "Horror",
          "Adventure"
        ],
        "id": 1,
        "period": "1h 44m",
        "release_date": "Fri, 18 Jul 2014 00:00:00 GMT",
        "title": "The Purge: Anarchy",
        "video_link": null
      },
      {
        "cover_image_link": null,
        "description": "Aspiring actress, Kia Anderson, is about to learn that the final callback for a horror Feature Film is something more than she could ever of imagined - Something sinister is awaiting for Kia.",
        "genres": [
          "Comedy"
        ],
        "id": 2,
        "period": "2h 33m",
        "release_date": "Sat, 18 Jul 2020 00:00:00 GMT",
        "title": "The Final Scream",
        "video_link": null
      }
    ],
    "success": true
  },
  "success": true
}
```

#### POST `/genres`
- Genrel
	- add new genre with specified parameters.
	- Request Arguement: name, description(optional).
	- Returns: success value and newly inserted genre
    - Authorization: Executive Producer  can only access this endpoint and access token must be specified in the header of the request. 
- Sample : `
	- Base url `curl http://????/genres -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{"description": "this demo for adding new genre", "name": "Demo_genre"}'`
	- localhost:  `curl http://127.0.0.1:5000/genres -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{"description": "this demo for adding new genre", "name": "Demo_genre"}'`
```
{
  "new_genre": {
    "description": "this demo for adding new genre",
    "id": 16,
    "name": "Demo_genre"
  },
  "success": true
}
```

#### DELETE `/genres/<int:genre_id>`
- Genrel
	- Deletes the genre of the given ID if it exists.
	- Request Arguement: None
	- Returns: succes value and deleted genre information.
	- Authorization: Executive Producer can only access this endpoint and access token must be specified in the header of the request. 
- Sample: 
	- Base url:  `curl http://????/genres/{genre_id} -X DELETE -H "Authorization:Bearer {access_token}"` 
	- localhost: `curl http://127.0.0.1:5000/genres/{genre_id} -X DELETE -H "Authorization:Bearer {access_token}`
```
{
  "deleted_genre": {
    "description": "This major genre type includes films that have tremendous impact, continuous high energy, lots of physical stunts and activity, possibly extended chase scenes, races, rescues, battles, martial arts, mountains and mountaineering, destructive disasters (floods, explosions, natural disasters, fires, etc.), fights, escapes, non-stop motion, spectacular rhythm and pacing, and adventurous heroes - all designed for pure audience escapism with the action sequences at the core of the film.",
    "id": 1,
    "name": "Action"
  },
  "success": true
}
```

#### PATCH `/genres/<int:genre_id>`
- Genrel
	- modify existing genre with specified parameters.
	- Request Arguement: name, description(optional).
	- Returns: success value and updated genre
    - Authorization: Executive Producer  can only access this endpoint and access token must be specified in the header of the request. 
- Sample : `
	- Base url `curl http://????/genres -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{ "description": "this demo for updating a genre","name": "Demo_update_genre"}'`
	- localhost:  `curl http://127.0.0.1:5000/genres -X POST -H "Content-Type: application/json" -H "Authorization:Bearer {access_token}" -d '{ "description": "this demo for updating a genre","name": "Demo_update_genre"}'`
```
{
  "success": true,
  "updated_genre": {
    "description": "this demo for updating a genre",
    "id": 16,
    "name": "Demo_update_genre"
  }
}
```