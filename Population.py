from Base import Base
import numpy as np
## Tepl
from operator import itemgetter
## Man
import pandas as pd
import math
import random

class Population(Base):

    #dmitry
    def elite_selection(self, parents, population, generator, fitness, sizeOfPopulation, **kwargs):
        """
        Берем все особи из родителей и потомков.
        На основе приспособленности отбираем лучших. Из них берем 20%
        :return:
        """
        tmp = np.concatenate((parents, population), axis=0)
        fitness_sort = np.argsort(fitness(population=tmp))[-1:-int(np.ceil(sizeOfPopulation*0.2)):-1]
        return np.concatenate([tmp[fitness_sort, :],
                               generator(int(np.floor(sizeOfPopulation*0.8)), population.shape[1])],
                              axis=0)


    # функция отбирает самых лучших особей из старого поколения в количестве не более 10% от общего объема популяции
    def Elite_Man(self, individs, fitness, data):
        indivs = individs
        F = fitness(population=individs, data=data)
        n = math.floor(len(F) * 0.1)
        elites = []
        while len(elites) < n:
            index = F.index(min(F))
            elites.append(indivs.pop(index))
            F.pop(index)
        return elites

    def NewGen_Man(self, parents, population, fitness, data, generator,  **kwargs):
        elite = self.Elite_Man(parents, fitness, data)
        new_population = generator(math.ceil(len(parents)*0.9),len(parents[0]))
        for os in elite:
            new_population.append(os)
        return new_population


    def generate_new_population_Tepl(self, pop, new_pop,fitness, data, sizeOfPopulation):
        """
        :param pop: массив со старым поколением
        :param new_pop: массив с мутированным поколением
        :param data: таблица ценности
        :return:
        """
        output = np.arange(sizeOfPopulation * len(pop[0])).reshape((sizeOfPopulation, len(pop[0])))
        middle = np.arange(2 * sizeOfPopulation * (len(pop[0]) + 1)).reshape((2 * sizeOfPopulation, len(pop[0]) + 1))
        for c, v in enumerate(pop):
            v = np.append(v, fitness(data, v))
            middle[c] = v
        for c, v in enumerate(new_pop):
            v = np.append(v, fitness(data, v))
            middle[c + sizeOfPopulation] = v
        middle = sorted(middle, key=itemgetter(len(pop[0])))
        middleR = np.array([np.array(midi) for midi in middle])
        output = middleR[sizeOfPopulation:, :len(pop[0])]
        return output