#!/usr/bin/python3
"""
Script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa.
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", user=argv[1],
                         password=argv[2], db=argv[3], port=3306)

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name \
        LIKE BINARY 'N%' ORDER BY states.id;")

    for row in cur.fetchall():
        print(row)

    db.close()
