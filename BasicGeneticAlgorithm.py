class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover, mutation):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation

    def newPopulation(self, x, evalFitness):
        ar = []
        for i in range(0, 100): #откуда брать размер популяции?
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

