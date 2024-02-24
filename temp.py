import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute('INSERT INTO restaurants (id, name, localisation) VALUES (1, "mcdonald", "wrzeszcz")')
print(cur)