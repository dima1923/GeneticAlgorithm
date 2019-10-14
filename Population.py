from Base import Base
import numpy as np

class Population(Base):
    def truncation_selection(self):
        pass


    #dmitry
    def elite_selection(self, parents, population, generator,
                        fitness, sizeOfPopulation, **kwargs):
        tmp = np.concatenate((parents, population), axis=0)
        fitness_sort = np.argsort(fitness(population=tmp))[-1:-int(np.ceil(sizeOfPopulation*0.2)):-1]
        return np.concatenate([tmp[fitness_sort, :],
                               generator(int(np.floor(sizeOfPopulation*0.8)), population.shape[1])],
                              axis=0)

    def displacement_selection(self):
        pass

    def annealing_selection(self):
        pass
