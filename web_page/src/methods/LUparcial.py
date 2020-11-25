from math import *
class LUParcial:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.b = vector
        self.count = 0

    def create_matrix(self, matrix):
        x = matrix.split(',')
        new_matrix = list()
        for i in range(len(x)):
            new_matrix.append(list(map(float, x[i].split(' '))))
        return new_matrix

    def vector_b(self, b):
        return list(map(float, b.split(' ')))

    def matrix_u(self, matrix):
        matrix_u = list()
        for x in range(len(matrix)):
            matrix_u.append(list())
            for y in range(len(matrix)):
                matrix_u[x].append(0)
        return matrix_u

    def matrix_l(self, matrix):
        matrix_l = list()
        for x in range(len(matrix)):
            matrix_l.append(list())
            for y in range(len(matrix)):
                if x == y:
                    matrix_l[x].append(1)
                else:
                    matrix_l[x].append(0)
        return matrix_l

    def identity_l(self, matrix):
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                if x == y:
                    matrix[x][y] = 1
                if x < y:
                    matrix[x][y] = 0
        return matrix

    def matrix_p(self, matrix):
        matrix_p = list()
        for x in range(len(matrix)):
            matrix_p.append(list())
            for y in range(len(matrix)):
                if x == y:
                    matrix_p[x].append(1)
                else:
                    matrix_p[x].append(0)
        return matrix_p

    def multiply_line(self, multiplier, line, x):
        z = x
        for y in range(len(self.matrix)-x):
            self.matrix[line][x] = self.matrix[line][x] - (multiplier * self.matrix[z][x])
            x+=1

    def change_lines(self, matrix, l1, l2):
        matrix[l2], matrix[l1] = matrix[l1], matrix[l2]

    def sustreg(self, matrix, b):
        length = len(matrix)
        x_array = list()
        cont = length - 1
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * matrix[cont][length - 1 - y]
            x_array.append((b[length - 1 - x] - summ)/matrix[length - 1 - x][length - 1 - x])
            cont -= 1
        x_array.reverse()
        return x_array

    def sustprog(self, matrix, b):
        length = len(matrix)
        x_array = list()
        cont = 0
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * matrix[cont][y]
            x_array.append((b[x] - summ)/matrix[x][x])
            cont += 1
        return x_array

    def multiply_matrix(self, matrix, vector):
        new_vector = list()
        for line in matrix:
            summ = 0
            for y in range(len(matrix)):
                summ += line[y] * vector[y]
            new_vector.append(summ)
        return new_vector

    def run(self):
        self.matrix = self.create_matrix(self.matrix)
        matrix_l = self.matrix_l(self.matrix)
        matrix_u = self.matrix_u(self.matrix)
        matrix_p = self.matrix_p(self.matrix)
        A = []
        L = []
        U = []
        P = []
        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                aux=0
                if(abs(self.matrix[i][i])<abs(self.matrix[j][i])):
                    self.change_lines(self.matrix,i,j)
                    self.change_lines(matrix_p,i,j)
                    if i != 0:
                        self.change_lines(matrix_l,i,j)

            for p in range(i+1,len(self.matrix)):
                multiplier = self.matrix[p][i]/self.matrix[i][i]
                matrix_l[p][i] = multiplier
                self.multiply_line(multiplier, p, i)
            for x in range(i, len(self.matrix[0])):
                matrix_u[i][x] = self.matrix[i][x]
                if x+1 < len(self.matrix[0]):
                    matrix_u[i+1][x+1] = self.matrix[i+1][x+1]
            print('Etapa ' + str(i) + '\n')
            print('A = [\n')
            for x in range(len(self.matrix)):
                a = []
                for element in self.matrix[x]:
                    a.append(f'{element:.4f}')
                if x == len(self.matrix) - 1:
                    A.append(a)
            print('L = [\n')
            for x in range(len(self.matrix)):
                l = []
                for element in matrix_l[x]:
                    l.append(f'{element:.4f}')
                if x == len(self.matrix) - 1:
                    L.append(l)
            print('U = [\n')
            for x in range(len(self.matrix)):
                u = []
                for element in matrix_u[x]:
                    u.append(f'{element:.4f}')
                if x == len(self.matrix) - 1:
                    U.append(u)
            print('P = [\n')
            for x in range(len(self.matrix)):
                p = []
                for element in matrix_p[x]:
                    p.append(f'{element:.4f}')
                if x == len(self.matrix) - 1:
                    P.append(p)


        matrix_l = self.identity_l(matrix_l)
        matrix_u[len(self.matrix)-1][len(self.matrix)-1] = self.matrix[len(self.matrix)-1][len(self.matrix)-1]
                    
        vector_b = self.vector_b(self.b)
        Pxb = self.multiply_matrix(matrix_p, vector_b)
        z = self.sustprog(matrix_l, Pxb)
        x = self.sustreg(matrix_u, z)
        return A, L, U, P, z, x