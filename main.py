import BasicGeneticAlgorithm, Crossover, Fitness, Mutation, Selection
from numpy.random import default_rng

def genPopulation(n, k):
    ans = default_rng().integers(low=0, high=2, size=(n,k))
    return ans

if __name__ == "__main__":
    fitness = Fitness.Fitness('my')
    crossover = Crossover.Crossover('single_point_crossover')
    selection = Selection.Selection('tournament_selection', t=4)
    mutation = Mutation.Mutation('binary_mutation')
    bga = BasicGeneticAlgorithm.BasicGeneticAlgorithm(generator=genPopulation,
                                                      fitness=fitness,
                                                      crossover=crossover,
                                                      selection=selection,
                                                      mutation=mutation,
                                                      sizeOfPopulation=50,
                                                      stopFunction=True)
    ans=bga.fit()
    print(ans)
