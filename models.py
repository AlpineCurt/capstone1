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
    def signup(cls, username, password, bio):
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


class Favorites(db.Model):
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

def conenct_db(app):
    """Connect this database to provided Flask app"""

    db.app = app
    db.init_app(app)

###--- Flask App Models ---###

class RecipeResult():
    """Helper Model for parsing search results"""

    def __init__(self, name, image, id):
        self.name = name
        self.image = image
        self.id = id

class RecipeInfo():
    """Helper Model for info about a single recipe"""

    def __init__(self, info=None):
        
        if info:
            self.parse_Edamam_info(info)

    def parse_Edamam_info(self, info):
        """Takes json formatted 'info' and fills object attributes"""

        self.name = info["recipe"]["label"]
        self.ingredients = info["recipe"]["ingredientLines"]
        self.image = info["recipe"]["image"]
        self.instructions = info["recipe"]["url"]