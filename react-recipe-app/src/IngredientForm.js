import React, { useState } from 'react'

function IngredientForm({ findRecipes }) {

    const [ingredientList, setIngredientList] = useState();
    const [minutes, setMinutes] = useState();

    const handleSubmit = (e) => {
        findRecipes([ingredientList, minutes])
        e.preventDefault();
    }

    return (
        <div className="ingredient-form">
            <h1>Enter some information to get recipe suggestions:</h1>
            <form onSubmit={e => {handleSubmit(e)}}>
                <label>What are some ingredients you have on hand?</label>
                <br />
                <input 
                name="ingredient-list"
                placeholder="enter one or more ingredients, separated by commas"
                type="text"
                value={ingredientList}
                onChange={e => setIngredientList(e.target.value)}
                />
                <br/>
                <label>How much time do you have to cook?</label>
                <br />
                <input 
                name="max-minutes" 
                placeholder="enter number of minutes"
                type="text"
                value={minutes}
                onChange={e => setMinutes(e.target.value)}
                />
                <br />
                <input className="submitButton" type="submit" value="Find Recipes"
                />
            </form>
        </div>
    )
}

export default IngredientForm