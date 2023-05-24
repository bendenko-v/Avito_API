# Django REST API like Avito API

Django REST framework app like Avito API.

## Usage

Run `docker-compose up -d` in the **db_avito** folder.

Fill the database with **location.json, categories.json, user.json, ads.json** from the **datasets** folder and the command `python manage.py loaddata <file.json>` 

Start Django server to run app.

## App features

- "ad/": GET - get all ads,
- "ad/create/": POST - authorized user can add a new ad with POST request multipart/form-data with file `image` or simple JSON:
```
{
    'author': 10,
    'category': 4,
    'name': 'Flower',
    'price': 30000,
    'description': 'Garden flower',
    'is_published': false,
}
```
- "ad/{id}/": GET - get ad by id
- "ad/{id}/update/": PATCH - authorized user or admin/moderator can update ad with PATCH request multipart/form-data with file `image` or simple JSON:
```
{
    'name': 'Flower uppdated',
    'price': 20000,
    'description': 'Garden flower upppdated',
    'is_published': true,
}
```
- "ad/{id}/delete/": DELETE - authorized user or admin/moderator can delete ad by id
---
- "cat/": GET - get all categories,
- "cat/create/": POST - add new category with JSON body like:
```
{
    "name": "Autoparts"
}
```
- "cat/{id}/": GET - get category by id
- "cat/{id}/update/": PATCH - update category by id
- "cat/{id}/delete/": DELETE - delete category by id
- ---
- "user/": GET - get all users,
- "user/create/": POST - add new user with JSON body like:
```
{
    "first_name": "First_name",
    "last_name": "Last_name",
    "username": "Username",
    "password": "Password",
    "email": "email@email.me",
    "birth_date": "1999-01-01",
    "role": "moderator",
    "age": 33,
    "location": [  # optional
        {
            "name": "St. Petersburg", # optional
            "lat": "59.9343",  # optional
            "lng": "30.3351"   # optional
        }
    ]
}
```
- "user/{id}/": GET - get user by id
- "user/{id}/update/": PATCH - update user by id
- "user/{id}/delete/": DELETE - delete user by id
- ---
- "selection/": GET - get all selections created by all users,
- "selection/create/": POST - authorized user can add a new selection with JSON body like:
```
{
    "name": "My selection",
    "items": [
        15,
        16
    ]
}
```
- "selection/{id}/": GET - get selection by id
- "selection/{id}/update/": PATCH - update selection by id (only authorized user)
- "selection/{id}/delete/": DELETE - delete selection by id (only authorized user)

## Tests

The tests cover the following views:

- Creating an advertisement: 
  - Method and endpoint: POST '/ads/'
  - Test case will verify that ad can be created as expected.

- Creating a collection: 
  - Method and endpoint: POST '/selection/'
  - Test case will verify that collection can be created as expected.

- Retrieving a list of ads (without filters):
  - Method and endpoint: GET '/ads/'
  - Test case will validate the retrieval of a list of ads without any filters applied.

- Retrieving a single advertisement:
  - Method and endpoint: GET '/ads/<ad_id>/'
  - Test case will check the retrieval of a specific ad based on its id.