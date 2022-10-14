from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.dao.models.models import Movie
from project.services import MoviesService


class TestMoviesService:

    @pytest.fixture()
    @patch('project.dao.MoviesDAO')
    def movies_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = Movie(
            id=1,
            title='test_movie',
            description="test_description",
            trailer="test_trailer",
            year=2000,
            rating=1.0,
            genre_id=1,
            director_id=1
        )
        dao.get_all.return_value = [
            Movie(id=1, title="Movie_1"),
            Movie(id=2, title="Movie_2"),
        ]
        return dao

    @pytest.fixture()
    def movies_service(self, movies_dao_mock):
        return MoviesService(dao=movies_dao_mock)

    @pytest.fixture
    def movie(self, db):
        obj = Movie(title="movie")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_movie(self, movies_service, movie):
        assert movies_service.get_item(movie.id)

    def test_movie_not_found(self, movies_dao_mock, movies_service):
        movies_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            movies_service.get_item(10)