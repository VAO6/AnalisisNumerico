import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

class Gausseidel:
    def __init__(self, matrix, b, x0, tol, it):
        self.matrix=matrix
        self.b=b
        self.x0=list(map(float, x0.split(' ')))
        self.tol=10**tol
        self.it=it


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

    def matrix_t(self, mD, mL, mU):
        md = self.substract_matrix(mD, mL)
        md = inv(md)
        return np.matmul(md, np.array(mU)).tolist()

    def matrix_c(self, mD, mL, b):
        md = self.substract_matrix(mD, mL)
        md = inv(md)
        return self.multiply_matrix(md, b)

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
                    if type(m1[0]) == list:
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
                    if type(m1[0]) == list:
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
        matrix = self.create_matrix(self.matrix)
        matrix_d = self.matrix_d(matrix)
        matrix_u = self.matrix_u(matrix, matrix_d)
        matrix_l = self.matrix_l(matrix, matrix_d)
        matrix_t = self.matrix_t(matrix_d, matrix_l, matrix_u)
        vector_b = self.vector_b(self.b)
        matrix_c = self.matrix_c(matrix_d, matrix_l, vector_b)
        xant = self.x0
        E = 1000
        cont=0

        T = []
        print('T = [\n')
        for x in range(len(matrix_t)):
            t = []
            for element in matrix_t[x]:
                t.append(f'{element:.6f}')
            T.append(t)
        C= []
        print('C = [\n')
        for element in matrix_c:
            C.append(f'{element:.6f}')
        imprimir = ['| iter |      E     |']

        while E > self.tol and cont<self.it:
            xact=self.sum_matrix(matrix_c, self.multiply_matrix(matrix_t, xant))
            E = LA.norm(np.array(self.substract_matrix(xant, xact)))
            xant = xact
            cont += 1
            imp = []
            imp.append(f'|  {cont}   |   {E:.1e}  | ')
            for x in xact:
                imp.append(f'{x:.6f} ')
            imprimir.append(imp)
            
        return T, C, imprimir, xact, cont, E
        