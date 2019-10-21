from Base import Base
import numpy as np
import math
from numpy import exp, average
import time
from keras.layers import Dense, Dropout

## import time

class Fitness(Base):
    def my(self, population, **kwargs):
        """
        Приспособленность каждой. Каждую из популяции возводим в экспоненту и берем среднее из экспонент.
        :param population: массив особей
        :return: приспособленность всей популяции
        """
        return average(exp(population), axis=1)


    def Fit_Man(self, population, data, **kwargs):
        """
        Рассчитываем приспособленность каждой особи, как сумму расстояний между городами.
        :param individ: массив сгенерированных особей
               distant: матрица расстояний (массив)
        :return: массив сумм растояний между городами для каждой особи
        """
        s = []
        for i in range(len(population)):
            summ = 0
            for j in range(len(population[0]) - 1):
                if j != len(population[0]):
                    summ += data[int(population[int(i)][int(j)] - 1)][int(population[int(i)][int(j + 1)] - 1)]
            s.append(summ)
        return s


    def fitness_f_Tepl(self, population, data, **kwargs):
        """
        Расчет фитнесс-функции для каждого юнита
        Суммарное значение фитнесс-функций по таблице ценностей
        :param data: таблица ценности
        :param unit: конкретная особь
        :return:
        """
        fit = []
        for unit in population:
            sum = 0
            for c, u in enumerate(unit):
                sum += data.item((c, u - 1))
            fit.append(sum)
        return fit

    def compile_model(network, input_shape):
        """Compile a sequential model.
        Args: network (dict): the parameters of the network
        Returns: a compiled network.
        """
        # Get our network parameters.
        nb_layers = network[2]
        model = Sequential()
        model.add(Dense(5, activation='sigmoid', input_shape=input_shape))
        # Add each layer.
        for i in range(2, nb_layers - 1):
            # Need input shape for first layer.
            if i == 2:
                model.add(Dense(network[i + 1], activation=network[0], input_shape=input_shape))
                i += 1
            else:
                model.add(Dense(network[i], activation=network[0]))
            model.add(Dropout(0.2))  # hard-coded dropout
        model.add(Dense(n_class, activation='sigmoid'))
        model.compile(loss='categorical_crossentropy', optimizer='adagrad',
                      metrics=['accuracy'])
        return model

    def train_and_score_NN(network):
        nb_classes = network[-1]
        input_shape, X_train, X_test, y_train, y_test, batch_size = split_train_test(path, network[1])

        model = compile_model(network, input_shape)

        model.fit(X_train, y_train,
                  epochs=10000,  # using early stopping, so no real limit
                  verbose=0,
                  validation_data=(X_test, y_test)
                  )

        score_test = model.evaluate(X_test, y_test, verbose=0)
        score_train = model.evaluate(X_train, y_train, verbose=0)
        print("individ\n")
        print(network)
        print("\ntest\n")
        print(score_test)
        print("\ntrain\n")
        print(score_train)
        print("\n")
        return [score_train[1], score_test[1]]  # 1 is accuracy. 0 is loss.

    def fitness_indiv_NN(self, indiv):
        res_of_train = train_and_score_NN(indiv)
        return res_of_train[0] * indiv[1] + (1 - indiv[1]) * res_of_train[1]

    def fitness_population_NN(self, population):
        start_time = time.time()

        population_fitness = []
        for item in population:
            population_fitness.append(self.fitness_indiv_NN(item))

        end_time = time.time()
        print("Process take {0}  seconds ".format(end_time - start_time))

        return population_fitness

