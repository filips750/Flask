from flask import Flask, request, jsonify, Blueprint
from db_drivers import get_cursor_and_connection, get_cursor
from DB_wrappers.models import Reviews, db
from app import app
from sqlalchemy import or_


reviews = Blueprint('reviews', __name__, template_folder='API_parts')
@reviews.route('/rev')


@reviews.get('/review')
def get_review():
    if request.args.get('id'):
        with app.app_context():
            review = Reviews.query.filter_by(id=request.args.get('id')).first()
        return review.to_dict()


@reviews.post('/review')
def add_review():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415

    review = request.get_json()
    if not (review.get('stars') and review.get('review') and review.get('fk_restaurant') and review.get('fk_user')):
        return {"error": "Request doesn't have all necessary fields"}, 406
    try:
        with app.app_context():
            new_review = Reviews(stars=review.get('stars'), review=review.get('review'), email=review.get('email'))
            db.session.add(new_review)
            db.session.commit()
    except:
        return 'Woopsie'
    return review


@reviews.get('/reviews')
def get_reviews():
    if request.args.get('id'):
        with app.app_context():
            review = Reviews.query.filter_by(id=request.args.get('id')).first()
            return review.to_dict()
    
    stars_comparator = request.args.get('stars_comparator')
    review_txt = request.args.get["review"]

    reviews_query = Reviews.query \
        .filter(Reviews.review.ilike(f"%{review_txt}%")) \
        .filter(or_(Reviews.fk_restaurant == request.args.get('id'), Reviews.fk_user == request.args.get('id')))

    if stars_comparator not in ['>', '<']:
        return [review.dict() for review in reviews]


    if stars_comparator == '>':
        reviews_query = reviews_query.filter(Reviews.stars > request.args.get('stars'))
    elif stars_comparator == '<':
        reviews_query = reviews_query.filter(Reviews.stars < request.args.get('stars'))

    reviews = reviews_query.all()
    return [review.dict() for review in reviews]
    
            
        
        