from typing import Optional

from sqlalchemy import desc
from werkzeug.exceptions import NotFound

from project.dao.base import BaseDAO
from project.dao.models import Genre, Movie, Director, User
from project.tools.security import generate_password_hash


class GenresDAO(BaseDAO[Genre]):
    __model__ = Genre


class MoviesDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_order_by(self, filter: Optional[str], page: Optional[int] = None):
        stmt = self._db_session.query(self.__model__)
        if filter:
            stmt = stmt.order_by(desc(self.__model__.year))
        if page:
            try:
                return stmt.paginate(page, self._items_per_page).items
            except NotFound:
                return []
        return stmt.all()


class DirectorsDAO(BaseDAO[Director]):
    __model__ = Director


class UsersDAO(BaseDAO[User]):
    __model__ = User

    def create(self, email, password):
        try:
            self._db_session.add(
                User(
                    email=email,
                    password=generate_password_hash(password)
                )
            )
            self._db_session.commit()
            print("Пользователь добавлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()

    def get_by_email(self, email):
        try:
            stmt = self._db_session.query(self.__model__).filter(self.__model__.email == email).all()[0]
            return stmt
        except Exception as e:
            print(e)
            return {}

    def update(self, email, data):
        try:
            self._db_session.query(self.__model__).filter(self.__model__.email == email).update(
                data
            )
            self._db_session.commit()
            print("Пользователь обновлен")
        except Exception as e:
            print(e)
            self._db_session.rollback()
