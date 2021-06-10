"""Records scopes for each recipe"""

def add(recipe, correct):
    with open('scores.txt', 'a') as fd:
        print('%s %s' % (correct, recipe.name), file=fd)
