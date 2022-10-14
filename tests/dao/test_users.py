import pytest

from project.dao.main import UsersDAO
from project.dao.models.models import User


class TestUsersDAO:

    @pytest.fixture
    def users_dao(self, db):
        return UsersDAO(db.session)

    @pytest.fixture
    def user_1(self, db):
        g = User(
            email="example_1@yahoo.com",
            password="Example_1",
            name="Имя 1",
            surname="Фамилия 1",
            favorite_genre="Комедия"
        )
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def user_2(self, db):
        g = User(
            email="example_2@yahoo.com",
            password="Example_2",
            name="Имя 2",
            surname="Фамилия 2",
            favorite_genre="Боевик"
        )
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_user_by_id(self, user_1, users_dao):
        assert users_dao.get_by_id(user_1.id) == user_1

    def test_get_user_by_id_not_found(self, users_dao):
        assert not users_dao.get_by_id(1)

    def test_get_all_users(self, users_dao, user_1, user_2):
        assert users_dao.get_all() == [user_1, user_2]

    def test_get_users_by_page(self, app, users_dao, user_1, user_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert users_dao.get_all(page=1) == [user_1]
        assert users_dao.get_all(page=2) == [user_2]
        assert users_dao.get_all(page=3) == []
