#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # Edge case - check to see if ingredients dict has all of the keys from recipe dict
    # if not, return 0
    for key in recipe:
        if key in ingredients.keys():
            return 0

    # General case...

    # batches = 0
    # Loop through each key in recipe
    # if recipe[key] <= ingredients[key]:
    #    b_ingrediants = math.floor(ingredients[key] / recipe[key])
    #    if b_ingrediants < batches or batches == 0:
    #       batches = b_ingrediants
    # else return 0
    pass


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
    pass
# print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
#     'milk': 1288, 'flour': 9, 'sugar': 95}))
