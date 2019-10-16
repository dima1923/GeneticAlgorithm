from Base import Base
import numpy as np
import math
from numpy import exp, average

## import time

class Fitness(Base):
    def my(self, population, **kwargs):
        return average(exp(population), axis=1)

    @staticmethod
    def summ_rasst_Man(individ, distant):
        """
        функция расчета суммы расстояний между городами для каждой особи
        :param individ: массив сгенерированных особей
               distant: матрица расстояний (массив)
        :return: массив сумм растояний между городами для каждой особи
        """
        s = []
        for i in range(len(individ)):
            summ = 0
            for j in range(len(individ[0]) - 1):
                if j != len(individ[0]):
                    summ += distant[individ[i][j] - 1][individ[i][j + 1] - 1]
            s.append(summ)
        return s

    def prisp_1_Man(self, sum_rasst_Man):
        """
        1-ая функция расчета приспособленности
        ФП1 = 1.1 * (максимальное знаение суммы расстояний) - (i-ое значение суммы расстояний)
        :param sum_rasst: массив сумм растояний между городами для каждой особи
        :return: массив результатов подсчетов приспособленности каждой особи
        """
        z = []
        for i in range(len(sum_rasst_Man)):
            prisp = 1.1 * max(sum_rasst_Man) - sum_rasst_Man[i]
            z.append(prisp)
        z = np.around(z, decimals=5)
        return z

    def prisp_2_Man(self, sum_rasst_Man):
        """
        2-ая функция расчета приспособленности
        ФП2 = exp( (- i-ое значение суммы расстояний) / (масимальное значение суммы расстояний))
        :param sum_rasst: массив сумм растояний между городами для каждой особи
        :return: массив результатов подсчетов приспособленности каждой особи
        """
        z = []
        for i in range(len(sum_rasst_Man)):
            prisp = math.exp((- sum_rasst_Man[i]) / max(sum_rasst_Man))
            z.append(prisp)
        z = np.around(z, decimals=5)
        return z

"""
    def fitness_f_Tepl(self, data, unit):
        
        Расчет фитнесс-функции для каждого юнита
        Суммарное значение фитнесс-функций по таблице ценностей
        :param data: таблица ценности
        :param unit: конкретная особь
        :return:
        
        sum = 0
        for c, u in enumerate(unit):
            sum += data.item((c, u - 1))
        return sum
"""

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

