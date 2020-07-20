import random
import bisect


class WeightedChoice(object):
    def __init__(self, weights):
        self.totals = []
        self.weights = weights
        running_total = 0

        for w in weights:
            running_total += w[1]
            self.totals.append(running_total)

    def next(self):
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]


def waifu_stats(rarity_list):



rarity_list = (('alpha', 70),
               ('beta', 55),
               ('delta', 30),
               ('epsilon', 18),
               ('gamma', 8),
               ('zeta', 0.05))

weighted_choice = WeightedChoice(rarity_list)
