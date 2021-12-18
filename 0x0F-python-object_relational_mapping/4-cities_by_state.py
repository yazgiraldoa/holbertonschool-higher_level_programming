#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv


def cities_by_state():
    """
    Function that lists all cities by state.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id;
                """)

    for row in cur.fetchall():
        print(row)

    db.close()

if __name__ == '__main__':
    cities_by_state()
