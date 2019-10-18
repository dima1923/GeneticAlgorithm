from Base import Base
import numpy as np
## Tepl
from operator import itemgetter
## Man
import pandas as pd
import math

class Population(Base):

    #dmitry
    def elite_selection(self, parents, population, generator, fitness, sizeOfPopulation, **kwargs):
        tmp = np.concatenate((parents, population), axis=0)
        fitness_sort = np.argsort(fitness(population=tmp))[-1:-int(np.ceil(sizeOfPopulation*0.2)):-1]
        return np.concatenate([tmp[fitness_sort, :],
                               generator(int(np.floor(sizeOfPopulation*0.8)), population.shape[1])],
                              axis=0)


    def generate_new_population_Tepl(self, pop, new_pop,fitness, data, sizeOfPopulation):
        """
        Создание новой популяции.
        Заполняем таблицу middle элементами pop/new_pop и добавляем столбец значений фитнес-функции каждого юнита
        Все юниты упорядочиваются по уменьшению значений своих ФФ
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



    # функция отбирает самых лучших особей из старого поколения в количестве не более 10% от общего объема популяции
    def Elite_Man(self, individs, Fit_Man):
        indivs = individs
        F = Fit_Man(individs, distant)
        n = math.floor(len(F) * 0.1)
        elites = []
        while len(elites) < n:
            index = F.index(min(F))
            elites.append(indivs.pop(index))
            F.pop(index)

        return elites

    def NewGen(self, indivs, elites, inver_prob):
        method = 'prob'
        new_generation = []

        for i in elites:
            indivs.remove(i)
        resid = len(indivs)

        F = indivs[len(indivs.columns) - 1]

        ind = indivs.drop(len(indivs.columns) - 1, 1)
        ind = ind.values.tolist()

        elites = pd.DataFrame(elites)
        elites = elites.drop(len(elites.columns) - 1, 1)
        elites = elites.values.tolist()
        new_generation.extend(elites)

        if method == 'prob':
            mutation_list = []
            for i in range(resid):
                a = random.choices(ind, weights=F)
                mutation_list.append(a[0])

            mut_ind = Mutation(mutation_list)
            mut_ind = mut_ind.values.tolist()
        elif method == 'tour':
            ind = pd.DataFrame(ind)
            ind['Fitness'] = F
            mutation_list = Tournament(ind, resid)
            mutation_list = mutation_list.drop(len(mutation_list.columns) - 1, 1)
            mutation_list = mutation_list.values.tolist()
            mut_ind = Mutation(mutation_list)
            mut_ind = mut_ind.values.tolist()
        elif method == 'roul':
            ind = pd.DataFrame(ind)
            ind['Fitness'] = F
            mutation_list = Roulette(ind, resid)
            mutation_list = mutation_list.drop(len(mutation_list.columns) - 1, 1)
            mutation_list = mutation_list.values.tolist()
            mut_ind = Mutation(mutation_list)
            mut_ind = mut_ind.values.tolist()

        if inver_prob != 0:
            inver_list = []
            for i in mut_ind:
                j = random.random()
                if j <= inver_prob:
                    inver_list.append(i)
            for i in inver_list:
                mut_ind.remove(i)

            inver_ind = Inver(inver_list).values.tolist()

        new_generation.extend(mut_ind)
        new_generation.extend(inver_ind)

        return pd.DataFrame(new_generation)
