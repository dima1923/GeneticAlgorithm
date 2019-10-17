from Base import Base
import random
from random import randint
import numpy as np

class Crossover(Base):
    def empty(self, parents):
        return parents

    def density_crossover(self):
        pass

    def intermediate_crossover(self):
        pass

    def linear_crossover(self):
        pass


    def single_point_crossover(self, parents:np.ndarray, **kwargs):
        """
        Из родителей рандомно выбираются 2 особи. Определяется точка разрыва (случайным образом).
        Потомок определяется как конкатенация части первого и второго родителя.
        Меняются частями с выбранной точкой раздела.
        :param parents: все родители
        :return: потомки
        """
        tmp = np.empty(shape=parents.shape)
        j = 0
        while parents.shape[0] != 0:
            index_of_parent = random.sample([i for i in range(parents.shape[0])],2)
            point = int(parents.shape[1] / 2)
            while (point == int(parents.shape[1] / 2)):
                point = random.randint(0, parents.shape[1])
            tmp[j] = np.concatenate((parents[index_of_parent[0], 0:point],parents[index_of_parent[1], point:]), axis=None)
            j += 1
            tmp[j] = np.concatenate((parents[index_of_parent[1], 0:point], parents[index_of_parent[0], point:]), axis=None)
            j += 1
            parents = np.delete(parents, index_of_parent, 0)
        return tmp

    def double_point_crossover(self):
        pass

    def multipoint_crossover(self):
        pass

    def uniform_crossover(self):
        pass

    def process_crossover(self):
        pass

    def shuffle_crossover(self):
        pass

    def replacement_crossover(self):
        pass
    
    def crossover_NN(self, p1, p2):
        """
        Хромосома ребенка наследует в вероятностью 50/50 ген одного из родителей.
        Если длина хромосомы будет наследована от большего родителя, то недостающие
        гены будут также унаследованы у этого родителя
        :param p1: хромосома 1 родителя
        :param p2: хромосома 2 родителя
        :return: хромосома наследника (наследников?)
        """
        MainPos=2
        def error__NN(p1, p2, pos):
            if not (isinstance(p1, list) and isinstance(p2, list)):
                raise ArithmeticError("one or both from parents not list")
            if (pos > len(p1) or pos > len(p2)):
                raise ArithmeticError("this position %d out of range parent's lists")
        def randBol_NN(b=1):
            return randint(0, b)
        def introduction_NN(p1, p2, pos):
            child = list()
            if pos != 0:
                for i in range(0, pos):
                    child.append(p2[i] if randBol_NN() else p1[i])
            return child
        def adder_NN(a, b):
            child.append(a if randBol_NN() else b)
            return len(child)

        error(p1, p2, MainPos)
        child = introduction_NN(p1, p2, MainPos)
        if (p2[MainPos] - p1[MainPos] < 0):
            p = p1.copy()
            p1 = p2.copy()
            p2 = p
        pos = adder_NN(p2[MainPos], p1[MainPos])
        for i in range(pos, p1[MainPos] + pos):
            pos = adder_NN(p2[i], p1[i])
        if child[MainPos] == p2[MainPos]:
            child += p2[pos:]
        return child
