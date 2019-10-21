from Base import Base
import numpy as np
import math
from numpy import exp, average

## import time

class Fitness(Base):
    def my(self, population, **kwargs):
        """
        Приспособленность каждой. Каждую из популяции возводим в экспоненту и берем среднее из экспонент.
        :param population: массив особей
        :return: приспособленность всей популяции
        """
        return average(exp(population), axis=1)


    def Fit_Man(self, population, data, **kwargs):
        """
        Рассчитываем приспособленность каждой особи, как сумму расстояний между городами.
        :param individ: массив сгенерированных особей
               distant: матрица расстояний (массив)
        :return: массив сумм растояний между городами для каждой особи
        """
        s = []
        for i in range(len(population)):
            summ = 0
            for j in range(len(population[0]) - 1):
                if j != len(population[0]):
                    summ += data[int(population[int(i)][int(j)] - 1)][int(population[int(i)][int(j + 1)] - 1)]
            s.append(summ)
        return s


    def fitness_f_Tepl(self, population, data, **kwargs):
        """
        Расчет фитнесс-функции для каждого юнита
        Суммарное значение фитнесс-функций по таблице ценностей
        :param data: таблица ценности
        :param unit: конкретная особь
        :return:
        """
        fit = []
        for unit in population:
            sum = 0
            for c, u in enumerate(unit):
                sum += data.item((c, u - 1))
            fit.append(sum)
        return fit


""" NN

    def fitness_indiv(indiv):
        res_of_train = train_and_score(indiv)
        return res_of_train[0] * indiv[1] + (1 - indiv[1]) * res_of_train[1]

    def fitness_population(population):
        start_time = time.time()

        population_fitness = []
        for item in population:
            population_fitness.append(fitness_indiv(item))

        end_time = time.time()
        print("Process take {0}  seconds ".format(end_time - start_time))

        return population_fitness
"""

