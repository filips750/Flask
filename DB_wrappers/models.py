from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    hashed_pwd = db.Column(db.String(255), unique=False, nullable=False)
    def to_dict(self):
        return{
            "email": self.email
        }

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_restaurant = db.Column(db.String(255), unique=True, nullable=False)
    description_of_restaurant = db.Column(db.String(1024), unique=True, nullable=False)
    localisation = db.Column(db.String(255), unique=True, nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'name_of_restaurant': self.name_of_restaurant,
            'description_of_restaurant': self.description_of_restaurant,
            'localisation': self.localisation
        }

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(1024), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fk_restaurant = db.Column(db.Integer, foreign_key=True, nullable=False)
    fk_user = db.Column(db.Integer, foreign_key=True, nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'stars': self.stars,
            'review': self.review,
            'email': self.email,
            'restaurant_id': self.fk_restaurant,
            'user_id': self.fk_user
        }