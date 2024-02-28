from flask import Flask, request, jsonify, Blueprint
from db_drivers import get_cursor_and_connection, get_cursor


reviews = Blueprint('reviews', __name__, template_folder='API_parts')
@reviews.route('/rev')


@reviews.get('/review')
def get_review():
    if request.args.get('id'):
        query = 'SELECT stars, review, fk_restaurant, fk_user FROM reviews WHERE id = ?'
        cur = get_cursor()
        id = request.args.get('id')
        cur.execute(query, (int(id),))
        user = cur.fetchone()
        return jsonify(user)


@reviews.post('/review')
def add_review():
    if request.is_json:
        cur, con = get_cursor_and_connection()
        review = request.get_json()
        query = 'INSERT INTO reviews (stars, review, fk_restaurant, fk_user) VALUES (?, ?, ?, ?)'
        if not (review.get('stars') and review.get('review') and review.get('fk_restaurant') and review.get('fk_user')):
            return {"error": "Request doesn't have all necessary fields"}, 406
        try:
            cur.execute(query, (review["stars"],
                                review["review"], 
                                review["fk_restaurant"],
                                review["fk_user"]))
            con.commit()
        except:
            return 'Woopsie'
        return review
    else:
        return {"error": "Request must be JSON"}, 415


@reviews.get('/reviews')
def get_reviews():
    query = 'SELECT stars, review, fk_restaurant, fk_user FROM reviews WHERE'
    begin_len = len(query)
    cur = get_cursor()
    add_and_to_query = False
    parameters_list = []

    if request.args.get('id'):
        query += 'id = ?'
        id = request.args.get('id')
        cur.execute(query, (int(id),))
        response = cur.fetchone()
        return jsonify(response)
    
    if request.args.get('review'):
        query += 'review LIKE ?'
        add_and_to_query = True
        parameters_list.append(request.args.get('review'))

    if request.args.get('fk_restaurant'):
        if add_and_to_query:
            query += 'AND'
        query += 'fk_restaurant = ?'
        add_and_to_query = True
        parameters_list.append(request.args.get('fk_restaurant'))

    if request.args.get('fk_user'):
        if add_and_to_query:
            query += 'AND'
        query += 'fk_user = ?'
        add_and_to_query = True
        parameters_list.append(request.args.get('fk_user'))

    return jsonify(cur.execute(query, tuple(parameters_list)).fetchall())
    
    
            
        
        