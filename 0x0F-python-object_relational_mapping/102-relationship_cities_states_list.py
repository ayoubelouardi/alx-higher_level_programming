#!/usr/bin/python3
"""
Module that performs MySQL queries using SQLAlchemy.

This script connects to a MySQL database, creates tables if they don't exist,
and queries the City table to display city details along with their
associated state.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from relationship_state import Base, State
from relationship_city import City


def create_database_connection(username, password, database):
    """Create and return a SQLAlchemy engine for the MySQL database."""
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        username,  # MySQL username
        password,  # MySQL password
        database   # Database name
    )
    return create_engine(db_uri, pool_pre_ping=True)


def query_and_display_cities(session):
    """Query the City table and display city details."""
    for a_city in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(a_city.id, a_city.name, a_city.state.name))


def main():
    """Main function to execute the script."""
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        return

    try:
        # Create database connection and tables
        engine = create_database_connection(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3])
        Base.metadata.create_all(engine)

        # Create a session and query the database
        Session = sessionmaker(bind=engine)
        session = Session()

        query_and_display_cities(session)
    except SQLAlchemyError as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
