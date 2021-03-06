#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """create an engine"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    """create a configured "Session" class"""
    Session = sessionmaker(bind=engine)

    """create a Session"""
    session = Session()

    """Getting the state and deleting it"""
    for data in session.query(City, State)\
            .filter(State.id == City.state_id).order_by(City.id):
        print(f"{data.State.name}: ({data.City.id}) {data.City.name}")
