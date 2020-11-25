from math import *
import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

class Sor:
    def __init__(self, matrix, b, x0, tol, it, w):
        self.matrix=matrix
        self.b=b
        self.x0=list(map(float, x0.split(' ')))
        self.tol=10**tol
        self.it=it
        self.w = w

    def create_matrix(self, matrix):
        x = matrix.split(',')
        new_matrix = list()
        for i in range(len(x)):
            new_matrix.append(list(map(float, x[i].split(' '))))
        return new_matrix

    def vector_b(self, b):
        return list(map(float, b.split(' ')))

    def matrix_d(self, matrix):
        matrix_d = list()
        for x in range(len(matrix)):
            matrix_d.append(list())
            for y in range(len(matrix)):
                if x == y:
                    matrix_d[x].append(matrix[x][y])
                else:
                    matrix_d[x].append(0)
        return matrix_d

    def matrix_u(self, mA, mD):
        return self.sum_matrix(self.minus_triangular_upper(mA), mD)

    def matrix_l(self, mA, mD):
        return self.sum_matrix(self.minus_triangular_lower(mA), mD)

    def matrix_t(self, mD, mL, mU, w):
        md = self.substract_matrix(mD, self.multiply_matrix_scalar(mL, w))
        md = inv(md)
        return np.matmul(md, self.sum_matrix(self.multiply_matrix_scalar(self.matrix_d,(1-w)), self.multiply_matrix_scalar(self.matrix_u, w)))

    def matrix_c(self, mD, mL, b, w):
        md = self.substract_matrix(mD, self.multiply_matrix_scalar(mL, w))
        md = self.multiply_matrix_scalar(inv(md).tolist(), w)
        return self.multiply_matrix(md, b)

    def multiply_matrix_scalar(self, m1, s):
        new_matrix = list()
        x = 0
        for element in m1:
            if type(element) == list:
                new_matrix.append(list())
                for number in element:
                    new_matrix[x].append(number*s)
                x+=1
            else:
                new_matrix.append(element*s)
        return new_matrix

    def multiply_matrix(self, matrix, vector):
        new_vector = list()
        for line in matrix:
            summ = 0
            for y in range(len(matrix)):
                summ += line[y] * vector[y]
            new_vector.append(summ)
        return new_vector

    def sum_matrix(self, m1, m2):
        length = len(m1)
        new_matrix = list()
        for x in range(length):
            if type(m1[0]) == list:
                new_matrix.append(list())
                for y in range(length):
                        new_matrix[x].append((m1[x][y] + m2[x][y]))
            else:
                new_matrix.append(m1[x] + m2[x])
        return new_matrix

    def substract_matrix(self, m1, m2):
        length = len(m1)
        new_matrix = list()
        for x in range(length):
            if type(m1[0]) == list:
                new_matrix.append(list())
                for y in range(length):
                        new_matrix[x].append((m1[x][y] - m2[x][y]))
            else:
                new_matrix.append(m1[x] - m2[x])
        return new_matrix

    def sum_matrix_vector(self, m1, vector):
        length = len(m1)
        new_matrix = list()
        for element in m1:
            new_matrix.append(list())
            for y in range(length):
                new_matrix[y].append((element[y] + vector[y]))
        return new_matrix

    def minus_triangular_upper(self, matrix):
        matrix_d = list()
        for x in range(len(matrix)):
            matrix_d.append(list())
            for y in range(len(matrix)):
                if x <= y:
                    matrix_d[x].append(-matrix[x][y])
                else:
                    matrix_d[x].append(0)
        return matrix_d

    def minus_triangular_lower(self, matrix):
        matrix_d = list()
        for x in range(len(matrix)):
            matrix_d.append(list())
            for y in range(len(matrix)):
                if x >= y:
                    matrix_d[x].append(-matrix[x][y])
                else:
                    matrix_d[x].append(0)
        return matrix_d

    def list_to_vector(self, listt):
        return list(map(lambda x: [x], listt))

    def run(self):
        self.matrix = self.create_matrix(self.matrix)
        self.matrix_d = self.matrix_d(self.matrix)
        self.matrix_u = self.matrix_u(self.matrix, self.matrix_d)
        self.matrix_l = self.matrix_l(self.matrix, self.matrix_d)
        self.matrix_t = self.matrix_t(self.matrix_d, self.matrix_l, self.matrix_u, self.w)
        self.vector_b = self.vector_b(self.b)
        self.matrix_c = self.matrix_c(self.matrix_d, self.matrix_l, self.vector_b, self.w)
        xant = self.x0
        E = 1000
        cont=0
        T = []
        C = []
        for x in range(len(self.matrix_t)):
            t = []
            for element in self.matrix_t[x]:
                t.append(f'{element:.4f}')
            if x == len(self.matrix_t) - 1:
                T.append(t)
        for element in self.matrix_c:
            C.append(f'{element:.6f}')
        imprimir = ['| iter |      E     | ']

        while E > self.tol and cont<self.it:
            xact=self.sum_matrix(self.matrix_c, self.multiply_matrix(self.matrix_t, xant))
            E = LA.norm(np.array(self.substract_matrix(xant, xact)))
            xant = xact
            cont += 1
            imp = []
            imp.append(f'|  {cont}   |   {E:.1e}  | ')
            for x in xact:
                imp.append(f'{x:.6f} ')
            imprimir.append(imp)

        return T, C, imprimir, xact, cont, E