import numpy as np

class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover,
                 mutation, sizeOfPopulation,
                 genPopulation, numberChromosome, epoche =100, error=0.001,
                 stopFunctionChange=False, **kwargs):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.sizeOfPopulation = sizeOfPopulation
        self.stopFunctionChange = stopFunctionChange
        self.populationGen = genPopulation
        self.numberChromosome = numberChromosome
        self.epoche = epoche
        self.error = error
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
        i = 0
        old_fit = np.inf
        while ((i!=self.epoche and self.stopFunctionChange is False)
               or (np.abs(old_fit-self.fitness(population=population).argmin()) <= self.error and self.stopFunctionChange is True)):
            old_fit = self.fitness(population=population).argmin()
            population = self.newPopulation(population)
            i += 1
        return population[self.fitness(population=population).argmin()]
