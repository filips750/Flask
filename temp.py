import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()

cur.execute('INSERT INTO restaurants (id, name, localisation) VALUES (1, "mcdonald", "wrzeszcz")')

# cur.execute('DROP TABLE reviews')
cur.execute(
'CREATE TABLE reviews (id INT, stars INT, review VARCHAR(1024), fk_restaurant INT NOT NULL, fk_user INT NOT NULL, FOREIGN KEY(fk_restaurant) REFERENCES restaurants(id), FOREIGN KEY(fk_user) REFERENCES users(id))'
)
