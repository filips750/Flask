from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hashed_pw = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_of_restaurant = db.Column(db.String(255), unique=True, nullable=False)
    description_of_restaurant = db.Column(db.String(1024), unique=True, nullable=False)
    localisation = db.Column(db.String(255), unique=True, nullable=False)

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stars = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(1024), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)