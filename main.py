import BasicGeneticAlgorithm, Crossover, Fitness, Mutation, Selection, Population
from numpy.random import default_rng

def genBinaryPopulation(n, k):
    ans = default_rng().integers(low=0, high=2, size=(n,k))
    return ans

if __name__ == "__main__":
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
    print(ans)

