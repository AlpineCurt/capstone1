"""User Model tests"""

import os
from unittest import TestCase

from models import db, User

os.environ['DATABASE_URL'] = "postgresql:///wildcarrot_test"

from app import app

db.create_all()

class UserModelTestCase(TestCase):
    
    def setUp(self):
        """Clear any botched data; Create test client."""

        User.query.delete()

        self.client = app.test_client()
    
    def  test_user_model(self):
        """Does the basic model create correctly?"""

        u = User(
            username="CoolGuy",
            password="ilikesunglasses"
        )

        db.session.add(u)
        db.session.commit()

        u_test = User.query.all()

        self.assertEqual(len(u_test), 1)
        self.assertEqual(len(u_test[0].comments), 0)
    
    def test_signup(self):
        """User.signup method"""

        user1 = User.signup(
            username="CoolGuy",
            password="ilikesunglasses"
        )

        self.assertIsInstance(user1,
            User,
            msg="User signup method did not return a User object.")

        user1_query = User.query.filter_by(username="CoolGuy").first()
        self.assertNotEqual(user1_query.password,
            'ilikesunglasses',
            msg="Password did not hash correctly.")
    
    def test_authenticate(self):
        """User.authenticate method"""

        user1 = User.signup(
            username="CoolGuy",
            password="ilikesunglasses"
        )

        user1_auth = User.authenticate("CoolGuy", "ilikesunglasses")
        self.assertIsInstance(user1_auth, User,
            msg="Correct password did not correctly authenticate.")
        
        user1_bad_password = User.authenticate("CoolGuy", "sunglasses")
        self.assertFalse(user1_bad_password,
            msg="Authentication with wrong password did not return False.")
        
        user1_bad_username = User.authenticate("RadGuy", "ilikesunglasses")
        self.assertFalse(user1_bad_username,
            msg="Authentication with wrong username did not return False.")