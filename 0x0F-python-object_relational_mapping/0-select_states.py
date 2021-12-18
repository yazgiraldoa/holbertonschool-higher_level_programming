#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


def select_states():
    """
    Function that lists all states.
    """

    """Connecting to the database"""
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    """The cursor gives us the ability to have multiple seperate
    working environments through the same connection to the database"""
    cur = db.cursor()

    """Executing the query"""
    cur.execute("SELECT * FROM states ORDER BY states.id")

    for row in cur.fetchall():
        print(row)

    """Closing the connection to the database"""
    db.close()


if __name__ == '__main__':
    select_states()
