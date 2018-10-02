import numpy
import math


class UCB1():
    def __init__(self, counts=[], values=[]):
        self.counts = counts
        self.values = values

    def __repr__(self):
        return ("UCB1({!r}{!r})".format(self.counts, self.values))

    def initialize(self, n_arms):
        self.counts = [0 for col in range(n_arms)]
        self.values = [0.0 for col in range(n_arms)]

    def select_arm(self):
        n_arms = len(self.counts)

        '''
        Following few lines of code ensure ensure UCB does not have a cold start before it starts to 
        apply its confidence based decision rule'''
        for arm in range(n_arms):
            if self.counts[arm] == 0:
                return arm

        ucb_values = [0.0 for arm in range(n_arms)]
        total_counts = sum(self.counts)
        for arm in range(n_arms):
            bonus = math.sqrt(2 * math.log(total_counts)) / float(self.counts[arm])
            ucb_values[arm] = self.values[arm] + bonus

        '''
            The most basic statement that can be made about it is that it augments the estimated value of any arm with a 
            measure of how less about that arm than we know about the arms.
            These rescaling terms allow the algorithm to define a confidence interval that has a reasonable chance of 
            containing the true value of the arm inside of it. UCB creates its ucb_values by replacing every arm's estimated
            value with the upper bound on the confidence interval for its value.r

        '''
        return ucb_values.index(max(ucb_values))

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]

        value = self.values[chosen_arm]
        new_value = ((n - 1) * value + reward) / float(n)
        self.values[chosen_arm] = new_value
