from flask import Flask, request, jsonify, Blueprint
from db_drivers import get_cursor, get_cursor_and_connection, find_next_id, sanitize


restaurants = Blueprint('restaurants', __name__, template_folder='API_parts')
@restaurants.route('/places')


@restaurants.get("/restaurants")
def get_restaurants():
    if request.args.get('name'):
        cur = get_cursor()
        query = 'SELECT id, name, localisation FROM restaurants WHERE name LIKE ?'
        name = '%' + sanitize(request.args.get('name')) + '%'
        cur.execute(query, (name,))
        restaurants = cur.fetchall()
        return jsonify(restaurants)


@restaurants.post("/restaurant")
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
    else:
        return {"error": "Request must be JSON"}, 415
