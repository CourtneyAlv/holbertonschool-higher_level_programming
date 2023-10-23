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

    state_name = sys.argv[4]

    cursor = db.cursor()

    query = "SELECT * FROM cities WHERE state_id IN " /
        "(SELECT id FROM states WHERE name = %s) ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    result_cities = cursor.fetchall()

    for city in result_cities:
        print(cities)

    cursor.close()
    db.close()
