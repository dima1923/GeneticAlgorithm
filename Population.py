from Base import Base
import numpy as np
## Tepl
from operator import itemgetter

class Population(Base):
    def truncation_selection(self):
        pass


    #dmitry
    def elite_selection(self, parents, population, generator, fitness, sizeOfPopulation, **kwargs):
        tmp = np.concatenate((parents, population), axis=0)
        fitness_sort = np.argsort(fitness(population=tmp))[-1:-int(np.ceil(sizeOfPopulation*0.2)):-1]
        return np.concatenate([tmp[fitness_sort, :],
                               generator(int(np.floor(sizeOfPopulation*0.8)), population.shape[1])],
                              axis=0)

    def displacement_selection(self):
        pass

    def annealing_selection(self):
        pass


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
