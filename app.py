import os
from secrets_ import flask_secret_key

from flask import Flask, render_template, request, flash, redirect, session, get_flashed_messages, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, conenct_db, User, Comment, Recipe
from forms import NewUserForm, LoginForm

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

@app.before_request
def add_user_to_g():
    """If user is logged in, add user to g"""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

def do_login(user):
    """Log in a user"""
    session[CURR_USER_KEY] = user.id

def do_logout():
    """Logout current user"""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

@app.route("/login", methods=["GET", "POST"])
def login():
    """Handles login.
    If form is valid, logs user in and redirects to homepage.
    Otherwise display login page and errors with login (if any)."""

    if CURR_USER_KEY in session:
        return redirect("/")

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
            form.password.data)
        
        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")
        
        flash("Invalid credentials", "danger")
    
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    """Handles logout"""

    do_logout()
    flash(f"Successfully logged out.", "success")
    return redirect("/")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Handles user signup.
    Create a new user, add them to DB, redirect to home page.
    If form is not valid, present signup form.
    If username taken, flash message and re-present form."""

    if CURR_USER_KEY in session:
        flash("Please logout before createing a new account.", "danger")
        return redirect("/")

    form = NewUserForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                bio=form.bio.data
            )
            db.session.commit()
        except IntegrityError:
            flash("Username already taken", "danger")
            return render_template('signup.html', form=form)

        do_login(user)

        return redirect("/")
    
    else:
        return render_template('signup.html', form=form)

@app.route("/")
def home_page():
    """Show homepage"""
    return render_template("home.html")