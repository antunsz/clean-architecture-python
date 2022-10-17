import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infrastructure.entities.Base import Base


class AnimalTypes(enum.Enum):
    """
    Define animal types
    """

    DOG = 'dog'
    CAT = 'cat'
    BIRD = 'bird'
    FISH = 'fish'
    OTHER = 'other'


class Pet(Base):
    """
    Pet entity
    """
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    id_user = Column(Integer, ForeignKey('users.id'))
    species = Column(Enum(AnimalTypes))
    age = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Pet(name='{self.name}')"
