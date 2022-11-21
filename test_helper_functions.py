from unittest import TestCase
from helper_functions import parse_search_results, get_recipe_id
from testing_data import search_results, single_recipe
from json import loads
from models import RecipeInfo


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