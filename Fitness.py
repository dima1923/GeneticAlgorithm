from Base import Base
from numpy import exp, average

class Fitness(Base):
    def my(self, population):
        return average(exp(population))