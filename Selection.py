from Base import Base
import numpy as np
from numpy.random import default_rng
from random import randint

class Selection(Base):
    #dmitry
    def tournament_selection(self, population, fitness):
        try:
            t = self.kwargs['t']
        except KeyError:
            raise AttributeError
        ans = np.empty(shape=(int(np.ceil(0.9*population.shape[0])),population.shape[1]))
        tmp = np.array(population)
        for i in range(0,int(np.ceil(0.9*population.shape[0]))):
            default_rng().shuffle(tmp)
            position = fitness(population=tmp[:t]).argmax()
            ans[i] = tmp[position]
            tmp = np.delete(tmp, position, 0)
        return ans

    #NN
    @staticmethod
    def Hamming_distance(individ_1, individ_2):
        distance = 0;
        len_1 = len(individ_1)
        len_2 = len(individ_2)
        if (len_1 > len_2):
            diff = len_1 - len_2
            for i in range(len_2):
                if i > 1:
                    if (individ_2[i] != individ_1[i]):
                        dis = abs(individ_1[i] - individ_2[i])
                        distance += dis
                else:
                    distance += 1
        else:
            diff = len_2 - len_1
            for i in range(len_1):
                if i > 1:
                    if (individ_1[i] != individ_2[i]):
                        dis = abs(individ_1[i] - individ_2[i])
                        distance += dis
                else:
                    distance += 1
        # distance += diff
        return distance

    #NN
    def inbreeding_nn(self, population):
        """
        :param population:массив сгенерированных особей; выходные данные: массив из двух выбранных родителей
        :return: массив из двух выбранных родителей
        """
        rand_index = randint(0, len(population) - 1)
        parent_1 = population[rand_index]
        min_hamming_dist = 99999
        candidates = []
        for i in range(0, len(population)):
            if (i == rand_index):
                continue
            else:
                tmp = self.Hamming_distance(parent_1, population[i])
                if (tmp < min_hamming_dist):
                    min_hamming_dist = tmp
        l = 0
        for j in range(0, len(population)):
            if (self.Hamming_distance(parent_1, population[j]) == min_hamming_dist):
                candidates.append(population[j])
                l += 1
        rand_index_2 = randint(0, l - 1)
        parent_2 = candidates[rand_index_2]
        return [parent_1, parent_2]

    #NN
    def outbreeding_nn(self, population):
        rand_index = randint(0, n_osob - 1)
        parent_1 = population[rand_index]
        max_hamming_dist = 0
        candidates = []
        for i in range(0, len(population)):
            tmp = self.Hamming_distance(parent_1, population[i])
            if (tmp > max_hamming_dist):
                max_hamming_dist = tmp
        l = 0
        for j in range(0, len(population)):
            if (self.Hamming_distance(parent_1, population[j]) == max_hamming_dist):
                candidates.append(population[j])
                l += 1
        rand_index_2 = randint(0, l - 1)
        parent_2 = candidates[rand_index_2]
        return [parent_1, parent_2]


    def panmixia_nn(self, population):
        rand_index_1 = randint(0, len(population) - 1)
        parent_1 = population[rand_index_1]
        while True:
            rand_index_2 = randint(0, len(population) - 1)
            if (rand_index_2 != rand_index_1):
                parent_2 = population[rand_index_2]
                break
            else:
                continue
        return [parent_1, parent_2]

#Komiv
    def selection(self, pr, individ):#??????????
        selectia = []
        sr_pr = np.mean(pr)
        for i in range(len(individ)):
            if pr[i] > sr_pr:
                selectia.append(individ[i])
        print(sr_pr)
        return selectia

    def turnir(self, individ, pr):
        t = 2
        turn = []
        for i in range(len(individ)):
            choice = []
            for j in range(t):
                x = choice(pr)
                k = list(pr).index(x)
                choice.extend([x, k])
            if choice[t - 2] > choice[t]:
                turn.append(individ[int(choice[t - 1])])
            else:
                turn.append(individ[int(choice[t + 1])])

        return turn


    def roulette(self, F, n):
        import random
        total_fit = sum(F)
        rel_fit = [i / total_fit for i in F]
        prob_list = [sum(rel_fit[:i + 1]) for i in range(len(rel_fit))]

        chosen_indivs = []
        for i in range(n):
            point = random.random()
            index = -1
            for j in prob_list:
                index += 1
                if point <= j:
                    chosen_indivs.append(index)
                    break

        return chosen_indivs