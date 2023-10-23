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
    
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    result_cities = cursor.fetchall()

    for city in result_cities:
        print(city)

    cursor.close()
    db.close()
