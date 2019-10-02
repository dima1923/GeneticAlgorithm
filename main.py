import BasicGeneticAlgorithm, Crossover, Fitness, Mutation, Selection
import numpy.random.randint as randint

def genPopulation(n, k):
    ans = randint(low=0, size=(n,k))
    return ans

if __name__ == "__main__":
    bga = BasicGeneticAlgorithm.BasicGeneticAlgorithm(generator=genPopulation(100, 100),
                                                      fitness=Fitness.Fitness('my'),
                                                      crossover=Crossover.Crossover('single_point_crossover'),
                                                      selection=Selection.Selection('my_imbreading'),
                                                      mutation=Mutation.Mutation('binary_mutation'),
                                                      sizeOfPopulation=50)