from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режиссер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Пол Вайц'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Американский пирог'),
    'description': fields.String(required=True, max_length=250, example='Смешной фильм для подростков'),
    'trailer': fields.String(required=True, max_length=100, example='https://youtu.be/8rI2G_eTTUs'),
    'year': fields.Integer(required=True, example=1999),
    'rating': fields.Integer(required=True, example=7.0),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=150, example="stifler20@yahoo.com"),
    'password': fields.String(required=True, max_length=100, example="!FinchSucks!"),
    'name': fields.String(required=True, max_length=50, example="Стив"),
    'surname': fields.String(required=True, max_length=80, example="Стифлер"),
    'favorite_genre': fields.Nested(genre),
})
