#!/usr/bin/python3
"""python file that contains the class definition of a State and an
instance Base = declarative_base() """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Representing a state for MySQL dtatabase.

     __tablename__: (str): name of MySQL table to store states
    id int: State Id
    name str: state name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
