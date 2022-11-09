Goals
My website will help users find recipe ideas based on flavors or ingredients they like.  Optionally, users can select dietary restrictions (vegan, gluten-free, etc.)  Users will be able to create a profile and select favorite recipes for easy retrieval and viewing.  On their profile, they can set dietary restrictions to be included by default so they will not need to filter results manually.

Target Demographic
The target demographic is pretty broad:  anyone who enjoys finding and cooking new recipes.  

API
I will be using the Edamam API.  The documentation is at https://developer.edamam.com/edamam-docs-recipe-api.  Eamam’s API provides the search function and each recipe in the results contains a lot of detail:  ingredients, cooking instructions, dietary restrictions, nutrition information, just to name a few.

Outline
The main (home) page will have a single text area for entering keywords for ingredients or flavors.  Below will be a list of checkboxes for dietary restrictions.  No login will be required to use the search feature.  After searching, the results page will show approximately 10 recipe titles and preview pictures (the API provides a image link in its response).  At the bottom will be a button or link to display the next 10 results.  I might try to implement infinite scrolling with results.  Clicking on a recipe will display all of the details about that recipe:  primarily ingredients and instructions, but also anything else interesting the API provides.  If a user is logged in they will be able to tag recipes as a favorite and they can view a list of their favorites.

Database Schema
-Users
   -username
   -password (will need to be stored hashed)
-Favorites
   -user id
   -recipe id
-user_favorites
   -Many to many relationship between favorites and users 
