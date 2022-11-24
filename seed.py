"""Seed database with sample data"""

from app import db
#from models import User, Recipe, Favorite, Comment

db.drop_all()
db.create_all()