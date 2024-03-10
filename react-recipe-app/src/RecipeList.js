import React, { useState, useEffect } from 'react'

function RecipeList() {  
    const [recipes, setRecipes] = useState([{}])

    useEffect(() => {
        fetch("/recipes").then(  // fetches the route from our app
        res => res.json()  // turns the response into json
        ).then(
        recipeList => {  // accessing the recipes in the json object
            setRecipes(recipeList)   // sets the data from json to the recipes variable
            console.log(recipes)
        }
        )
    }, [])  // passing empty array here means this `useEffect` block only runs once



  return (
    <div className="recipe-results">
        <h1>We found these recipes: </h1>
        <div>
            {(typeof recipes.recipeList === "undefined") ? (  // check to see if we have data from the backend yet
            <p> Loading ... </p>  // if not, display this
            ): (
                recipes.recipeList.map((recipe, i) => (  // once we have the list of recipes, map the recipe & its index
                <p key={i}>{recipe}</p>  // display each element of the list, setting its index as the "key"
                ))
            )}  
        </div>
    </div>
  )
}

export default RecipeList