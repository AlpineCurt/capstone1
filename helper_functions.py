"""Wild Carrot helper functions"""

from models import RecipeResult, RecipeInfo, User, SearchPref
from json import loads
from forms import SearchForm
from secrets_ import edamam_app_id, edamam_app_key

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

def build_search_params(request_args):
    """Retturns a dictionary of request parameters based on request_args"""

    params = {
        "type": "public",
        "q": request_args.get('q'),
        "app_id": edamam_app_id,
        "app_key": edamam_app_key,
        "diet": [],
        "health": [],
        "cuisineType": []
    }

    for req in request_args:
        if req in SearchPref.diets:
            params["diet"].append(req.replace('_', '-'))
        elif req in SearchPref.health:
            params["health"].append(req.replace('_', '-'))
        elif req in SearchPref.cuisines:
            params["cuisineType"].append(req.replace('_', ' '))

    return params

def valid_params(params):
    """checks params dict to make sure at least one search
    criteria has been submitted.  Returns False if not."""

    q = True if params['q'] != '' else False
    diet = True if params['diet'] != [] else False
    health = True if params['health'] != [] else False
    cuisine = True if params['cuisineType'] != [] else False

    return q or diet or health or cuisine

def set_modify_search_form(params):
    """Returns a SearchForm object with values of fields
    set according to params dict"""

    form = SearchForm()
    
    for key, value in params.items():
        if key == 'q':
            form['q'].data = value
        else:
            form[key].data = True
    
    return form