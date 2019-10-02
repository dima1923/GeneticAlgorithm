from Base import Base
import random
import numpy as np

class Mutation(Base):
    def binary_mutation(self,ar):
        tmp = np.array(ar)
        position = random.randint(tmp.shape[1])
        tmp[:,position]=np.invert(tmp[:,position])
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