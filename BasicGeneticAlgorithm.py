import numpy as np

class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover,
                 mutation, sizeOfPopulation, stopFunction):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.sizeOfPopulation = sizeOfPopulation
        self.stopFunction = stopFunction

    def newPopulation(self, x, evalFitness):
        ar = []
        for i in range(0, self.sizeOfPopulation): #откуда брать размер популяции?
            parents = self.selection(population=x, fitness=self.fitness)
            crossover = self.crossover(parents=parents)
            mutation = self.mutation(ar=crossover)
            for l in mutation:
                ar.append(l)
        return np.array(ar)


    def fit(self):
        population = self.generator(50,100)
        for epoche in range(0, 100):#откуда брать критерий остановки?
            evalFitness = self.fitness(population=population)
            population = self.newPopulation(population, evalFitness)
        return 0
