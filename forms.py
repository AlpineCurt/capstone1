from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, EmailField
from wtforms.validators import InputRequired, Length, Email

class BooleanField2(BooleanField):
    def __init__(self, label='', validators=None, group='', **kwargs):
        super(BooleanField2, self).__init__(label, validators, **kwargs)
        self.group = group

class NewUserForm(FlaskForm):
    """Form for adding a user"""
    username = StringField("Username", validators=[InputRequired()])
    password= PasswordField("Psssword", validators=[InputRequired(), Length(min=8)])
    email = EmailField("Email", validators=[InputRequired(), Email()])

class LoginForm(FlaskForm):
    """Login form"""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class SearchForm(FlaskForm):
    """Recipe Search form.  Fields here must
    match fields in models.py -> SearchPref"""

    q = StringField("Search")

    # Dietary Restrictions
    low_sodium = BooleanField2("Low Sodium", group="diet")
    low_carb = BooleanField2("Low Carb", group="diet")
    high_protein = BooleanField2("High Protein", group="diet")
    kosher = BooleanField2("Kosher", group="diet")
    low_sugar = BooleanField2("Low Sugar", group="diet")
    vegan = BooleanField2("Vegan", group="diet")
    vegetarian = BooleanField2("Vegetarian", group="diet")
    pescatarian =BooleanField2("Pescatarian", group="diet")

    # Allergies
    dairy_free = BooleanField2("Dairy Free", group="allergy")
    egg_free = BooleanField2("Egg Free", group="allergy")
    shellfish_free =BooleanField2("Shellfish Free", group="allergy")
    gluten_free = BooleanField2("Gluten Free", group="allergy")
    peanut_free = BooleanField2("Peanut Free", group="allergy")

    # Cuisine Type
    American = BooleanField2("American", group="cuisine")
    Asian = BooleanField2("Asian", group="cuisine")
    British = BooleanField2("British", group="cuisine")
    Caribbean = BooleanField2("Caribbean", group="cuisine")
    Central_europe = BooleanField2("Central Europe", group="cuisine")
    Chinese = BooleanField2("Chinese", group="cuisine")
    Eastern_Europe = BooleanField2("Eastern Europe", group="cuisine")
    French = BooleanField2("French", group="cuisine")
    Indian = BooleanField2("Indian", group="cuisine")
    Italian = BooleanField2("Italian", group="cuisine")
    Japanese = BooleanField2("Japanese", group="cuisine")
    Mediterranean = BooleanField2("Mediterranean", group="cuisine")
    Mexican = BooleanField2("Mexican", group="cuisine")
    Middle_Eastern = BooleanField2("Middle Eastern", group="cuisine")
    South_American = BooleanField2("South American", group="cuisine")
    South_East_Asian = BooleanField2("South East Asian", group="cuisine")

    # Meal Type
    Breakfast = BooleanField2("Breakfast", group="mealType")
    Lunch = BooleanField2("Lunch", group="mealType")
    Dinner = BooleanField2("Dinner", group="mealType")
    Snack = BooleanField2("Snack", group="mealType")

class PasswordResetForm(FlaskForm):
    """Form for submitting email for recovering password"""

    email = EmailField("Email", validators=[InputRequired()])

class NewPasswordForm(FlaskForm):
    """Form for submitting a new password"""
    password = PasswordField("New Password", validators=[InputRequired()])