from flask import Flask, request, session
from flask_session import SqlAlchemySessionInterface, Session
from flask_sqlalchemy import SQLAlchemy
from DB_wrappers.models import Users, Reviews, Restaurants, db


app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12Kudelicze!@localhost:3306/kuluars'
db.init_app(app)

# Configure Flask-Session to use SqlAlchemySessionInterface
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# @app.before_request
# def decode_json():
#     if request.is_json:
#         pass

from API_parts.restaurants_driver import restaurants
from API_parts.user_driver import auth
from API_parts.reviews_driver import reviews

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12Kudelicze!@localhost:3306/kuluars'
db.init_app(app)

app.register_blueprint(restaurants)
app.register_blueprint(auth)
app.register_blueprint(reviews)