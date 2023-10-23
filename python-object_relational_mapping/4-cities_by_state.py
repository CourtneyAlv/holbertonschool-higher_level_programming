#!/usr/bin/python3
""" write a script that is safe from MySQL injections! """
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

    state_name = sys.argv[4]

    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)

    result_states = cursor.fetchall()

    for city in result_cities:
        print(cities)

    cursor.close()
    db.close()
