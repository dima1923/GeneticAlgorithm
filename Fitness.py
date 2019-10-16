from Base import Base
from numpy import exp, average

class Fitness(Base):
    def my(self, population, **kwargs):
        return average(exp(population), axis=1)