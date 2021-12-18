#!/usr/bin/python3
"""
Defining class State that inherits from Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Defining class states that inherits from Base
    Attributes:
        id(int): state id
        name(str): state name
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
