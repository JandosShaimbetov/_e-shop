# _e-shop

e-Shop is an online shopping app

Heroku [link](https://e-shop-43rt1q.herokuapp.com/)

### Prerequisites	

First clone repository:
```
git clone 'repository'
```
Then you need to build containers with the following command:
```
docker-compose up --build
```
### Create database and user
```
docker exec -it e-shop_db bash
su postgres
psql
CREATE DATABASE e-shop;
CREATE USER e-shop_admin WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE e-shop TO e-shop_admin;
```
### Running the migrations
```
docker-compose run --rm eshop python manage.py migrate
```
### Create a superuser
```
docker-compose run --rm eshop python manage.py createsuperuser
```
### Running 
```
docker-compose up
```
### Built With

* [Python](https://www.python.org) - an interpreted high-level general-purpose programming language
* [Django](https://docs.djangoproject.com/en/3.2/) - web framework
* [Django Rest Framework](https://www.django-rest-framework.org) - toolkit for building Web APIs
* [PostgreSQL](https://www.postgresql.org) - open source object-relational database system
* [Postman](https://www.postman.com) - an API platform for building and using APIs
* [Docker](https://www.docker.com) - Docker is an open platform for developing, shipping, and running applications

### Postman Collection

* [Here](https://go.postman.co/workspace/Team-Workspace~211288c4-497a-4020-87ff-ecc0e9c44012/collection/21087623-f3f02821-d053-479f-af45-57003d5df4c0?action=share&creator=21087623) is the project's Postman collection

## Author

* Jandos Shaimbetov
