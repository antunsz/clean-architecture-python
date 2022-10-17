from collections import namedtuple
from src.infrastrucuture.config import DBConnectionHandler
from src.domain.models import User
from src.infrastrucuture.entities.User import User as UserEntity


class UserRepository:
    """
    User repository
    """

    def insert(self, name:str, password:str) -> UserEntity:
        """
        Insert a new user
        params: name, password
        return: None
        """
        with DBConnectionHandler() as db:
            try:
                user = User(name=name, password=password)
                db.session.add(user)
                db.session.commit()

                return UserEntity(user.id, user.name, user.password)
            except Exception as e:
                db.session.rollback()
                raise e
            finally:
                db.session.close()
        return None

