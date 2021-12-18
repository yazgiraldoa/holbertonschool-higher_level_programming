#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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

    """create a Session"""
    session = Session()

    """Get state passed by argument"""
    instance = session.query(State)\
        .filter(State.name == sys.argv[4]).order_by(State.id).first()
    if (instance):
        print(instance.id)
    else:
        print("Not found")
