from flask import Blueprint, Flask
import api

app = Flask(__name__)
api.register_blueprint(app)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# def login():
#     return '