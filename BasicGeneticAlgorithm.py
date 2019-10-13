import numpy as np

class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover,
                 mutation, sizeOfPopulation, stopFunction,
                 genPopulation, numberChromosome, **kwargs):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.sizeOfPopulation = sizeOfPopulation
        self.stopFunction = stopFunction
        self.populationGen = genPopulation
        self.numberChromosome = numberChromosome
        self.otherArgs = kwargs

    def newPopulation(self, x):
        parents = self.selection(population=x, fitness=self.fitness)
        crossover = self.crossover(parents=parents)
        mutation = self.mutation(ar=crossover)
        ans=self.populationGen(parents=x, population=mutation,
                               generator=self.generator, fitness=self.fitness,
                               otherArgs=self.otherArgs,
                               sizeOfPopulation=self.sizeOfPopulation)
        return ans


    def fit(self):
        population = self.generator(self.sizeOfPopulation, self.numberChromosome)
        for epoche in range(0, 100):#откуда брать критерий остановки?
            population = self.newPopulation(population)
        return population[self.fitness(population=population).argmax()]
