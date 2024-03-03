from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_pwd = db.Column(db.String(255), unique=False, nullable=False)

    def to_dict(self):
        return {
            "email": self.email
        }


class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_restaurant = db.Column(db.String(255), unique=True, nullable=False)
    description_of_restaurant = db.Column(db.String(1024), unique=True, nullable=False)
    localisation = db.Column(db.String(255), unique=True, nullable=False)
    avg_stars = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name_of_restaurant': self.name_of_restaurant,
            'description_of_restaurant': self.description_of_restaurant,
            'localisation': self.localisation,
            'avg_stars': self.avg_stars
        }


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(1024), unique=True, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'stars': self.stars,
            'review': self.review,
            'restaurant_id': self.restaurant_id,
            'user_id': self.user_id
        }
