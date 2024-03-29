from Base import Base
import random
import numpy as np
##NN
from random import randint
## Tepl
import random

class Mutation(Base):

    def binary_mutation(self, ar, **kwargs):
        """
        Входит особь для мутации. Выбирается рандомная позиция разделения на части.
        Части меняются местами.
        :param ar: крассовер
        :return: мутированная особь
        """
        tmp = np.array(ar)
        position = random.randint(0,tmp.shape[1]-1)
        for i in range(tmp.shape[0]):
            if tmp[i, position] == 0:
                tmp[i ,position] = 1
            else:
                tmp[i, position] = 0
        return tmp


    def transposition_mutation_Man(self, ar, **kwargs):
        """
        перестановка
        :param R: матрица особей, заслуживших право на мутацию (по сути, родителей)
        :return:  матрица мутированных особей
        """
        R = ar
        for i in range(len(R)):
            # список из двух случайно сгенерированных индексов в диапазоне от 0 до длины хромосомы
            j = random.sample(range(len(R[0])),2)
            tmp_1 = R[i][j[0]]
            tmp_2 = R[i][j[1]]
            R[i][j[0]] = tmp_2  # собственно перестановка
            R[i][j[1]] = tmp_1  # собственно перестановка
        return R


    def inversion_Man(self, ar, **kwargs):
        """
        Хромосома делиться на 2 части и затем они меняются местами
        :param R: матрица особей, заслуживших право на мутацию (по сути, родителей)
        :return: матрица мутированных особей
        """
        R = ar
        for i in range(len(R)):
            j = random.sample(range(1, len(R[0])), 1)
            tmp = R[i][:j[0] + 1]
            R[i] = R[i][j[0] + 1:]
            R[i].extend(tmp)
        return R


    def gen_mut_Tepl(self, unit):
        """
        Генная мутация юникода.
        При  длине генокода больше 1, выбирает 2 рандомных гена и меняет их местами
        :param unit: генекод
        :return:
        """
        if len(unit) > 1:
            i, j = 0, 0
            while i == j:
                i, j = random.randint(0, len(unit) - 1), random.randint(0, len(unit) - 1)
            unit[i], unit[j] = unit[j], unit[i]
        return unit

    def chromo_mut_Tepl(self, unit):
        """
        Проводит хромосомную мутацию юнита
        При  длине генокода больше 1,  выбирает отрезок случайной длины,
        меняет порядок генов на противоположный (1234->4321)
        :param unit: генекод
        :return:
        """
        if len(unit) > 1:
            sp = random.randint(0, len(unit) - 2)
            len_mut = random.randint(2, len(unit) - sp)
            b_unit = unit[sp:sp + len_mut]
            unit[sp:sp + len_mut] = b_unit[::-1]
        return unit

    def mut_Tepl(self, ar, **kwargs):
        MUT_PROBABILITY = 20
        new_pop = []
        new_pop = np.array(new_pop)
        unit_n = np.array(unit_n)
        for counter, unit in enumerate(ar):
            i, j = np.random.random((2,))
            if i < MUT_PROBABILITY / 100:
                unit_n = self.gen_mut_Tepl(unit)
            if j < MUT_PROBABILITY / 100:
                unit_n = self.chromo_mut_Tepl(unit)
                np.concatenate((new_pop, unit_n), axis=0)
        print(new_pop)
        return new_pop


    def insertion_deleting_mutation_NN(self, population):
        """
        Замена у особи одного случайно выбранного гена случайно выбранным значением из диапазона всевозможных значений генов
        :param population: массив особей
        :return: измененный массив особей (изменена только 1 особь)
        """
        min_ = 1
        max_ = 10
        chance_to_mutate = 0.05  # probabitity of mutatation
        for i in range(len(population)):
            if chance_to_mutate > random():
                place_to_modify = randint(1, len(population[i]) - 2)
                population[i][place_to_modify] = randint(min_, max_)
        return population

