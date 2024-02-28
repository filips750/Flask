from flask import Flask, request, jsonify, Blueprint
from db_drivers import get_cursor_and_connection, get_cursor


auth = Blueprint('auth', __name__, template_folder='API_parts')
@auth.route('/auth')


@auth.get("/user")
def get_user():
    if request.args.get('id'):
        cur = get_cursor()
        query = 'SELECT id, email, password FROM users WHERE id = ?'
        id = request.args.get('id')
        return jsonify(cur.execute(query, (int(id),)).fetchone())


@auth.post("/register")
def add_user():
    if request.is_json:
        cur, con = get_cursor_and_connection()
        user = request.get_json()
        query = 'INSERT INTO users (email, password) VALUES (?, ?)'
        cur.execute(query, (user['email'], user['password']))
        con.commit()
        return user, 201
    return {"error": "Request must be JSON"}, 415
