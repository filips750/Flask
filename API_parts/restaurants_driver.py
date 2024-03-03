from flask import request, Blueprint
from DB_wrappers.models import Restaurants
from app import app, db
from sqlalchemy import or_


restaurants = Blueprint('restaurants', __name__, template_folder='API_parts')


@restaurants.route('/places')
@restaurants.get("/restaurants")
def get_restaurants():
    if request.args.get('id'):
        with app.app_context():
            restaurant = Restaurants.query \
                .filter_by(id=request.args.get('id')) \
                .first()
            return restaurant.to_dict()

    stars_comparator = request.args.get('stars_comparator')
    restaurant_txt = request.args.get["restaurant"]

    restaurants_query = Restaurants.query \
        .filter(Restaurants.name_of_restaurant.ilike(f"%{restaurant_txt}%")) \
        .filter(or_(Restaurants.fk_restaurant == request.args.get('id'),
                    Restaurants.fk_user == request.args.get('id')))

    if stars_comparator not in ['>', '<']:
        return [restaurant.dict() for restaurant in restaurants]

    if stars_comparator == '>':
        restaurants_query = restaurants_query \
            .filter(Restaurants.stars_avg > request.args.get('stars'))
    elif stars_comparator == '<':
        restaurants_query = restaurants_query \
            .filter(Restaurants.stars_avg < request.args.get('stars'))

    restaurants = restaurants_query.all()
    return [restaurant.dict() for restaurant in restaurants]


@restaurants.post("/restaurant")
def add_restaurant():
    if not request.is_json:
        return {"error": "Request must be JSON"}, 415

    with app.app_context():
        restaurant = request.get_json()
        new_restaurant = Restaurants(
            name_of_restaurant=restaurant.get('name_of_restaurant'),
            description_of_restaurant=restaurant.get('description_of_restaurant'),
            localisation=restaurant.get('localisation')
        )
        db.session.add(new_restaurant)
        db.session.commit()
        restaurant_dict = new_restaurant.to_dict()
        return restaurant_dict
