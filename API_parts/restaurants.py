from flask import Flask, request, jsonify
from db_drivers import get_cursor, get_cursor_and_connection, find_next_id, sanitize


app = Flask(__name__)


@app.get("/restaurants")
def get_restaurants():
    if request.arg.get('name'):
        cur = get_cursor()
        query = 'SELECT id, login, password FROM restaurants WHERE name LIKE ?'
        name = sanitize(request.args.get('name'))
        cur.execute(query, (int(name),))


@app.post("/restaurant")
def add_restaurant():
    if request.is_json:
        cur, con = get_cursor_and_connection()
        restaurant = request.get_json()
        restaurant["id"] = find_next_id()
        query = 'INSERT INTO restaurants (id, name, localisation) VALUES (?, ?, ?)'
        cur.execute(query, (restaurant['id'],
                            restaurant['name'],
                            restaurant['localisation']))
        con.commit()
