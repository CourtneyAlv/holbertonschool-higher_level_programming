#!/usr/bin/python3
""" Lists all the states from mySQL database """
import sys
import MySQLdb


def list_states(username, password, database):
    """
        lists all states from the database hbtn_0e_0_usa
        ARGS:
            username: MYSQL Username
            password: MYSQL password
            dtatbase: dtatabase name
    """


db = MYSQLdb.connect(
    host="localhost", 
    port=3306, 
    user=username, 
    passwd=password, 
    db=database
)

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

list_st = cursor.fetchall()

for list_st in list_sts:
    print(list_st)

cursor.close()
db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

list_states(username, password, database)
