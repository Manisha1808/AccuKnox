import csv
import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("create table if not exists users (id integer primary key, name text, email text)")

with open("users.csv") as f:
    r = csv.reader(f)
    next(r)
    for row in r:
        if len(row) == 2:
            c.execute("insert into users (name, email) values (?, ?)", (row[0], row[1]))

conn.commit()

rows = c.execute("select * from users").fetchall()
for x in rows:
    print(x)

conn.close()
