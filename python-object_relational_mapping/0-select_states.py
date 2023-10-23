#!/usr/bin/python3
""" Lists all the states from mySQL database """
import sys
import MYSQLdb

def list_states(username, password, database):

db = MYSQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)

cursor = db.cursor()

cursor.execute("Select * FROM states ORDER BY id ASC")

states = cursor.fetchall()

for state in states:
    print(state)

cursor.close()
db.close()

if __name__ == "__main__":

