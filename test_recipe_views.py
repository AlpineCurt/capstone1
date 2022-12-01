"""Tests for Search and recipe views"""

import os

from unittest import TestCase
from flask import session
from models import db, conenct_db, User, Recipe, Favorite
from testing_data import test_image

os.environ['DATABASE_URL'] = "postgresql:///wildcarrot_test"

from app import app, CURR_USER_KEY

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db.drop_all()
db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class TestHomePage(TestCase):
    """Tests for Home Page"""

    def setUp(self):
        """Clear any botched data; Create test client; Clear session"""

        User.query.delete()
        db.session.commit()

        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess.clear()
    
    def test_home_page_not_logged_in(self):
        """Home Page view NOT logged in
        / GET"""
        
        with self.client as c:
            resp = c.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Search for Recipes", html, msg="home.html did not load")
    
    def test_home_page_logged_in(self):
        """Home Page view while logged in
        / GET"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        with self.client as c:
            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id
            
            resp = c.get("/")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Search for Recipes", html, msg="home.html did not load")
            self.assertIn("CoolGuy", html, msg="Logged in username did not appear on homepage")


class TestSearchResults(TestCase):
    """Tests for Search results"""

    def setUp(self):
        """Clear any botched data; Create test client; Clear session"""

        User.query.delete()
        db.session.commit()

        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess.clear()
        
    def test_search_results_not_logged_in(self):
        """Search Results while NOT logged in
        /search GET"""

        User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        with self.client as c:
            
            resp = c.get("/search?q=pizza")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertNotIn("CoolGuy", html, msg="A username not logged in appeared on the page")
            self.assertIn("Pizza", html, msg="Search results did not appear or do not make sense.")
    
    def test_search_results_logged_in(self):
        """Search results while logged in
        /search GET"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        with self.client as c:

            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id
            
            resp = c.get("/search?q=pizza")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("CoolGuy", html, msg="A logged in username did not appear on the page")
            self.assertIn("Pizza", html, msg="Search results did not appear or do not make sense.")
    
    def test_single_recipe_view(self):
        """Single Recipe View while NOT logged in
        /recipes/<string:edamam_id> GET"""

        with self.client as c:

            resp = c.get("/recipes/4d63b2fef227383bd4891f5c5217e88b")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Meat Lovers", html, "Recipe name did not appear in html.")
            self.assertIn("bacon", html, msg="An ingredient did not appear in html.")
            self.assertIn("For Coooking Instructions", html, "Instructions link did not appear in html.")
    
    def test_single_recipe_view(self):
        """Sing Recipe View while logged in
        /recipes/<string:edamam_id> GET"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        with self.client as c:

            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id

            resp = c.get("/recipes/4d63b2fef227383bd4891f5c5217e88b")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Meat Lovers", html, "Recipe name did not appear in html.")
            self.assertIn("bacon", html, msg="An ingredient did not appear in html.")
            self.assertIn("For Coooking Instructions", html, "Instructions link did not appear in html.")
            self.assertIn("CoolGuy", html, msg="A logged in username did not appear on the page")


class TestFavoritesView(TestCase):
    """Testing for displaying a user's favorited recipes"""

    def setUp(self):
        """Clear any botched data; Create test client; Clear session"""

        User.query.delete()
        db.session.commit()

        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess.clear()
    
    def test_favorites_not_logged_in(self):
        """Favorites page while NOT logged in
        /favorites GET"""

        with self.client as c:

            resp = c.get("/favorites", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Please login or create", html, msg="flash message not included in redirect")

    def test_favorites_logged_in(self):
        """Favorites page while logged in
        /favorites GET"""

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        test_recipe = Recipe(edamam_id="4d63b2fef227383bd4891f5c5217e88b",
            name="Meat Lovers' Pizza Dip",
            image=test_image)
        db.session.add(test_recipe)
        db.session.commit()

        test_favorite = Favorite(user_id=test_user.id, recipe_id=test_recipe.id)
        db.session.add(test_favorite)
        db.session.commit()

        with self.client as c:

            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id
            
            resp = c.get("/favorites")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Meat Lovers", html, msg="favorited recipe did not appear in html")
            self.assertNotIn("Please login or create", html, msg="Flash message for not being logged in appeared.")
            self.assertIn("CoolGuy", html, msg="Logged in username did not appear in html")