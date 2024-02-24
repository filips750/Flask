from flask import Flask, request, jsonify
from db_drivers import get_cursor_and_connection, get_cursor, find_next_id, sanitize

app = Flask(__name__)


# TO DO
# restukturyzacja projektu na różne pliki

@app.get("/user")
def get_user():
    if request.args.get('id'):
        cur = get_cursor()
        query = 'SELECT id, login, password FROM users WHERE id = (?)'
        id = request.args.get('id')
        cur.execute(query, (int(id),))
        user = cur.fetchone()
        return jsonify(user)


@app.post("/register")
def add_user():
    if request.is_json:
        cur, con = get_cursor_and_connection()
        user = request.get_json()
        user["id"] = find_next_id('users')
        query = 'INSERT INTO users (id, login, password) VALUES (?, ?, ?)'
        cur.execute(query, (user['id'], user['login'], user['password']))
        con.commit()
        return user, 201
    return {"error": "Request must be JSON"}, 415


@app.post("/restaurant")
def add_restaurant():
    if request.is_json:
        cur, con = get_cursor_and_connection()
        restaurant = request.get_json()
        restaurant["id"] = find_next_id('restaurants')
        query = 'INSERT INTO restaurants (id, name, localisation) VALUES (?, ?, ?)'
        cur.execute(query, (restaurant['id'],
                            restaurant['name'],
                            restaurant['localisation']))
        con.commit()
        return restaurant, 201
    else:
        return {"error": "Request must be JSON"}, 415
    

@app.get("/restaurants")
def get_restaurants():
    if request.args.get('name'):
        cur = get_cursor()
        query = 'SELECT id, name, localisation FROM restaurants WHERE name LIKE ?'
        name = sanitize(request.args.get('name'))
        cur.execute(query, (name,))
        restaurant = cur.fetchone()
        return jsonify(restaurant)
