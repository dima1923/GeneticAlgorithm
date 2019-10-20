import numpy as np
from Crossover import Crossover

class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover,
                 mutation, sizeOfPopulation,
                 genPopulation, numberChromosome=None, epoche=100, error=0.001,
                 stopFunctionChange=False, data=None, **kwargs):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        if crossover is None:
            crossover = Crossover('empty')
        self.crossover = crossover
        self.mutation = mutation
        self.sizeOfPopulation = sizeOfPopulation
        self.stopFunctionChange = stopFunctionChange
        self.populationGen = genPopulation
        self.numberChromosome = numberChromosome
        self.epoche = epoche
        self.error = error
        self.data = data
        self.otherArgs = kwargs

    def newPopulation(self, x):
        parents = self.selection(population=x, generator=self.generator, fitness=self.fitness, data=self.data)
        crossover = self.crossover(parents=parents, generator=self.generator, fitness=self.fitness, data=self.data)
        mutation = self.mutation(ar=crossover, generator=self.generator, fitness=self.fitness, data=self.data)
        ans = self.populationGen(parents=x, population=mutation, generator=self.generator, fitness=self.fitness,
                               sizeOfPopulation=self.sizeOfPopulation, data=self.data)
        return ans


    def fit(self):
        population = self.generator(self.sizeOfPopulation, self.numberChromosome)
        i = 0
        old_fit = np.inf
        while ((i != self.epoche and self.stopFunctionChange is False)
               or (np.abs(old_fit-np.array(self.fitness(population=population, data=self.data)).argmin()) <= self.error and self.stopFunctionChange is True)):
            old_fit = np.array(self.fitness(population=population, data=self.data)).argmin()
            population = self.newPopulation(population)
            i += 1
        return population[np.array(self.fitness(population=population, data=self.data)).argmin()], min(self.fitness(population=population,data=self.data))
