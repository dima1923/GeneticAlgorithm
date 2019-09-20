class BasicGeneticAlgorithm:
    def __init__(self, generator, fitness, selection, crossover, mutation):
        self.generator = generator
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation

    def newPopulation(self, evalFitness):
        ar = []
        for i in range(0,100): #откуда брать размер популяции?
            parents = self.selection(evalFitness)
            crossover = self.crossover(parents)
            mutation = self.mutation(crossover)
            ar.append(mutation)
        return ar


    def fit(self):
        x = self.generator
        for epoche in range(0,100):#откуда брать критерий остановки?
            evalFitness = self.fitness(x)
            newPopulation = self.newPopulation(evalFitness)
            x = newPopulation

