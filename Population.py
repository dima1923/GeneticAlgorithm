from Base import Base
import numpy as np

class Population(Base):
    def truncation_selection(self):
        pass

    def elite_selection(self, parents, population, generator, fitness):
        tmp = np.concatenate((parents, population), axis=0)
        fitness_sort = np.argsort(fitness(population=tmp))[-1:-int(population.shape[0]*0.1):-1]
        return np.concatenate([tmp[fitness_sort, :],
                               generator(int(population.shape[0]*0.9), population.shape[1])],
                              axis=0)

    def displacement_selection(self):
        pass

    def annealing_selection(self):
        pass
