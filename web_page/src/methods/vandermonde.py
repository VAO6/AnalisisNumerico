from math import *
from .piv_par import Piv_par
class Vandermonde:

    def __init__(self, X, Y):
        self.matrix = X
        self.y = Y

    def matrix_x(self, matrix):
        x = list(map(float, matrix.split(' ')))
        n = len(x)
        new_matrix = list()
        for y in range(n):
            new_matrix.append(list())
            for z in range(n):
                new_matrix[y].append(x[y]**(n-1-z))
        return new_matrix

    def vector_b(self, b):
        return list(map(float, b.split(' ')))

    def run(self):
        X = self.matrix_x(self.matrix)
        Y = self.vector_b(self.y)

        vandermonde = []
        for x in range(len(X)):
            v = []
            for element in X[x]:
                v.append(f'{element:.4f}')
            vandermonde.append(v)

        pp = Piv_par(X, Y)
        A, x = pp.run()
        pol = []
        for y in range(len(x)):
            pol.append(f'{x[y]:.6f}x^' + str(len(x) - y) + (' + ' if x[y] < 0 else ' '))
        
        return vandermonde, pol