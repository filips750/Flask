from DB_wrappers.models import Reviews, Restaurants
from sqlalchemy.sql import func
from app import app, db


def update_avg_stars():
    with app.app_context():
        subquery = db.session.query(func.avg(Reviews.stars)).filter(Reviews.id == Restaurants.id).scalar()
        avg_stars = subquery if subquery is not None else 0.0
        print("Recalculating average stars of restaurants")
        Restaurants.query.update({'avg_stars': avg_stars})
        print("Recalculating successfully ended")
        db.session.commit()
