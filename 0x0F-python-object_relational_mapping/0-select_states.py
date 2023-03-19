#!/usr/bin/python3
"""script that list all state from db hbtn_0o_0_usa"""

import MySQLdb


if __name__ == '__main__':
    
    """getting access to db and states"""

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv{2], db=argv[3])


    cur = db.cursor()
    cur.execute("SElECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
