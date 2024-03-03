from flask import Flask
from flask_session import Session
# from flask_session import SqlAlchemySessionInterface
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql://root:12Kudelicze!@localhost:3306/kuluars'

db = SQLAlchemy(app)

# Configure Flask-Session to use SqlAlchemySessionInterface
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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
from helpers.restaurant_helper import update_avg_stars


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12Kudelicze!@localhost:3306/kuluars'
db.init_app(app)
update_avg_stars()


app.register_blueprint(restaurants)
app.register_blueprint(auth)
app.register_blueprint(reviews)
