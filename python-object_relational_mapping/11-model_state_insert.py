#!/usr/bin/python3
"""script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Lousiana')
    session.add(new_state)
    new_inst = session.query(State).filter_by(name='Louisiana').first()
    print(new_inst.id)
    session.commit()
