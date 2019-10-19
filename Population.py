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

    """
    def generate_new_population_Tepl(self, pop, new_pop,fitness, data, sizeOfPopulation):
        
        :param pop: массив со старым поколением
        :param new_pop: массив с мутированным поколением
        :param data: таблица ценности
        :return:
        
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
    """


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

    def NewGen_Man(self, parents, population, fitness, data, **kwargs):
        new_generation = []
        method = 'prob'
        method = 'tour'

        elites = self.Elite_Man(population, fitness, data)
        indivs = population
        for i in elites:
            indivs.remove(i)  # Удаляем тех особей, которые были признаны Элитными
        resid = len(indivs)  # Записываем в переменную resid количество оставленных особей
        F = fitness(indivs)  # список с приспособленностями
        new_generation.extend(elites)  # Добавляем список из элитных особей в новое поколение

        if method == 'tour':  # Проверяем условие на метод
            mutation_list = parents(indivs, F)
            mutation_list = mutation_list.drop(len(mutation_list.columns) - 1,
                                               1)  # Убираем столбец с приспособленностью из DataFrame
            mutation_list = mutation_list.values.tolist()  # Переводим DataFrame в список
            mut_ind = Mutation(mutation_list)  # Производим мутацию выбранных особей
            mut_ind = mut_ind.values.tolist()

        elif method == 'roul':  # Проверяем условие на метод
            ind = pd.DataFrame(ind)  # Переводим список в DataFrame
            ind['Fitness'] = F  # Добавляем столбец Fitness с приспособленностями
            mutation_list = Roulette(ind, resid)  # Добавляем особей в DataFrame на мутацию по методу отбора "Рулетка"
            mutation_list = mutation_list.drop(len(mutation_list.columns) - 1,
                                               1)  # Убираем столбец с приспособленностью из DataFrame
            mutation_list = mutation_list.values.tolist()  # Переводим DataFrame в список
            mut_ind = Mutation(mutation_list)  # Производим мутацию выбранных особей
            mut_ind = mut_ind.values.tolist()  # Переводим DataFrame в список

        if inver_prob != 0:  # Проверяем условие на инверсию
            inver_list = []
            for i in mut_ind:
                j = random.random()  # Получаем случайное число от 0 до 1
                if j <= inver_prob:  # Проверяем условие
                    inver_list.append(i)  # Если число меньше или равно вероятности, то добавляем в список на инверсию
            for i in inver_list:
                mut_ind.remove(i)  # Удаляем тех особей из списка mut_ind, которые будут подвержены инверсии

            inver_ind = Inver(inver_list).values.tolist()  # Производим инверсию выбранных особей

        new_generation.extend(mut_ind)  # Добавляем список из мутировавших особей в новое поколение
        new_generation.extend(inver_ind)  # Добавляем список из особей, подвергнувшихся и

        return pd.DataFrame(new_generation)