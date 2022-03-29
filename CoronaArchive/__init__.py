from flask import Flask, render_template, url_for, redirect, flash

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import sqlite3
import qrcode
# import os

app = Flask(__name__)
# dir = os.path.dirname(os.path.abspath(__file__))

app.config['SECRET_KEY'] = '714b0d0941d7658afa9dc194f0033602'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cad.db'

mydb = SQLAlchemy(app)

encrypt = Bcrypt(app)

signin = LoginManager(app)

from CoronaArchive import routes