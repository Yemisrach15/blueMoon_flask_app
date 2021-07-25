from flask import Flask, request, abort, views
# from requests.api import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisourprojectsecretkey '
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Plant.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from appFolder.routes import *
from appFolder import models
db.create_all()