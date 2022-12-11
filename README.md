Wild Carrot

https://wildcarrot.herokuapp.com

Goals
My website helps users find recipe ideas based on flavors or ingredients they like.  Optionally, users can select dietary restrictions (vegan, gluten-free, etc.)  Users can create a profile and select favorite recipes for easy retrieval and viewing.

Target Demographic
The target demographic is pretty broad:  anyone who enjoys finding and cooking new recipes.  

API
I will be using the Edamam API.  The documentation is at https://developer.edamam.com/edamam-docs-recipe-api.  Eamam’s API provides the search function and each recipe in the results contains a lot of detail:  ingredients, cooking instructions, dietary restrictions, nutrition information, just to name a few.

Outline
The main (home) page has a single text area for entering keywords for ingredients or flavors.  Below that is a list of checkboxes for dietary restrictions.  No login is required to use the search feature.  After searching, the results page will show approximately 20 recipe titles and preview pictures (the API provides a image link in its response).  At the bottom will be a button or link to display the next page of results.  Clicking on a recipe displays all of the details about that recipe:  primarily ingredients and instructions.  If a user is logged in they will be able to tag recipes as a favorite and they can view a list of their favorites.

Database Schema
-Users
   -username
   -password (will need to be stored hashed)
-Favorites
   -user id
   -recipe id
-user_favorites
   -Many to many relationship between favorites and users
-Recipe
   -edamam_id
   -name
   -image
 
 Technology Stack
 -Backend
   -Flask
   -SQLAlchemy
   -Postgresql
   -Jinja
  FrontEnd
   -JQuery
