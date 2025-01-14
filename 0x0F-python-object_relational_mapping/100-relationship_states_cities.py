#!/usr/bin/python3
"""
Adds the State object "California" with the City "San Francisco" to the
database.

This script connects to a MySQL database and creates a new `State` object
named "California" and a new `City` object named "San Francisco". It then
establishes a relationship between the two and commits them to the database.
"""

import sys
from sqlalchemy.exc import SQLAlchemyError
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    try:
        # Create a connection to the database
        engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],  # MySQL username
                sys.argv[2],  # MySQL password
                sys.argv[3]   # Database name
            ),
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)

        # Create a session and add the new State and City objects
        session = Session(engine)
        new_city = City(name='San Francisco')
        new_state = State(name='California')
        new_state.cities.append(new_city)
        session.add_all([new_state, new_city])
        session.commit()
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
