from sqlalchemy import Column, String, Integer, Float, ForeignKey

from project.setup.db import models
from sqlalchemy.orm import relationship


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), unique=True, nullable=False)
    description = Column(String(250), nullable=True)
    trailer = Column(String(100), nullable=True)
    year = Column(Integer, nullable=True)
    rating = Column(Float, nullable=True)
    genre_id = Column(Integer, ForeignKey(f'{Genre.__tablename__}.id'), nullable=True)
    director_id = Column(Integer, ForeignKey(f'{Director.__tablename__}.id'), nullable=True)
    genre = relationship(Genre)
    director = relationship(Director)


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String(150), unique=True, nullable=True)
    password = Column(String(100), nullable=True)
    name = Column(String(50))
    surname = Column(String(80))
    favorite_genre = Column(String(50))
