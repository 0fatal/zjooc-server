from flask import Flask


from api.course import courseApi
from api.user import userApi

def register_blueprint(app: Flask):
    app.register_blueprint(courseApi, url_prefix='/course')
    app.register_blueprint(userApi, url_prefix='/user')
