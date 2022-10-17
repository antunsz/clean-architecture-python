from collections import namedtuple
from src.infrastrucuture.config import DBConnectionHandler
from src.infrastrucuture.entities.User import User


class UserRepository:
    """
    User repository
    """

    def insert(self, name:str, password:str) -> User:
        """
        Insert a new user
        params: name, password
        return: None
        """
        inserted_data = namedtuple('User', ['id', 'name', 'password'])
        with DBConnectionHandler() as db:
            try:
                user = User(name=name, password=password)
                db.session.add(user)
                db.session.commit()

                return inserted_data(user.id, user.name, user.password)
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
        return None

