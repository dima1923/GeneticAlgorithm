class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover, mutation, sizeOfPopulation, stopFunction):
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
            parents = self.selection.method(x, evalFitness)
            crossover = self.crossover.method(parents)
            mutation = self.mutation.method(crossover)
            ar.append(mutation)
        return ar


    def fit(self):
        population = self.generator
        for epoche in range(0, 100):#откуда брать критерий остановки?
            evalFitness = self.fitness.method(population)
            population = self.newPopulation(population, evalFitness)

