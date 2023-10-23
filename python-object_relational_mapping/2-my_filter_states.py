#!/usr/bin/python3
"""script that takes in an argument and displays all values 
in the states table of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    query = ("SELECT * FROM states WHERE = '{}' ORDER BY id ASC".format(sys.argv[4]))
    cursor.execute(query)

    result_states = cursor.fetchall()

    for state in result_states:
        if state[1] == sys.argv[4]:
            print(state)

    cursor.close()
    db.close()
