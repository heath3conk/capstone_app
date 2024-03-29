import json
import requests

import pandas as pd


with open("../secrets.json", "rb") as f:
    key_file = json.loads(f.read())

APP_ID = key_file["app_id"]
APP_KEY = key_file["key"]


def get_recipes(ingr: list[str], time: int, dish: str="Main course", meal: str="Dinner"):
    recipes_endpoint = "https://api.edamam.com/api/recipes/v2?type=public"
    ingredients = f"q={'%2C%20'.join(ingr)}"  # TODO: handle empty `ingr` list
    
    num_ingr = (len(ingr), 10)
    min_max_ingr = f"ingr={min(num_ingr)}-{max(num_ingr)}"
    time_spent = f"time=0-{time}" # TODO: handle empty `time` value
    dish_type=f"dishType={dish}"
    meal_type = f"mealType={meal}"
    full_url = f"{recipes_endpoint}&{ingredients}&{min_max_ingr}&{dish_type}&{meal_type}&{time_spent}&app_id={APP_ID}&app_key={APP_KEY}"
    response = requests.get(full_url)
    data = response.json()
    print(response.status_code)
    
    if response.status_code == 200 and data["count"] > 0:
        items = []
        for item in data["hits"]:
            recipe_dict = {}
            recipe_dict["title"] = item["recipe"]["label"]
            recipe_dict["link"] = item["recipe"]["url"]
            recipe_dict["servings"] = item["recipe"]["yield"]
            recipe_dict["cuisine"] = item["recipe"]["cuisineType"]
            recipe_dict["diet_labels"] = item["recipe"]["dietLabels"]
            recipe_dict["healh_labels"] = item["recipe"]["healthLabels"]
            recipe_dict["cautions"] = item["recipe"]["cautions"]
            recipe_dict["ingredient_lines"] = item["recipe"]["ingredientLines"]
            
            ingred_labels =[]    
            ingreds = []
            for ingr in item["recipe"]["ingredients"]:
                ingredient_details = {}
                ingredient_details["text"] = ingr["text"]
                ingredient_details["quantity"] = ingr["quantity"]
                ingredient_details["measure"] = ingr["measure"]
                ingredient_details["weight"] = ingr["weight"]
                ingredient_details["food"] = ingr["food"]  # adds "food" label to the "ingredient details" dict
                ingredient_details["food_category"] = ingr["foodCategory"]
                ingreds.append(ingredient_details)
                recipe_dict["ingredient_details"] = ingreds
                
                ingred_labels.append(ingr["food"])  # adds "food" label to list of ingredients
                recipe_dict["ingredient_labels"] = ingred_labels
            items.append(recipe_dict)
    return pd.DataFrame.from_dict(items)

    