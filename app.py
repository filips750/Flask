from API_parts.restaurants import restaurants
from API_parts.user_driver import auth
from flask import Flask

app = Flask(__name__)

app.register_blueprint(restaurants)
app.register_blueprint(auth)
