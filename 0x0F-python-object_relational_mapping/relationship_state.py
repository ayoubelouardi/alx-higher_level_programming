#!/usr/bin/python3
"""
Module that defines the `State` class using SQLAlchemy's declarative base.

This module creates a `State` class that represents a table in a MySQL
database.
The class inherits from `Base` and defines columns for `id` and `name`.
It also establishes a one-to-many relationship with the `City` class.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    The ``State`` class represents a table in the database.

    Attributes:
        id (int): The primary key for the state.
        name (str): The name of the state, with a maximum length of 128
        characters.  cities (List[City]): A list of `City` objects associated
        with this state.
    """
    __tablename__ = 'states'
    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
