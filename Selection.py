from Base import Base
import numpy as np
from numpy.random import default_rng
import random
from random import randint

class Selection(Base):
    n_osob = 15

    #dmitry
    def tournament_selection(self, population, fitness, **kwargs):
        """
        Рандомно выбираем две особи(без повторения) и сравниваем их приспособленность.
        В новую популяцию поподает та, у которой лучше значение функции приспособленности
        :param: population : массив сгенерированных особей
                fitness : значение приспособленности для всей популяции
        :return: массив новой популяции
        """
        try:
            t = self.kwargs['t']
        except KeyError:
            raise AttributeError
        ans = np.empty(shape=(int(np.ceil(0.9*population.shape[0])),population.shape[1]))
        tmp = np.array(population)
        for i in range(0,int(np.ceil(0.9*population.shape[0]))):
            default_rng().shuffle(tmp)
            position = fitness(population=tmp[:t]).argmin()
            ans[i] = tmp[position]
            tmp = np.delete(tmp, position, 0)
        return ans



    def tournament_selection_Man(self, population, fitness, data, **kwargs):
        """
        Рандомно выбираем две особи(без повторения) и сравниваем их приспособленность.
        В новую популяцию поподает та, у которой лучше значение функции приспособленности
        :param: population : массив сгенерированных особей
                fitness : значение приспособленности для всей популяции
        :return: массив новой популяции
        """
        t = 2
        fitnes = fitness(population=population, data=data)
        turn = []
        for i in range(len(population)):
            choice = []
            for j in range(t):
                x = random.choice(fitnes)
                k = list(fitnes).index(x)
                choice.extend([x, k])
            if choice[t - 2] > choice[t]:
                turn.append(population[int(choice[t - 1])])
            else:
                turn.append(population[int(choice[t + 1])])
        return turn

    def roulette_selection_Man(self, population, fitness, data, **kwargs):
        fitnes = fitness(population= population, data=data)
        total_fit = sum(fitnes)
        rel_fit = [i / total_fit for i in fitnes]
        prob_list = [sum(rel_fit[:i + 1]) for i in range(len(rel_fit))]
        chosen_index = []
        for i in range(len(population)):
            point = random.random()
            index = -1
            for j in prob_list:
                index += 1
                if point <= j:
                    chosen_index.append(index)
                    break
        indivs_1 = population
        chosen_indivs = []
        for i in chosen_index:
            chosen_indivs.append(indivs_1[i])
        return chosen_indivs



    """
    @staticmethod
    def Hamming_distance(individ_1, individ_2):
        
        функция вычисления Хэммингого расстояния
        :param: individ_1, individ_2 : индивидуумы
        :return: количество позиций, в которых индивидуумы отличаются
        
        distance = 0;
        len_1 = len(individ_1)
        len_2 = len(individ_2)
        if (len_1 > len_2):
            for i in range(len_2):
                if i > 1:
                    if (individ_2[i] != individ_1[i]):
                        dis = abs(individ_1[i] - individ_2[i])
                        distance += dis
                else:
                    distance += 1
        else:
            for i in range(len_1):
                if i > 1:
                    if (individ_1[i] != individ_2[i]):
                        dis = abs(individ_1[i] - individ_2[i])
                        distance += dis
                else:
                    distance += 1
        return distance

## вместо двух отдельных родителей возвращает массив из 2 родителей
    def inbreeding_NN(self, population, **kwargs):
        
        функция выбора пары родителей
        первый родитель выбирается случайно, вторым выбирается такой, который наиболее похож на первого
        :param population : массив сгенерированных особей
        :return: массив из двух выбранных родителей
        
        parents = []
        rand_index = randint(0, len(population) - 1)
        parents.append(population[rand_index])
        min_hamming_dist = 99999
        candidates = []
        for i in range(0, len(population)):
            if (i == rand_index):
                continue
            else:
                tmp = self.Hamming_distance(parents[0], population[i])
                if (tmp < min_hamming_dist):
                    min_hamming_dist = tmp
        l = 0
        for j in range(0, len(population)):
            if (self.Hamming_distance(parents[0], population[j]) == min_hamming_dist):
                candidates.append(population[j])
                l += 1
        rand_index_2 = randint(0, l - 1)
        parents.append(candidates[rand_index_2])
        return parents

## вместо двух отдельных родителей возвращает массив из 2 родителей
    def outbreeding_NN(self, population, **kwargs):
        
        функция выбора пары родителей
        первый родитель выбирается случайно, вторым выбирается такой, который наименее похож на первого
        :param population : массив сгенерированных особей
        :return: массив из двух выбранных родителей
        
        parents = []
        rand_index = randint(0, self.n_osob - 1)
        parents.append(population[rand_index])
        max_hamming_dist = 0
        candidates = []
        for i in range(0, len(population)):
            tmp = self.Hamming_distance(parents[0], population[i])
            if (tmp > max_hamming_dist):
                max_hamming_dist = tmp
        l = 0
        for j in range(0, len(population)):
            if (self.Hamming_distance(parents[0], population[j]) == max_hamming_dist):
                candidates.append(population[j])
                l += 1
        rand_index_2 = randint(0, l - 1)
        parents.append(candidates[rand_index_2])
        return parents

## вместо двух отдельных родителей возвращает массив из 2 родителей
    def panmixia_NN(self, population, **kwargs):
        
        функция выбора пары родителей
        оба родителя выбираются случайно, каждая особь популяции имеет равные шансы быть выбранной
        :param population : массив сгенерированных особей
        :return: массив из двух выбранных родителей
        
        parents = []
        rand_index_1 = randint(0, len(population) - 1)
        parents.append(population[rand_index_1])
        while True:
            rand_index_2 = randint(0, len(population) - 1)
            if (rand_index_2 != rand_index_1):
                parents.append(population[rand_index_2])
                break
            else:
                continue
        return parents

    def tournament_selection_NN(self, population, fitness, **kwargs):
        
        Рандомно выбираем две особи(без повторения) и сравниваем их приспособленность.
        В новую популяцию поподает та, у которой лучше значение функции приспособленности
        :param: population : массив сгенерированных особей
                fitness : значение приспособленности для всей популяции
        :return: массив новой популяции
        
        new_population = []
        for i in range(self.n_osob):
            ind_osob_1 = randint(0, len(population) - 1)
            select_1 = population[ind_osob_1]
            while True:
                ind_osob_2 = randint(0, len(population) - 1)
                if (ind_osob_2 != ind_osob_1):
                    select_2 = population[ind_osob_2]
                    break
                else:
                    continue
            if (fitness[ind_osob_1] > fitness[ind_osob_2]):
                new_population.append(select_1)
            else:
                new_population.append(select_2)
        return new_population


    def roulette_selection_NN(self, population, fitness, **kwargs):
        
        Для каждой особи высчитываем вероятность поподания в новую популяцию(отношение приспособленности к сумме всех
        приспособленностей). Далее рандомно выбираем особь и путем рандомного выбора k = [0;1] определяем попала
        ли особь в новую популяцию. Т.е. её вероятность должна быть больше k.
        :param: population : массив сгенерированных особей
                fitness : значение приспособленности для всей популяции
        :return: массив новой популяции
        
        summ_i = 0
        probabilities = []
        new_population = []
        j = 0
        for i in range(len(population)):
            summ_i += fitness[i]

        for i in range(len(population)):
            probabilities.append(fitness[i] / summ_i)

        while j < self.n_osob:
            i = randint(0, len(population) - 1)
            k = random()
            if (probabilities[i] > k):
                new_population.append(population[i])
                j += 1
        return new_population
    """



