#!/usr/bin/python3
"""
Script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """create an engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """create a configured "Session" class"""
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    """create a Session"""
    session = Session()

    """Add new state"""
    new_state = State(name="Lousiana")

    """Adding new object"""
    session.add(new_state)
    session.commit()

    print(new_state.id)
