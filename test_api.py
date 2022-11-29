"""Tests for API routes"""

import os

from unittest import TestCase
from flask import session
from models import db, conenct_db, User, Favorite, Recipe

os.environ['DATABASE_URL'] = "postgresql:///wildcarrot_test"

from app import app, CURR_USER_KEY

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db.drop_all()
db.create_all()

app.config['WTF_CSRF_ENABLED'] = False

class TestFavorites(TestCase):
    """Test Cases for API favoriting and unfavoriting"""

    def setUp(self):
        """Clear any botched data; Create test client; Clear session"""

        User.query.delete()
        Favorite.query.delete()
        Recipe.query.delete()
        db.session.commit()

        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess.clear()

    def test_add_favorite_not_logged_in(self):
        """Try to add a favorite while not logged in
        /api/favorite POST"""
        with self.client as c:
            with self.client.session_transaction() as sess:
                self.assertNotIn(CURR_USER_KEY, sess, msg="User logged in, preventing rest of tests from running correctly.")
            
            TEST_FAV_DATA = {
                "edamam_id": "2f6ad7442c3853e72770662ec6c51bcb"
            }

            resp = c.post("/api/favorite", json=TEST_FAV_DATA)

            self.assertEqual(resp.status_code, 400, msg="Favorite API POST not logged in did not return 400 code.")

            favorites = Favorite.query.all()
            self.assertEqual(len(favorites), 0, msg="A favorite was added to DB when it should have been rejected.")

    def test_add_favorite_logged_in_new_recipe(self):
        """Add a favorite while logged in
        Recipe does NOT exist in database
        /api/favorite POST"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        with self.client as c:

            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id

            TEST_FAV_DATA = {
                "edamam_id": "2f6ad7442c3853e72770662ec6c51bcb",
                "recipe_name": "Thai Shrimp Curry"
            }

            resp = c.post("/api/favorite", json=TEST_FAV_DATA)

            self.assertEqual(resp.status_code, 201, msg="Favorite did not get added while user is logged in.")
            
            data = resp.json

            self.assertEqual(data,{
                "favorite": {
                    "Thai Shrimp Curry": "Added to favorites"
                } 
            })

            test_recipes = Recipe.query.all()
            test_favorites = Favorite.query.all()

            self.assertEqual(len(test_recipes), 1, msg="Recipe was not added to recipes table")
            self.assertEqual(len(test_favorites), 1, msg="Favoite was not added to favorites table")

            test_recipe = Recipe.query.first()
            test_favorite = Favorite.query.first()

            self.assertEqual(test_recipe.edamam_id, "2f6ad7442c3853e72770662ec6c51bcb", msg="edamam_id not added to recipes table")
            self.assertEqual(test_recipe.name, "Thai Shrimp Curry", msg="Recipe name not get added to database")
            self.assertEqual(test_favorite.user_id, test_user.id, msg="user_id not added to user_favorites table")
            self.assertEqual(test_favorite.recipe_id, test_recipe.id, msg="recipe_id not added to user_favorites table")
    
    def test_add_favorite_logged_in_recipe_exists(self):
        """Add a favorite while logged in
        Recipe already exists in database
        /api/favorite POST"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )

        test_r = Recipe(
            edamam_id="2f6ad7442c3853e72770662ec6c51bcb",
            name="Thai Shrimp Curry"
        )
        db.session.add(test_r)
        db.session.commit()

        with self.client as c:

            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id

            TEST_FAV_DATA = {
                "edamam_id": "2f6ad7442c3853e72770662ec6c51bcb",
                "recipe_name": "Thai Shrimp Curry"
            }
        
        resp = c.post("/api/favorite", json=TEST_FAV_DATA)

        self.assertEqual(resp.status_code, 201, msg="Favorite did not get added while user is logged in.")
        
        data = resp.json

        self.assertEqual(data,{
            "favorite": {
                "Thai Shrimp Curry": "Added to favorites"
            } 
        })

        test_recipes = Recipe.query.all()
        test_favorites = Favorite.query.all()

        self.assertEqual(len(test_recipes), 1, msg="Recipe was incorrectly added to recipes table")
        self.assertEqual(len(test_favorites), 1, msg="Favoite was not added to favorites table")

        test_recipe = Recipe.query.first()
        test_favorite = Favorite.query.first()

        self.assertEqual(test_recipe.edamam_id, "2f6ad7442c3853e72770662ec6c51bcb", msg="edamam_id not added to recipes table")
        self.assertEqual(test_recipe.name, "Thai Shrimp Curry", msg="Recipe name not get added to database")
        self.assertEqual(test_favorite.user_id, test_user.id, msg="user_id not added to user_favorites table")
        self.assertEqual(test_favorite.recipe_id, test_recipe.id, msg="recipe_id not added to user_favorites table")

    def test_delete_favorite_not_logged_in(self):
        """Delete favorite while NOT logged in
        /api/favorite DELETE"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )

        test_r = Recipe(
            edamam_id="2f6ad7442c3853e72770662ec6c51bcb",
            name="Thai Shrimp Curry"
        )
        db.session.add(test_r)
        db.session.commit()

        test_f = Favorite(user_id=test_user.id, recipe_id=test_r.id)
        db.session.add(test_f)
        db.session.commit()        

        with self.client as c:
            with self.client.session_transaction() as sess:
                self.assertNotIn(CURR_USER_KEY, sess, msg="User logged in, preventing rest of tests from running correctly.")
            
            TEST_DATA = {
                "edamam_id": "2f6ad7442c3853e72770662ec6c51bcb"
            }

            resp = c.delete("/api/favorite", json=TEST_DATA)

            self.assertEqual(resp.status_code, 400, msg="Favorite API DELETE not logged in did not return 400 code.")

            test_recipe = Recipe.query.first()
            self.assertEqual(test_recipe.name, "Thai Shrimp Curry", msg="recipe erroneosly deleted from recipes table")

            test_fav = Favorite.query.one_or_none()
            self.assertIsNotNone(test_fav, msg="favorite erroneously deleted from user_favorites_table")
    
    def test_delete_favorite_logged_in(self):
        """Delete favorite while logged in
        /api/favorite DELETE"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )

        test_r = Recipe(
            edamam_id="2f6ad7442c3853e72770662ec6c51bcb",
            name="Thai Shrimp Curry"
        )
        db.session.add(test_r)
        db.session.commit()

        test_f = Favorite(user_id=test_user.id, recipe_id=test_r.id)
        db.session.add(test_f)
        db.session.commit()

        test_f_confirm = Favorite.query.one_or_none()
        self.assertIsNotNone(test_f_confirm, msg="test favorite not added to database")

        with self.client as c:
            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id

            TEST_DATA = {
                "edamam_id": "2f6ad7442c3853e72770662ec6c51bcb"
            }

            resp = c.delete("/api/favorite", json=TEST_DATA)

            self.assertEqual(resp.status_code, 204, msg="Favorite API DELETE while logged in did not return 204 code.")

            test_recipe = Recipe.query.first()
            self.assertEqual(test_recipe.name, "Thai Shrimp Curry", msg="recipe erroneosly deleted from recipes table")

            test_fav = Favorite.query.one_or_none()
            self.assertIsNone(test_fav, msg="Favorite not deleted from database")