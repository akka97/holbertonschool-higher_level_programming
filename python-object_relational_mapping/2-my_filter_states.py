#!/usr/bin/python3
"""module for getting states that start with letter n"""
import MySQLdb
import sys


if __name__ == '__main__':
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
               .format(sys.argv[4]))
    states = cr.fetchall()
    for state in states:
        print(state)
    cr.close()
    db.close()
