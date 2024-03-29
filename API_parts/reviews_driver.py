from flask import request, Blueprint
from DB_wrappers.models import Reviews
from app import app, db
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

    review_to_add = request.get_json()
    if not (review_to_add.get('stars') and
            review_to_add.get('review') and
            review_to_add.get('restaurant_id') and
            review_to_add.get('user_id')):
        return {"error": "Request doesn't have all necessary fields"}, 406
    try:
        with app.app_context():
            new_review = Reviews(
                stars=review_to_add.get('stars'),
                review=review_to_add.get('review'),
                restaurant_id=review_to_add.get('restaurant_id'),
                user_id=review_to_add.get('user_id')
            )
            db.session.add(new_review)
            db.session.commit()
    except Exception as e:
        return e
    return review_to_add


@reviews.get('/reviews')
def get_reviews():
    if request.args.get('id'):
        with app.app_context():
            review = Reviews.query.filter_by(id=request.args.get('id')).first()
            return review.to_dict()

    stars_comparator = request.args.get('stars_comparator')
    review_txt = request.args.get("review")

    reviews_query = Reviews.query \
        .filter(Reviews.review.ilike(f"%{review_txt}%")) \
        .filter(or_(Reviews.restaurant_id == request.args.get('id'),
                    Reviews.user_id == request.args.get('id')))

    if stars_comparator not in ['>', '<']:
        reviews = reviews_query.all()
        return [review.dict() for review in reviews]

    if stars_comparator == '>':
        reviews_query = reviews_query.order_by(Reviews.stars)
    elif stars_comparator == '<':
        reviews_query = reviews_query.order_by(Reviews.stars)

    reviews = reviews_query.all()
    return [review.dict() for review in reviews]
