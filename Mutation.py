from Base import Base
import random
import numpy as np

class Mutation(Base):
    #dmitry
    def binary_mutation(self, ar):
        tmp = np.array(ar)
        position = random.randint(0,tmp.shape[1]-1)
        for i in range(tmp.shape[0]):
            if tmp[i, position] == 0:
                tmp[i ,position] = 1
            else:
                tmp[i, position] = 0
        return tmp

    def density_mutation(self):
        pass

    def real_mutation(self):
        pass

    def insertion_deleting_mutation(self):
        pass

    def changing_mutation(self):
        pass

    def inversion(self):
        pass