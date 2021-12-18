#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv


def my_filter_states():
    """
    Function that lists all states matching an argument.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute(f"""
                SELECT *
                FROM states
                WHERE name LIKE '{argv[4]}'
                ORDER BY states.id
                """)

    for row in cur.fetchall():
        print(row)

    db.close()


if __name__ == '__main__':
    my_filter_states()
