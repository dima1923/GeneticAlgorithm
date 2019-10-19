import BasicGeneticAlgorithm, Crossover, Fitness, Mutation, Selection, Population
##from numpy.random import default_rng
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


# Считывание матрицы расстояний из таблицы Excel
def GenMtrx_Man():
    cities = pd.read_excel('rasstoyania_1.xlsx', header=None).values.tolist() # Считывание матр
    for i in range(len(cities[0])):
        cities[i][i] = float("Inf") # Задаем диагональным значениям бесконечно большое число
    cities = np.around(cities, decimals=0) # Округление числа
    return cities  # Возвращаем растояния между "городами"

## удалила list_g и list_i, они по сути только для красивого вывода
def genPopulation_Man(n, k):
    """
    :param n: кол-во особей в популяции
    :param k: кол-во генов особи
    :return: сгенерированная популяция
    """
    population = []
    for i in range(n):
        population.append(rd.sample(range(1, k + 1), k)) #Заполняем случайно-выбранными особями
    return population

"""
def genPopulation_Tepl(n,k):
    
    :param n: кол-во особей в популяции
    :param k: кол-во генов особи
    :return: сгенерированная популяция
    
    # массив размерности n на k
    population = np.arange(n*k).reshape((n, k))
    for i in range(n):
        # особь, заполняем генами от 1 до k и перемешиваем гены внутри особи
        osob = np.arange(1, k + 1 , 1)
        random.shuffle(osob)
        population[i] = osob
    return population


def genIndividual_NN(k, min_, max_, n_class):
    
    :param k: длина особи
    :param min_: мин кол-во нейронов в слоях
    :param max_: макс кол-во нейронов в слоях
    :param n_class: кол-во классов
    :return: сгенерированный индивид
    
    individ = []
    #функция активации
    individ.append(choice(['relu', 'elu', 'tanh', 'sigmoid']))
    #доля train выборки
    individ.append(round(uniform(0,0.9),2))
    #количество скрытых слоев и количество нейронов на них
    individ.append(k)
    for x in range(k - 1):
        individ.append(randint(min_, max_))
    individ.append(n_class)
    return individ
## вставила k, убрала рандомную длину особи
def genPopulation_NN(n,k):
    
    :param n: кол-во особей в популяции
    :param кол-во генов особи
    :return: сгенерированная популяция
    
    min_ = 1
    max_ = 10
    n_class = 3
    population = []
    for i in range(n):
        population.append(genIndividual_NN(k ,min_, max_, n_class))
    return population
    """

if __name__ == "__main__":
    """    
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
    print(ans)"""


    data_cities = GenMtrx_Man #инициализация условий задачи (считывание матрицы расстояний)
    NN = len(data_cities) #считываем количество городов
    fitness = Fitness.Fitness('Fit_Man')
    crossover = Crossover.Crossover('empty')
    selection = Selection.Selection('tournament_selection_Man')
    mutation = Mutation.Mutation('transposition_mutation_Man')
    populationGen = Population.Population('NewGen_Man')
    bga = BasicGeneticAlgorithm.BasicGeneticAlgorithm(generator=genPopulation_Man,
                                                      fitness=fitness,
                                                      selection=selection,
                                                      mutation=mutation,
                                                      sizeOfPopulation=20,
                                                      genPopulation=populationGen,
                                                      numberChromosome=100, epoche=10,
                                                      data=data_cities)
    ans = bga.fit()
    print(ans)