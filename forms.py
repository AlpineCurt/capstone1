from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Length

class NewUserForm(FlaskForm):
    """Form for adding a user"""
    username = StringField("Username", validators=[InputRequired()])
    password= PasswordField("Psssword", validators=[InputRequired(), Length(min=8)])
    bio = TextAreaField("Bio")

class LoginForm(FlaskForm):
    """Login form."""
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])