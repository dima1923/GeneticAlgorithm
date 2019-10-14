from Base import Base
import random
import numpy as np

class Mutation(Base):

    def binary_mutation(self, ar):
        """
        Входит особь для мутации. Выбирается рандомная позиция разделения на части.
        Части меняются местами.
        :param ar: особь для мутации
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

    def density_mutation(self):
        pass

    def real_mutation(self):
        pass

    def gen_mut_ZON(self, unit):
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

    def chromo_mut(self, unit):
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

    def insertion_deleting_mutation_NN(self, population):
        """
        Замена у особи одного случайно выбранного гена случайно выбранным значением из диапазона всевозможных значений генов
        :param population: массив особей
        :return: измененный массив особей (изменена только 1 особь)
        """
        chance_to_mutate = 0.05;  # probabitity of mutatation
        for i in range(len(population)):
            if chance_to_mutate > random():
                place_to_modify = randint(1, len(population[i]) - 2)
                population[i][place_to_modify] = randint(min_, max_)
        return population


# ??????????????????
    def transposition_mutation_Man(self, R):
        """
        перестановка
        :param R: матрица особей, заслуживших право на мутацию (по сути, родителей)
        :return:  матрица мутированных особей
        """
        for i in range(len(R)):
            # список из двух случайно сгенерированных индексов в диапазоне от 0 до длины хромосомы
            j = random.sample(range(len(R[0])),2)
            tmp_1 = R[i][j[0]]
            tmp_2 = R[i][j[1]]
            R[i][j[0]] = tmp_2  # собственно перестановка
            R[i][j[1]] = tmp_1  # собственно перестановка
        list_g = []
        for i in range(len(R[0])):
            list_g.append("gen_{}".format(i + 1))
        return list_g


    def inversion_Man(self, R):
        """
        Хромосома делиться на 2 части и затем они меняются местами
        :param R: матрица особей, заслуживших право на мутацию (по сути, родителей)
        :return: матрица мутированных особей
        """
        for i in range(len(R)):
            j = random.sample(range(1, len(R[0])), 1)
            tmp = R[i][:j[0] + 1]
            R[i] = R[i][j[0] + 1:]
            R[i].extend(tmp)
        return R