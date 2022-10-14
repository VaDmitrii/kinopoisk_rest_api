import pytest

from project.dao.models.models import Movie
from project.setup.api.models import genre, director


class TestMoviesView:
    @pytest.fixture
    def movie(self, db):
        obj = Movie(title="movie")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_many(self, client, movie):
        response = client.get("/movies/")
        assert response.status_code == 200
        assert response.json == [{
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "trailer": movie.trailer,
            "year": movie.year,
            "rating": movie.rating,
            "genre": {"id": None, "name": None},
            "director": {"id": None, "name": None},
        }]

    def test_movie_pages(self, client, movie):
        response = client.get("/movies/?page=1")
        assert response.status_code == 200
        assert len(response.json) == 1

        response = client.get("/movies/?page=2")
        assert response.status_code == 200
        assert len(response.json) == 0

    def test_movie(self, client, movie):
        response = client.get("/movies/1/")
        assert response.status_code == 200
        assert response.json.get("title") == movie.title

    def test_movie_not_found(self, client, movie):
        response = client.get("/movies/2/")
        assert response.status_code == 404
