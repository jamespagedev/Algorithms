#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Edge case - check to see if ingredients dict has all of the keys from recipe dict
    # if not, return 0
    for key in recipe:
        if key not in ingredients.keys():
            return 0

    # General case...

    batches = 0
    for key, r_value in recipe.items():
        if r_value <= ingredients[key]:
            b_ingrediants = math.floor(ingredients[key] / r_value)
            if b_ingrediants < batches or batches == 0:
                batches = b_ingrediants
        else:
            return 0
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
    pass
