"""Runs a quiz"""

import random

import recipe
import score

def run():
    recipes = recipe.load()
    todo = list(recipes.keys())
    scores = score.read()
    score.show_order(scores)
    while True:
        name = score.select_next(scores)
        drink = recipes[name]
        answer = input('Drink: %s (return to show)' % drink.name)
        print(drink.get_detail(1))
        print()
        answer = input('Did you get it right? y/n: ')
        correct = answer.lower() == 'y'
        score.add(drink, correct)
        print()
