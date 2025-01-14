#!/usr/bin/python3
""" Module that defines the `City` class using SQLAlchemy's declarative base.

This module creates a `City` class that represents a table in a MySQL database.
The class inherits from `Base` and defines columns for `id`, `name`, and
`state_id`, where `state_id` is a foreign key referencing the `states` table.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    The ``City`` class represents a table in the database.

    Attributes:
        id (int): The primary key for the city.  name (str): The name of the
        city, with a maximum length of 128 characters.
        state_id (int): A foreign key referencing the `id`
        column in the `states` table.  state (State): A relationship to the
        `State` class.
    """
    __tablename__ = 'cities'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(128), nullable=False)
    state_id: int = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates="cities")
