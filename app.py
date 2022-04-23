from flask import Blueprint, Flask
from flask_cors import CORS
import api

app = Flask(__name__)
CORS(app,supports_credentials=True)

api.register_blueprint(app)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# def login():
#     return '