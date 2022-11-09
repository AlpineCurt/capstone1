import os
from secrets_ import flask_secret_key


from flask import Flask, render_template, request, flash, redirect, session, get_flashed_messages
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, conenct_db

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///wildcarrot')
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = flask_secret_key
toolbar = DebugToolbarExtension(app)

conenct_db(app)

@app.route("/")
def home_page():
    """Show homepage"""
    return render_template("home.html")