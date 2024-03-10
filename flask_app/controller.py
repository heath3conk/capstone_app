from flask import Flask, Blueprint, request

import recipe_api

app = Flask(__name__)
main = Blueprint("main", __name__)

# input-ingredients route
@main.route("/recipes", methods=["GET"])
def recipes():
    terms = request.get_json()
    ingredients = terms["ingredient-list"]
    time_spent = terms["minutes"]
    response_df = recipe_api.get_recipes(ingr=ingredients, time=time_spent)
    # sort recipes by number of ingredients
    # return top 3? 5? as list of names to start with
    # 
       
    
    return "hello", 200

# recipes API route
@main.route("/ingredient-substitution", methods=["GET"])
def ingredient_substitution():
    return {"recipeList": ["recipe 1", "recipe 2", "recipe 3", "recipe 4"]}


if __name__ == "__main__":
    app.run(port=5005, debug=True)