from flask import Flask, request, jsonify, Blueprint
from db_drivers import get_cursor_and_connection, get_cursor, find_next_id


auth = Blueprint('auth', __name__, template_folder='API_parts')
@auth.route('/auth')


@auth.get("/user")
def get_user():
    if request.args.get('id'):
        cur = get_cursor()
        query = 'SELECT id, login, password FROM users WHERE id = (?)'
        id = request.args.get('id')
        cur.execute(query, (int(id),))
        user = cur.fetchone()
        return jsonify(user)


@auth.post("/register")
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
