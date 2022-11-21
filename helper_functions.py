"""Wild Carrot helper functions"""

from models import RecipeResult, RecipeInfo, User
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
        result = RecipeInfo(recipe)
        # result = RecipeInfo(
        #     name=recipe["recipe"]["label"],
        #     image=recipe["recipe"]["images"]["REGULAR"]["url"],
        #     id=RecipeInfo.get_recipe_id(recipe))
        results.append(result)
    
    return results

def get_recipe_id(recipe):
    """Returns Edamam recipe id from a single 'recipe' from API results 'hits' list.
    Used by parse_search_results"""
    start = 38
    end = recipe["_links"]["self"]["href"].index("?")
    id = recipe["_links"]["self"]["href"][start:end]

    return id

def set_favorites(user_id, recipes):
    """sets 'favorite' attribute of each obeject in 'recipes' list"""

    user = User.query.get(user_id)
    user_favorites = [recipe.edamam_id for recipe in user.favorites]

    for recipe in recipes:
        if recipe.edamam_id in user_favorites:
            recipe.favorite = True