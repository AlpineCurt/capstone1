"""User View tests"""

import os
from unittest import TestCase
from flask import session

from models import db, conenct_db, User

os.environ['DATABASE_URL'] = "postgresql:///wildcarrot_test"

from app import app, CURR_USER_KEY

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db.drop_all()
db.create_all()

app.config['WTF_CSRF_ENABLED'] = False

class LoginSignupTestCase(TestCase):
    """Test views for Login and Signup routes"""

    def setUp(self):
        """Clear any botched data; Create test client; Clear session"""
        User.query.delete()
        db.session.commit()

        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess.clear()

    def test_login_not_currently_logged_in(self):
        """Display Login Page - not already logged in
        /login  GET"""

        with self.client as c:
            
            resp = c.get("/login")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)

            with c.session_transaction() as sess:
                self.assertNotIn("CURR_USER_KEY", sess, msg="Login Page displayed with a user logged in")
            
            self.assertIn("Username", html, msg="Username field not in Login Page")
    
    def test_login_while_already_logged_in(self):
        """Display Login Page - user already logged in
        /login GET"""

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = 1
        
            resp = c.get("/login")

            self.assertEqual(resp.status_code, 302)

    def test_login_sumbit_valid_credentials(self):
        """User logs in with valid credentials
        /login POST"""

        User.signup(username="CoolGuy",
            password="ilikesunglasses",
            bio="ShrimpMaster3000")
        db.session.commit()

        with self.client as c:

            resp = c.post("/login",
                data={"username": "CoolGuy", "password": "ilikesunglasses"},
                follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("CoolGuy", html)

            with c.session_transaction() as sess:
                self.assertIn(CURR_USER_KEY, sess, msg="curr_user not in session after valid login.")
    
    def test_login_submit_invalid_credentials(self):
        """User logs in with invalid credentials
        /login POST"""

        User.signup(username="CoolGuy",
            password="ilikesunglasses",
            bio="ShrimpMaster3000")
        db.session.commit()

        with self.client as c:
            resp = c.post("/login",
                data={"username": "CoolGuy", "password": "ilikeraybands"},
                follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn("Invalid credentials", html)
            
            with c.session_transaction() as sess:
                self.assertNotIn("curr_user", sess, msg="user was added to session with invalid credentials.")

    def test_signup_view_not_logged_in(self):
        """Display signup.html page while NOT logged in
        /signup GET"""

        with self.client as c:
            resp = c.get("/signup")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Join Wild Carrot", html)

            with c.session_transaction() as sess:
                self.assertNotIn(CURR_USER_KEY, sess, msg="A user was logged in while viewing the signup.html page")

    def test_signup_view_logged_in(self):
        """Display signup page while user is already logged in
        /signup GET"""

        with self.client as c:
            with c.session_transaction() as sess:
                sess[CURR_USER_KEY] = 1

            resp = c.get("/signup", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Please logout before createing a new account.",
                html,
                msg="Message to logout before creating account did not display.")
    
    def test_signup_submit_valid_inputs(self):
        """Submit valid username, password, and bio
        /signup POST"""

        with self.client as c:
            resp = c.post("/signup",
                data={"username": "CoolGuy",
                    "password": "ilikesunglasses",
                    "bio": "ShrimpMaster2999"},
                follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("CoolGuy", html)

            test_user = User.query.filter_by(username="CoolGuy").first()
            self.assertIsInstance(test_user, User, msg="Test user not added to database after signup.")

            with c.session_transaction() as sess:
                self.assertIn(CURR_USER_KEY, sess, msg="User not logged in after successful signup")
                test_user = User.query.filter_by(username="CoolGuy").first()
                self.assertEqual(sess["curr_user"], test_user.id, msg="session curr_user not set correctly.")
    
    def test_signup_username_taken(self):
        """Submit signup with a taken username
        /signup POST"""

        User.signup(username="CoolGuy",
            password="ilikesunglasses",
            bio="ShrimpMaster3000")
        db.session.commit()

        with self.client as c:
            resp = c.post("/signup",
                data={"username": "CoolGuy",
                    "password": "ilikesunglasses",
                    "bio": "ShrimpMaster2999"},
                follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Username already taken", html, "username taken error did not display")

            with c.session_transaction() as sess:
                self.assertNotIn(CURR_USER_KEY, sess, msg="User should not be logged in after failed signup")
