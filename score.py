"""Records scopes for each recipe"""

import random


class Score:
    def __init__(self, name):
        self.name = name
        self.right = 0
        self.wrong = 0

    def add(self, correct):
        if correct:
            self.right += 1
        else:
            self.wrong += 1

    def priority(self):
        """Return the priority of asking about this drink

        Returns
            priority (int): the lower the value, the more important
        """
        return self.right - self.wrong

    def __str__(self):
        return '%s (%d/%d)' % (self.name, self.right, self.wrong)


def add_score(scores, drink, correct):
    """Add a new score to our records

    Args:
        Scores: dict:
            key: drink
            value: Score object
        drink: Name of drink to add
        correct: True if correct, False if wrong
    """
    score = scores.get(drink)
    if not score:
        score = Score(drink)
        scores[drink] = score
    score.add(correct)


def add(scores, recipe, correct):
    add_score(scores, recipe.name, correct)
    with open('scores.txt', 'a') as fd:
        print('%s %s' % (correct, recipe.name), file=fd)


def read(recipes):
    """Read in the scores from previos tests

    Args:
        recipes: list of recipe names
    """
    scores = {}
    with open('scores.txt') as fd:
        for line in fd.readlines():
            line = line.strip()
            correct, drink = line.split(maxsplit=1)
            if drink not in recipes:
                print("Score for unknown recipe '%s'" % drink)
            add_score(scores, drink, correct == 'True')

    # add drinks that have not been asked yet
    for drink in recipes:
        if drink not in scores:
            scores[drink] = Score(drink)

    return scores


def get_ordered(scores):
    """Get scores ordered so those answered correctly appear at the end

    Returns:
        Ordered dict of scores
            key: name
            value: Score object
    """
    return sorted(scores, key=lambda name: scores[name].priority())


def show_order(scores):
    ordered = get_ordered(scores)
    total = 0
    for recipe in ordered:
        total += scores[recipe].priority()

    for recipe in ordered:
        asked_proportion = scores[recipe].priority() / total
        print('%-15s %1.1f' % (recipe, asked_proportion * 100))


def select_next(scores):
    ordered = get_ordered(scores)
    todo = list(ordered)
    #select = random.randrange(len(ordered) // 2)
    #select = int(random.triangular(0, len(todo), 0))
    select = int(random.betavariate(.5, 5) * len(todo))
    return todo[select]
