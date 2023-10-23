#!/usr/bin/python3
""" script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
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

    state_name = sys.argv[4]

    cursor = db.cursor()

    query = "SELECT * FROM cities WHERE state_id IN " \
        "(SELECT id FROM states WHERE name = %s) ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    result_cities = cursor.fetchall()

    for city in result_cities:
        print(city)

    cursor.close()
    db.close()
