from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

###--- SQLAlchemy Models ---###

class Comment(db.Model):
    """An individual comment on a recipe"""

    __tablename__ = "comments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade'),
        nullable=False
    )

    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipes.id', ondelete='cascade'),
        nullable=False
    )

    comment = db.Column(
        db.Text,
        nullable=False
    )


class User(db.Model):
    """User Model"""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    password = db.Column(
        db.Text,
        nullable=False
    )

    bio = db.Column(
        db.Text
    )

    favorites = db.relationship(
        "Recipe",
        secondary="user_favorites"
    )

    comments = db.relationship(
        "Comment",
        backref="user",
        primaryjoin=(Comment.user_id == id)
    )

    def __repr__(self):
        return f"<user #{self.id}: {self.username}>"
    
    @classmethod
    def signup(cls, username, password, bio=None):
        """Sign up a user.  Hashes password and adds user to system."""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            password=hashed_pwd,
            bio=bio
        )

        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Find user with 'username' and 'password'.

        This queries for the User by `username`.  If found,
        checks that `password` hash matches the password hash
        for the user.  If both match, return user object.
        Otherwise, returns False. 
        """
        user = cls.query.filter_by(username=username).first()

        if user:
            if bcrypt.check_password_hash(user.password, password):
                return user
        return False


class Recipe(db.Model):
    """Recipe Model"""

    __tablename__ = 'recipes'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    edamam_id = db.Column(
        db.Text,
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.Text,
        nullable=False
    )

    image = db.Column(
        db.Text,
        nullable=False
    )


class Favorite(db.Model):
    """Mapping User's favorite Recipes"""

    __tablename__ = 'user_favorites'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade'),
        nullable=False
    )

    recipe_id = db.Column(
        db.Integer,
        db.ForeignKey('recipes.id', ondelete='cascade'),
        nullable=False
    )

    def serialize(self):
        """Returns a dictionary of attributes.
        Used for jsonifying data"""

        return {
            "user_id": self.user_id,
            "recipe_id": self.recipe_id
        }

class SearchPref(db.Model):
    """A user's search preferences. Columns here must
    match fields in forms.py -> SearchForm"""

    __tablename__ = "user_search_preferences"

    user_id = id = db.Column(
        db.Integer,
        db.ForeignKey('users.id', ondelete='cascade'),
        primary_key=True
    )

    diets = {'balanced', 'high_fiber', 'high_protein', 'low_sodium',
    'low_carb', 'low_fat'}
    health = {'dairy-free', 'egg-free', 'fish_free', 'gluten_free',
    'kosher', 'low_potassium', 'low_sugar', 'lupine-free', 'mediterranean',
    'paleo', 'peanut_free', 'pescatarian', 'shellfish_free', 'vegan',
    'vegetarian'}
    cuisines = {'American', 'Asian', 'British', 'Caribbean', 'Central_Europe',
    'Chinese', 'Eastern_Europe', 'French', 'Indian', 'Italian', 'Japanese',
    'Mediterranean', 'Mexican', 'Middle_Eastern', 'South_American',
    'South_East_Asian'}
    meal_types = {'Breakfast', 'Lunch', 'Dinner', 'Snack'}

    # Dietary Restrictions

    low_sodium = db.Column(
        db.Boolean,
        default=False
    )

    low_carb = db.Column(
        db.Boolean,
        default=False
    )

    high_protein = db.Column(
        db.Boolean,
        default=False
    )

    kosher = db.Column(
        db.Boolean,
        default=False
    )

    low_sugar = db.Column(
        db.Boolean,
        default=False
    )

    vegan = db.Column(
        db.Boolean,
        default=False
    )

    vegetarian = db.Column(
        db.Boolean,
        default=False
    )

    pescatarian = db.Column(
        db.Boolean,
        default=False
    )

    # Allergies

    dairy_free = db.Column(
        db.Boolean,
        default=False
    )

    egg_free = db.Column(
        db.Boolean,
        default=False
    )

    shellfish_free = db.Column(
        db.Boolean,
        default=False
    )

    gluten_free = db.Column(
        db.Boolean,
        default=False
    )

    peanut_free = db.Column(
        db.Boolean,
        default=False
    )

    # Cuisine Type

    American = db.Column(
        db.Boolean,
        default=False
    )

    Asian = db.Column(
        db.Boolean,
        default=False
    )

    British = db.Column(
        db.Boolean,
        default=False
    )

    Caribbean = db.Column(
        db.Boolean,
        default=False
    )

    Central_Europe = db.Column(
        db.Boolean,
        default=False
    )

    Chinese = db.Column(
        db.Boolean,
        default=False
    )

    Eastern_Europe = db.Column(
        db.Boolean,
        default=False
    )

    French = db.Column(
        db.Boolean,
        default=False
    )

    Indian = db.Column(
        db.Boolean,
        default=False
    )

    Italian = db.Column(
        db.Boolean,
        default=False
    )

    Japanese = db.Column(
        db.Boolean,
        default=False
    )

    Mediterranean = db.Column(
        db.Boolean,
        default=False
    )

    Mexican = db.Column(
        db.Boolean,
        default=False
    )

    Middle_Eastern = db.Column(
        db.Boolean,
        default=False
    )

    South_American = db.Column(
        db.Boolean,
        default=False
    )

    South_East_Asian = db.Column(
        db.Boolean,
        default=False
    )

    # Meal Type

    Breakfast = db.Column(
        db.Boolean,
        default=False
    )

    Lunch = db.Column(
        db.Boolean,
        default=False
    )

    Dinner = db.Column(
        db.Boolean,
        default=False
    )

    Snack = db.Column(
        db.Boolean,
        default=False
    )


def conenct_db(app):
    """Connect this database to provided Flask app"""

    db.app = app
    db.init_app(app)

###--- Flask App Models ---###

class RecipeResult():
    """Helper Model for parsing search results
    DEPRECIATED.  NOT USED ANYMORE
    Use RecipeInfo instead."""

    def __init__(self, name, image, id):
        self.name = name
        self.image = image
        self.edamam_id = id
        self.favorite = False

class RecipeInfo():
    """Helper Model for info about a single recipe"""

    def __init__(self, info=None, name=None, image=None, edamam_id=None):
        
        if info:
            self.parse_Edamam_info(info)
        else:
            self.name=name
            self.image=image
            self.edamam_id=edamam_id
        self.favorite=False

    def parse_Edamam_info(self, info):
        """Takes json formatted 'info' and fills object attributes"""

        self.name = info["recipe"]["label"]
        self.ingredients = info["recipe"]["ingredientLines"]
        self.image = info["recipe"]["image"]
        self.instructions = info["recipe"]["url"]
        self.edamam_id = self.get_recipe_id(info)
    
    @staticmethod
    def get_recipe_id(info):
        """Returns edamam_id from 'info'"""

        start = 38
        end = info["_links"]["self"]["href"].index("?")
        id = info["_links"]["self"]["href"][start:end]
        return id