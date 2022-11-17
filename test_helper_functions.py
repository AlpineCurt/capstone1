from unittest import TestCase
from helper_functions import parse_search_results
from testing_data import search_results


class ParseSearchResultsTestCase(TestCase):
    """Test Parsing of Search Results"""

    def test_parse_search_results(self):
        """Does the function pull the correct data from search results?"""

        results = parse_search_results(search_results)

        self.assertEqual(len(results), 20, msg="Results does not have expected 20 objects")
        self.assertEqual(results[0].name, "Cauliflower and Tofu Curry Recipe", msg="Name of recipe is incorrect.")
        self.assertEqual(results[0].image[:4], "http", msg="Image is not a url")