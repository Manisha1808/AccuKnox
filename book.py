import requests
import sqlite3

url = "https://fakerapi.it/api/v1/books?_quantity=5"
r = requests.get(url)
data = r.json()["data"]

conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute("create table if not exists books (id integer primary key, title text, author text, yr integer)")

for b in data:
    c.execute("insert into books (title, author, yr) values (?, ?, ?)", (b["title"], b["author"], b["published"]))

conn.commit()

rows = c.execute("select * from books").fetchall()
for x in rows:
    print(x)

conn.close()
