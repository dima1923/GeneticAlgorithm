from Base import Base
from sklearn.metrics import pairwise_distances
from numpy import unravel_index
import numpy as np
from numpy.random import default_rng

class Selection(Base):
    def truncation_selection(self):
        pass

    def elite_selection(self):
        pass

    def displacement_selection(self):
        pass

    def annealing_selection(self):
        pass

    def tournament_selection(self, population, fitness):
        ans = np.empty(shape=(2,population.shape[1]))
        for i in range(0,2):
            tmp = np.array(population)
            default_rng().shuffle(tmp)
            tmp = tmp[:self.kwargs['t']]
            position = fitness(population=tmp).argmax()
            ans[i] = tmp[position]
        return ans
