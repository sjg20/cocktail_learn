"""Records scopes for each recipe"""

import random


class Score:
    def __init__(self, name):
        self.name = name
        self.right = 0
        self.wrong = 0

    def add(self, correct):
        if correct == 'True':
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


def add(recipe, correct):
    with open('scores.txt', 'a') as fd:
        print('%s %s' % (correct, recipe.name), file=fd)


def read():
    scores = {}
    with open('scores.txt') as fd:
        for line in fd.readlines():
            line = line.strip()
            correct, drink = line.split(maxsplit=1)
            score = scores.get(drink)
            if not score:
                score = Score(drink)
                scores[drink] = score
            score.add(correct)
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
    select = random.randrange(len(ordered) / 2)
    return todo[select]
