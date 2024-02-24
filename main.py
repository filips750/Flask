from API_parts.restaurants import simple_page
from flask import Flask, request, jsonify


app = Flask(__name__)
app.register_blueprint(simple_page)