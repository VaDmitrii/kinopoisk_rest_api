from unittest.mock import patch

import pytest

from project.exceptions import ItemNotFound
from project.dao.models.models import User
from project.services import UsersService


class TestUsersService:

    @pytest.fixture()
    @patch('project.dao.UsersDAO')
    def users_dao_mock(self, dao_mock):
        dao = dao_mock()
        dao.get_by_id.return_value = User(
            id=1,
            email='test_email',
            password="test_password",
            name="test_name",
            surname="test_surname",
            favorite_genre="test_genre",
        )
        dao.get_all.return_value = [
            User(
                id=1,
                email='test_email_1',
                password="test_password_1",
                name="test_name_1",
                surname="test_surname_1",
                favorite_genre="test_genre_1"
            ),
            User(
                id=2,
                email='test_email_2',
                password="test_password_2",
                name="test_name_2",
                surname="test_surname_2",
                favorite_genre="test_genre_2"
            ),
        ]
        return dao

    @pytest.fixture()
    def users_service(self, users_dao_mock):
        return UsersService(dao=users_dao_mock)

    @pytest.fixture
    def user(self, db):
        obj = User(name="user")
        db.session.add(obj)
        db.session.commit()
        return obj

    def test_get_user(self, users_service, user):
        assert users_service.get_item(user.id)

    def test_user_not_found(self, users_dao_mock, users_service):
        users_dao_mock.get_by_id.return_value = None

        with pytest.raises(ItemNotFound):
            users_service.get_item(10)

    @pytest.mark.parametrize('page', [1, None], ids=['with page', 'without page'])
    def test_get_users(self, users_dao_mock, users_service, page):
        users = users_service.get_all(page=page)
        assert len(users) == 2
        assert users == users_dao_mock.get_all.return_value
        users_dao_mock.get_all.assert_called_with(page=page)
