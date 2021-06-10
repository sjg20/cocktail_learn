"""Holds recipes"""

class Recipe:
    def __init__(self, name):
        self.name = name
        self.detail = []
        
    def add(self, line):
        self.detail.append(line.strip())
    
    def get_detail(self, indent):
        istr = '   ' * indent
        return istr + ('\n' + istr).join(self.detail)
    
    
def load():
    recipes = {}
    recipe = None
    with open('recipes.db') as fd:
        for line in fd.readlines():
            line = line.rstrip()
            if line:
                if line[0] != ' ':
                    recipe = Recipe(line)
                else:
                    recipe.add(line)
            else:
                recipes[recipe.name] = recipe
                recipe = None
        if recipe:
            recipes[recipe.name] = recipe
    return recipes
