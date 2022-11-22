import os

from unittest import TestCase
from helper_functions import parse_search_results, get_recipe_id, set_favorites
from testing_data import search_results, single_recipe
from json import loads
from models import db, RecipeInfo, User, Favorite, Recipe

os.environ['DATABASE_URL'] = "postgresql:///wildcarrot_test"

from app import app, CURR_USER_KEY

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db.drop_all()
db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class ParseSearchResultsTestCase(TestCase):
    """Test Parsing of Search Results"""

    def test_get_recipe_id(self):
        """Do we get the correct Edamam API recipe id from the search results?"""

        results_json = loads(search_results)
        edaman_id_0 = get_recipe_id(results_json["hits"][0])
        edaman_id_1 = get_recipe_id(results_json["hits"][1])
        edaman_id_7 = get_recipe_id(results_json["hits"][7])

        self.assertEqual(edaman_id_0, "61c68c5e83feda078d4cd2f178a8aba3")
        self.assertEqual(edaman_id_1, "b8d126947d802def1f795016d75297c4")
        self.assertEqual(edaman_id_7, "d67920cf9dff811cfa122c3c8e98d753")

    def test_parse_search_results(self):
        """Does the function pull the correct data from search results?"""

        results = parse_search_results(search_results)

        #DELETE HERE
        # for result in results:
        #     print(result.name, result.edamam_id)

        self.assertEqual(len(results), 20, msg="Results does not have expected 20 objects")
        self.assertEqual(results[0].name, "Cauliflower and Tofu Curry Recipe", msg="Name of recipe is incorrect.")
        self.assertEqual(results[0].image[:4], "http", msg="Image is not a url")


class TestRecipeInfoModel(TestCase):
    """Tests for RecipeInfo Model"""

    def test_init(self):

        test_model_1 = RecipeInfo()

        self.assertIsInstance(test_model_1, RecipeInfo, msg="Object with no 'info' parameter did not get created.")

        single_recipe_json = loads(single_recipe)
        test_model_2 = RecipeInfo(single_recipe_json)

        self.assertEqual(test_model_2.name, "Thai Shrimp Curry", msg="RecipeInfo name is not correct.")
        self.assertEqual(test_model_2.ingredients,
            [
                "1½ c. jasmine rice",
                "1 package butternut squash",
                "4 oz. green beans",
                "1 tbsp. vegetable oil",
                "1 small onion",
                "1 tbsp. red curry paste",
                "1 tsp. red curry paste",
                "1 lb. large shrimp",
                "1 can light coconut milk",
            ])
        self.assertEqual(test_model_2.image, f"https://edamam-product-images.s3.amazonaws.com/web-img/d9b/d9bea22b3c3dde2174a56a4faf08c551.jpg?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLWVhc3QtMSJHMEUCIEI0YoNhxvf1qsx5mm%2F%2B8G91gqRFjEAmkSQplieDeOJaAiEAxQOV87KdHp7JTwEc%2FziOnd6tUBTiQNKdVSc5wbjdqmkqzAQIfRAAGgwxODcwMTcxNTA5ODYiDFadt5etH37qUK%2F2XiqpBAaJ7tCv6N9eF%2FmcJHRBCmBqpSv7xq%2FFeht4JowWBUuOGnxnvWCF6ixoTlSRklLPMS8TwMDcJD012uR4pv59IfY%2BURe8hofPbCCbx8kQqv4lGuSxO5VKXVgjxqtBrrSgIVTHdhI4JPa7sqv%2B6hMAdLcydpYl79h%2Bgnr56%2B24yET853dSuDLP%2FfYBi%2F8BKAjoC9bzmNJilpAPQkNJcepjNpYXDE0BC7P6QSUTMzhydq2y6H8ik3Cskn5Mvar0sm%2BjM5p9RhKT9PBUYvfmAIiYeDyuURyLe9BVRwg5AadDdTvSoYJeinpr2BWZO29cE4ZwBL0Qb5w38HfNdQ7pfPYt99MK%2FU3AwLlIJrJwNzl2QcyUaEKtcB6GQlFpikbL3vXEcIvJT9o88nZf8Kae2uhQV4qktbKROZXmQARzMKMhbs6T3O6XLS7k74mo85SnmiQ0A%2FZ5nA9fgEmMr5LxoVzeGj%2FyLVyhFTjTMkF6bgHIAtBCCJR2P9n1f%2B4Id0ysKGrTR2H09eWbIw3oeyu5TbJcsHLs%2F%2FvyECpLcaIh3alIzswO5AApmKv%2BON0B5e66hDsoTjw0jsiO6C36433r0BEg%2FeLIF%2BQ3j6VgbjiZvXHAFaHwHugR1vqB56Li2h4fZ3eYcmR%2B4kiKUACMcX8lmIaOcLJqe2cSOs5BvRiSFqHJEVLigc5%2FJqq5KVbDEMjfmK7PH%2BLHd6Q1XjOmdqBnbPQIA%2BsZbA7mzr8UXPIw1onqmwY6qQFBi5GJIfHVtK1NcmMsclTOnq4ic5%2F0CLIeb%2Fdw2mu%2BjffLNwNGUbfpEqLLSZnuB10B7OMBDUW7pj6iOYBf2vXzT4hIwcgdf%2Bvxjn8cLRhszunMUxb2G%2BTIJ4eWCpLMuCexDIz3YtEDzt%2FQMMs8XMyWNsE0GhlIf6kGQmFdt0PNwLGYMgWBQ04gA0ubRpFtKbNWkSSXISrn26hFWUbvPaCGGl6xNVEqLZ%2Fq&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221120T213717Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=ASIASXCYXIIFBFPHP7N7%2F20221120%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=929c2274a4da10c0241887582ffe1cdf405e157cb1836dc0785b7a01e67f1603")
        self.assertEqual(test_model_2.instructions, "http://www.delish.com/cooking/recipe-ideas/recipes/a30586/thai-shrimp-curry-recipe/")

class TestSetFavorites(TestCase):
    """Test Model for set_favorites() """

    def setUp(self):
        """Clear any botched data; Create test client; Clear session"""

        User.query.delete()
        Favorite.query.delete()
        Recipe.query.delete()
        db.session.commit()

        self.client = app.test_client()
        with self.client.session_transaction() as sess:
            sess.clear()

    def test_set_favorites(self):

        test_user = User.signup(
            username="CoolGuy",
            password="ilikesunglasses",
            bio="I really like dolphins."
        )
        db.session.commit()

        r1 = Recipe(edamam_id="2f6ad7442c3853e72770662ec6c51bcb", name="Thai Shrimp Curry")
        r2 = Recipe(edamam_id="94996060ba29ed1cd02c150f1b70d344", name="Curry Mayonnaise")
        r3 = Recipe(edamam_id="416b453ac07cc42ecd9a8775aa166451", name="Roasted Cashews & Curry Leaves")
        r4 = Recipe(edamam_id="611d58b2fcec4d894ed8c6443616d12e", name="Vegan Chickpea Coconut Curry")

        db.session.add_all([r1, r2, r3, r4])
        db.session.commit()

        f1 = Favorite(user_id=test_user.id, recipe_id=r1.id)
        f2 = Favorite(user_id=test_user.id, recipe_id=r2.id)
        f3 = Favorite(user_id=test_user.id, recipe_id=r3.id)
        f4 = Favorite(user_id=test_user.id, recipe_id=r4.id)

        db.session.add_all([f1, f2, f3, f4])
        db.session.commit()

        with self.client as c:
            with self.client.session_transaction() as sess:
                sess[CURR_USER_KEY] = test_user.id

        results = parse_search_results(search_results)
        set_favorites(test_user.id, results)

        self.assertEqual(len(results), 20, msg="Results list did not parse correctly")

        self.assertTrue(results[19].favorite, msg="Thai Shrimp Curry favorite did not get set to True")
        self.assertTrue(results[5].favorite, msg="Curry Mayonnaise favorite did not get set to True")
        self.assertTrue(results[13].favorite, msg="Roasted Cashews & Curry Leaves favorite did not get set to True")
        self.assertTrue(results[14].favorite, msg="Vegan Chickpea Coconut Curry favorite did not get set to True")

        self.assertFalse(results[0].favorite, msg="A not favorited recipe was set to True")
        self.assertFalse(results[4].favorite, msg="A not favorited recipe was set to True")
        self.assertFalse(results[11].favorite, msg="A not favorited recipe was set to True")