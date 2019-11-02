from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '74fcfe247ce3a623afb8affb76662531'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# database instance
db = SQLAlchemy(app)

from flaskblog import routes
