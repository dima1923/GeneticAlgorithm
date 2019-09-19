class BasicGeneticAlgorithm:
    def __init__(self, fitness, selection, crossover, mutation):
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation

    def newPopulation(self):
        pass

    def fit(self):
        pass