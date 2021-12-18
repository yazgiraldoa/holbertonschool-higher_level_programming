#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """Create an engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """Create a configured "Session" class"""
    Session = sessionmaker(bind=engine)

    """Create a Session"""
    session = Session()

    """Get all rows in table"""
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
