from Base import Base
import random
import numpy as np

class Crossover(Base):
    def empty(self,parents):
        return parents

    def density_crossover(self):
        pass

    def intermediate_crossover(self):
        pass

    def linear_crossover(self):
        pass

    #dmitry
    def single_point_crossover(self, parents:np.ndarray):
        tmp = np.empty(shape=parents.shape)
        j = 0
        while parents.shape[0] != 0:
            index_of_parent = random.sample([i for i in range(parents.shape[0])],2)
            point = int(parents.shape[1] / 2)
            while (point == int(parents.shape[1] / 2)):
                point = random.randint(0, parents.shape[1])
            tmp[j] = np.concatenate((parents[index_of_parent[0], 0:point],parents[index_of_parent[1], point:]), axis=None)
            j += 1
            tmp[j] = np.concatenate((parents[index_of_parent[1], 0:point], parents[index_of_parent[0], point:]), axis=None)
            j += 1
            parents = np.delete(parents, index_of_parent, 0)
        return tmp

    def double_point_crossover(self):
        pass

    def multipoint_crossover(self):
        pass

    def uniform_crossover(self):
        pass

    def process_crossover(self):
        pass

    def shuffle_crossover(self):
        pass

    def replacement_crossover(self):
        pass
