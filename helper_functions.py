"""Wild Carrot helper functions"""

from models import RecipeResult
from json import loads

def parse_search_results(search):
    """Parses 'search' and returns list of RecipeResult objects
    Converts 'search' to JSON if not already"""

    if isinstance(search, str):
        py_search = loads(search)
    else:
        py_search = search
    results = []

    for recipe in py_search["hits"]:
        result = RecipeResult(
            name=recipe["recipe"]["label"],
            image=recipe["recipe"]["images"]["REGULAR"]["url"])
        results.append(result)
    
    return results