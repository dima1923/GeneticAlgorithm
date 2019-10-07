import numpy as np

class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover,
                 mutation, sizeOfPopulation, stopFunction,
                 genPopulation):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation
        self.sizeOfPopulation = sizeOfPopulation
        self.stopFunction = stopFunction
        self.populationGen = genPopulation

    def newPopulation(self, x):
        ar = []
        for i in range(0, self.sizeOfPopulation): #откуда брать размер популяции?
            parents = self.selection(population=x, fitness=self.fitness)
            crossover = self.crossover(parents=parents)
            mutation = self.mutation(ar=crossover)
            for l in mutation:
                ar.append(l)
        ans=self.populationGen(parents=x, population=np.array(ar), generator=self.generator, fitness=self.fitness)
        return np.array(ans)


    def fit(self):
        population = self.generator(50,100)
        for epoche in range(0, 100):#откуда брать критерий остановки?
            population = self.newPopulation(population)
        return population[self.fitness(population=population).argmax()]
