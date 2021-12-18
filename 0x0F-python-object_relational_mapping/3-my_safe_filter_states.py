#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument,
but safe from SQL injections.
"""
import MySQLdb
from sys import argv


def my_safe_filter_states():
    """
    Function that lists all states matching an argument,
    safe from SQL injections.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("""
                SELECT *
                FROM states
                WHERE name = %s
                ORDER BY states.id;
                """, (argv[4], ))

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == '__main__':
    my_safe_filter_states()
