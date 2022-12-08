import os
from secrets_ import flask_secret_key, edamam_app_id, edamam_app_key, google_app_password

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from flask_mail import Mail, Message
# from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError
import requests

from models import db, conenct_db, User, Recipe, RecipeInfo, Favorite
from forms import NewUserForm, LoginForm, SearchForm, PasswordResetForm, NewPasswordForm

from helper_functions import parse_search_results, build_search_params, valid_params, set_modify_search_form, set_favorites, get_reset_token, verify_reset_token, generate_reset_email

"""Test data for frontend testing"""
# from testing_data import search_results_2
# from json import loads

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///wildcarrot')
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = flask_secret_key

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'wildcarrot.recovery@gmail.com'
app.config['MAIL_PASSWORD'] = google_app_password
mail = Mail(app)

#toolbar = DebugToolbarExtension(app)

conenct_db(app)

@app.before_request
def add_user_to_g():
    """If user is logged in, add user to g"""
    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None

### ---Login, Logout, Signup, Profile routes--- ###

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
                email=form.email.data
            )
            db.session.commit()
        except IntegrityError:
            flash("Username or email already taken", "danger")
            return render_template('signup.html', form=form)

        do_login(user)

        return redirect("/")
    
    else:
        return render_template('signup.html', form=form)

### ---Search route(s)--- ###

@app.route("/search")
def search():
    """Search Results from homepage search"""

    params = build_search_params(request.args.to_dict())

    if not valid_params(params):
        flash("Please enter a search term or select a category", "success")
        return redirect("/")

    if len(request.args) > 0:
        resp = requests.get("https://api.edamam.com/api/recipes/v2", params=params)
    else:
        resp = requests.get(session["next_page"])
    
    resp_json = resp.json()
    recipes = parse_search_results(resp_json)
    if g.user:
        set_favorites(g.user.id, recipes)

    try:
        session["next_page"] = resp_json["_links"]["next"]["href"]
        results_from = resp_json["from"]
        results_to = resp_json["to"]
        count = resp_json["count"]
    except KeyError:
        results_from = None
        results_to = None
        count = None

    form = set_modify_search_form(request.args.to_dict())

    return render_template("search_results.html",
        recipes=recipes,
        results_from=results_from,
        results_to=results_to,
        count=count,
        form=form,
        logged_in=bool(g.user)
        )

@app.route("/recipes/<string:edamam_id>")
def single_recipe(edamam_id):
    """Display page for a single recipe"""

    resp = requests.get(f"https://api.edamam.com/api/recipes/v2/{edamam_id}",
            params={
                "type": "public",
                "app_id": edamam_app_id,
                "app_key": edamam_app_key
            })
    
    recipe =  RecipeInfo(resp.json())
    if g.user:
        set_favorites(g.user.id, [recipe])

    return render_template("single_recipe_view.html", recipe=recipe)

@app.route("/favorites")
def user_profile():
    """Display a profile page for a user."""

    if CURR_USER_KEY not in session:
        flash("Please login or create an account to view and save favorites", "danger")
        return redirect("/")
    
    user = User.query.get(g.user.id)

    user_favs = user.favorites
    recipes = [RecipeInfo(
        name=fav.name,
        image=fav.image,
        edamam_id=fav.edamam_id
    ) for fav in user_favs]

    for fav in recipes:
        fav.favorite = True
    
    return render_template("user_favorites.html",
        user=user,
        recipes=recipes,
        logged_in=bool(g.user))
    

### ---Favoriting API route(s)--- ###

@app.route("/api/favorite", methods=["POST"])
def add_favorite():
    """Add a user's favorite"""

    if g.user == None:
        error = jsonify({"Error": "Must be logged in to add favorites"})
        return (error, 400)
    
    user_id = session[CURR_USER_KEY]
    edamam_id = request.json["edamam_id"]
    recipe_name = request.json["recipe_name"]
    image = request.json["image"]

    recipe = Recipe.query.filter_by(edamam_id=edamam_id).one_or_none()

    # Check if edamam_id already in recipes table.  Add if not.
    if recipe == None:
        recipe = Recipe(edamam_id=edamam_id,
            name=recipe_name,
            image=image)
        db.session.add(recipe)
        db.session.commit()

    new_favorite = Favorite(user_id=user_id, recipe_id=recipe.id)
    db.session.add(new_favorite)
    db.session.commit()

    return (jsonify(favorite={
        recipe_name: "Added to favorites"
    }), 201)


@app.route("/api/favorite", methods=["DELETE"])
def remove_favorite():
    """Remove a user's favorite"""
    
    if g.user == None:
        error = jsonify({"Error": "Must be logged in to remove favorites"})
        return (error, 400)
    
    user_id = session[CURR_USER_KEY]
    edamam_recipe_id = request.json["edamam_id"]

    recipe_id = Recipe.query.filter_by(edamam_id=edamam_recipe_id).first()

    old_favorite = Favorite.query.filter(
        Favorite.user_id==user_id,
        Favorite.recipe_id==recipe_id.id
        ).one_or_none()
    
    if old_favorite == None:
        error = jsonify({"Error": "Favorite not found"})
        return (error, 400)
    
    db.session.delete(old_favorite)
    db.session.commit()
    return (jsonify(message="Deleted"), 204)


### ---Homepage route(s)--- ###

@app.route("/")
def home_page():
    """Show homepage"""
    form = SearchForm()
    return render_template("home.html", form=form)

### ---Password Recovery route(s)--- ###

@app.route("/sendmail")
def sendmail():
    msg = Message()
    msg.subject = "Hello!"
    msg.recipients = ['alpinecurt@gmail.com']
    msg.sender = 'wildcarrot.recovery@gmail.com'
    msg.body = 'Did this work???'

    mail.send(msg)

@app.route("/recoverpassword", methods=["GET", "POST"])
def recover_password():
    """User requests to reset password"""

    form = PasswordResetForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).one_or_none()
        if user == None:
            """No need to let phishers know an email is invalid"""
            return render_template("password_reset_email_sent.html")
        
        msg = generate_reset_email(user)
        mail.send(msg)
        return render_template("password_reset_email_sent.html")

        
    return render_template("password_forgot.html", form=form)

@app.route("/resetpassword", methods=["GET", "POST"])
def reset_password():
    """Link from password reset email.
    Verify jwt, then allow user to set new password"""
    
    form = NewPasswordForm()
    if form.validate_on_submit():
        User.update_password(request.form["username"], form.password.data)
        db.session.commit()
        flash("Password Updated", "success")
        return redirect("/")

    if not request.args["token"]:
        """Token missing"""
        return redirect("/")
    
    token = request.args["token"]
    username = verify_reset_token(token)
    if username == None:
        flash("Invalid token", "danger")
        return redirect("/recoverpassword")

    return render_template("/password_reset.html", form=form, username=username)