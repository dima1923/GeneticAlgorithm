import BasicGeneticAlgorithm, Crossover, Fitness, Mutation, Selection, Population
from numpy.random import default_rng
## Man
import pandas as pd
import random as rd
## Tepl
import numpy as np
import random
## NN
from random import randint, choice, uniform

def genBinaryPopulation(n, k):
    """
    :param n: количество особей
    :param k: количество генов
    :return: сгенерированная популяция
    """
    ## мин и макс число в рандоме, размерность матрицы ans
    ans = default_rng().integers(low=0, high=2, size=(n,k))
    return ans

""" NN
def individual(length, min_, max_, n_class):
    count_chrom = 15;
    min_ = 1; #global variable
    max_ = 10; #global variable
    n_class = 3;
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

## удалила list_g и list_i
def GenPop_Man(n, k):
    """
    :param n: кол-во особей в популяции
    :param k: кол-во генов особи
    :return: сгенерированная популяция
    """
    population = []
    for i in range(n):
        population.append(rd.sample(range(1, k + 1), k))
    return population


## +++
def generate_first_population_Tepl(n,k):
    """
    :param n: кол-во особей в популяции
    :param k: кол-во генов особи
    :return: сгенерированная популяция
    """
    # массив размерности n на k
    population = np.arange(n*k).reshape((n, k))
    for i in range(n):
        # особь, заполняем генами от 1 до k и перемешиваем гены внутри особи
        osob = np.arange(1, k + 1 , 1)
        random.shuffle(osob)
        population[i] = osob
    return population

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

