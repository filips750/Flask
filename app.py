from API_parts.restaurants import restaurants
from API_parts.user_driver import auth
from API_parts.reviews import reviews
from flask import Flask, request
from flask_session import SqlAlchemySessionInterface, Session
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12Kudelicze!@localhost:3306/kuluars'
db = SQLAlchemy(app)

# Configure Flask-Session to use SqlAlchemySessionInterface
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db

Session(app)


app = Flask(__name__)

# @app.before_request
# def decode_json():
#     if request.is_json:
#         pass


app.register_blueprint(restaurants)
app.register_blueprint(auth)
app.register_blueprint(reviews)