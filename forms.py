from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length

class NewUserForm(FlaskForm):
    """Form for adding a user"""
    username = StringField("Username", validators=[InputRequired()])
    password= PasswordField("Psssword", validators=[InputRequired(), Length(min=8)])
    bio = TextAreaField("Bio")

class LoginForm(FlaskForm):
    """Login form"""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class SearchForm(FlaskForm):
    """Recipe Search form.  Fields here must
    match fields in models.py -> SearchPref"""
    q = StringField("Search", validators=[InputRequired()])
    low_sodium = BooleanField("Low Sodium")
    low_carb = BooleanField("Low Carb")
    high_protein = BooleanField("High Protein")
    dairy_free = BooleanField("Dairy Free")
    egg_free = BooleanField("Egg Free")
    gluten_free = BooleanField("Gluten Free")
    kosher = BooleanField("Kosher")
    low_sugar = BooleanField("Low Sugar")
    shellfish_free =BooleanField("Shellfish Free")
    vegan = BooleanField("Vegan")
    vegetarian = BooleanField("Vegetarian")