from Base import Base
from sklearn.metrics import pairwise_distances
from numpy import argmin

class Selection(Base):
    def truncation_selection(self):
        pass

    def elite_selection(self):
        pass

    def displacement_selection(self):
        pass

    def annealing_selection(self):
        pass

    def my_imbreading(self, population, metric='euclidean'):
        distance = pairwise_distances(population, metric=metric)
        indexes = argmin(distance)
        return population[indexes, :]