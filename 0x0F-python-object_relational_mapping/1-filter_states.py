#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv


def filter_states():
    """
    Function that lists all states with name starting by 'N'.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == '__main__':
    filter_states()
