import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db_connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    db_cursor = db_connection.cursor()

    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    result_states = db_cursor.fetchall()

    for state in result_states:
        print(state)

    db_cursor.close()
    db_connection.close()

