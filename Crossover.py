from Base import Base
import random
import numpy as np

class Crossover(Base):
    def density_crossover(self):
        pass

    def intermediate_crossover(self):
        pass

    def linear_crossover(self):
        pass

    def single_point_crossover(self, parents):
        point = int(parents.shape[1] / 2)
        offspring = np.empty(2)
        while (point == int(parents.shape[1] / 2)):
            point = random.randint(0, parents.shape[1])
        offspring[0] = np.concatenate((parents[0,0:point],parents[1,point:]), axis=None)
        offspring[1] = np.concatenate((parents[1, 0:point], parents[0, point:]), axis=None)
        return offspring

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
