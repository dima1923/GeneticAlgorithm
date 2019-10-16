import BasicGeneticAlgorithm, Crossover, Fitness, Mutation, Selection, Population
from numpy.random import default_rng
## import pandas as pd
## import random as rd
## Tepl
import numpy as np
import random
## NN
from random import randint, choice, uniform

def genBinaryPopulation(n, k):
    """

    :param n:
    :param k:
    :return:
    """
    ans = default_rng().integers(low=0, high=2, size=(n,k))
    return ans


""" NN
def individual(length, min_, max_, n_class):
    
    :param length: длина особи
    :param min_: мин кол-во нейронов в слоях
    :param max_: макс кол-во нейронов в слоях
    :param n_class: кол-ва классов
    :return: сгенерированный индивид
    
    individ = []
    #функция активации
    individ.append(choice(['relu', 'elu', 'tanh', 'sigmoid']))
    #доля train выборки
    individ.append(round(uniform(0,0.9),2))
    #количество скрытых слоев и количество нейронов на них
    individ.append(length)
    for x in range(length - 1):
        individ.append(randint(min_, max_))
    individ.append(n_class)
    return individ

def generate_population(n_osob, min_, max_, n_class):
    
    :param n_osob: кол-во особей в популяции
    :param min_: мин кол-во нейронов в слоях
    :param max_: макс кол-во нейронов в слоях
    :param n_class: кол-ва классов
    :return: сгенерированная популяция
    
    population = []
    for i in range(n_osob):
        length_individ = randint(2, 10)
        population.append(individual(length_individ,min_, max_, n_class))
    return population
"""

""" Man
def GenPop(N, l):

    :param N: объём формируемой популяции
    :param l: кол-во генов в одной особи (кол-во элементов вектора, характеризующего особь)
    :return: особь + гены

    Indiv = []
    for i in range(N):
        Indiv.append(rd.sample(range(1, l + 1), l))
    list_g = []
    for i in range(l):
        list_g.append("gen_{}".format(i + 1))
    list_i = []
    for i in range(N):
        list_i.append("indiv_{}".format(i + 1))
    return pd.DataFrame(Indiv, index=list_i, columns=list_g)
"""

""" Tepl
def generate_first_population_Tepl(NUM_POPULATION,length):
    
    Создание стартовой популяции.
    Создаем массив размерности NUM_POPULATION на length.
    Создаем особь, заполняем генами от 1 до length и перемешиваем гены внутри особи
    :param NUM_POPULATION: кол-во особей в популяции
    :param length: кол-во генов особи
    :return:
    
    population = np.arange(NUM_POPULATION*length).reshape((NUM_POPULATION, length))
    for i in range(NUM_POPULATION):
        osob = np.arange(1, length + 1 , 1)
        random.shuffle(osob)
        population[i] = osob
    return population
"""

if __name__ == "__main__":
    fitness = Fitness.Fitness('my')
    crossover = Crossover.Crossover('single_point_crossover')
    selection = Selection.Selection('tournament_selection', t=4)
    mutation = Mutation.Mutation('binary_mutation')
    populationGen = Population.Population('elite_selection')
    bga = BasicGeneticAlgorithm.BasicGeneticAlgorithm(generator=genBinaryPopulation,
                                                      fitness=fitness,
                                                      crossover=crossover,
                                                      selection=selection,
                                                      mutation=mutation,
                                                      sizeOfPopulation=100,
                                                      genPopulation=populationGen,
                                                      numberChromosome=100, epoche=100)
    ans = bga.fit()
    print(ans)

