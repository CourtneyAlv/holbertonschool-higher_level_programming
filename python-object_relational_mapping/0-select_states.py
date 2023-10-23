#!/usr/bin/python3
""" Lists all the states from mySQL database """
import sys
import MYSQLdb

if __name__ == "__main__"
    db = MYSQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    list_st = cursor.fetchall()

    for list_st in list_sts:
        print(list_st)

    cursor.close()
    db.close()
