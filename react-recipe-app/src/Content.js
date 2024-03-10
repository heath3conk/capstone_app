import React, { useState } from 'react'
import RecipeList  from './RecipeList'
import IngredientForm from './IngredientForm'

function Content(props) {

    const [recipeSearch, setRecipeSearch] = useState([])
    const findRecipes = (search) => {
        let searches = [...recipeSearch, search];
        setRecipeSearch(searches)
    }


    return (
        <main>
            <section>
                <IngredientForm findRecipes={findRecipes}/>
                <RecipeList />
            </section>
        </main>
    ) 
}

export default Content
