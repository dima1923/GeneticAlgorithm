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


    def generate_new_population_Tepl(self, parents, population, fitness, sizeOfPopulation, data, generator,  **kwargs):
        """
        :param pop: массив со старым поколением
        :param new_pop: массив с мутированным поколением
        :param data: таблица ценности
        :return:
        """
        #out_put = np.arange(sizeOfPopulation * len(parents[0])).reshape((sizeOfPopulation, len(parents[0])))
        parents=np.array(parents)
        population=np.array(population)
        print(parents.shape)
        print(population.shape)
        tmp = np.concatenate((parents, population), axis=0)
        fitness_sort = np.argsort(fitness(population=tmp, data=data))[-1:-int(np.ceil(len(parents))):-1]
        np.concatenate([tmp[fitness_sort, :],
                        generator(int(np.floor(sizeOfPopulation * 0.8)), population.shape[1])],
                       axis=0)
        return np.concatenate([tmp[fitness_sort, :],
                               generator(int(np.floor(sizeOfPopulation*len(parents[1]))), population.shape[1])],
                              axis=0)