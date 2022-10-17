from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infrastructure.entities.Base import Base

class User(Base):
    """
    User entity
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    id_pet = relationship("Pet")

    def __repr__(self):
        return f"User(name='{self.name}')"
