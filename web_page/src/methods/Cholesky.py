from math import *
import numpy as np

class Cholesky:

    def __init__(self,matrix,b):
            self.matrix=matrix
            self.b=b
            self.l=np.identity(len(self.matrix))
            self.u=np.identity(len(self.matrix))

    def create_matrix(self,matrix):
        x = self.matrix.split(',')
        new_matrix = list()
        for i in range(len(x)):
            new_matrix.append(list(map(float, x[i].split(' '))))
        return new_matrix

    def vector_b(self, b):
        return list(map(float, self.b.split(' ')))

    def sustreg(self, matrix, b):
        length = len(self.matrix)
        x_array = list()
        cont = length - 1
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * self.matrix[cont][length - 1 - y]
            x_array.append((self.b[length - 1 - x] - summ)/self.matrix[length - 1 - x][length - 1 - x])
            cont -= 1
        x_array.reverse()
        return x_array

    def sustprog(self, matrix, b):
        length = len(self.matrix)
        x_array = list()
        cont = 0
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * self.matrix[cont][y]
            x_array.append((self.b[x] - summ)/self.matrix[x][x])
            cont += 1
        return x_array  

    def run(self):
        self.matrix = self.create_matrix(self.matrix)
        imprimir=[]
        imprimir.append('Etapa 0: ')
        imprimir.append(self.matrix)
        for i in range(0,len(self.matrix)):
            if (self.matrix[i][i]-sum([self.l[i][s]*self.u[s][i] for s in range(0,i)]))<=0:
                print('It is not possible to run this method, either because of there are complex numbers or there is a division by cero')
            break    
            self.l[i][i]=sqrt(self.matrix[i][i]-sum([self.l[i][s]*self.u[s][i] for s in range(0,i)])) 
            self.u[i][i]=self.l[i][i]
            
            for j in range(i+1,len(self.matrix)):
                sum0=sum([self.l[i][s]*self.u[s][j] for s in range (0,1)])
                self.u[i][i]=(self.matrix[i][j]-sum0)/self.l[i][i]   
        
        vector = self.vector_b(self.b)
        imprimir.append('L = [\n', self.l, '\n]')
        imprimir.append('U = [\n', self.u, '\n]') 
        z = self.sustprog(self.l, vector)
        x = self.sustreg(self.u, z)
        imprimir.append('After applying progressive and regressive substitution: ')
        imprimir.append('x = [\n', x, '\n]')

# from math import *
# import numpy as np

# matrix=input("Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3): ")
# b=input("Enter the vector B separated by spaces. Example: (1 1 1): ")

# def create_matrix(matrix):
#     x = matrix.split(',')
#     new_matrix = list()
#     for i in range(len(x)):
#         new_matrix.append(list(map(float, x[i].split(' '))))
#     return new_matrix

# def vector_b(b):
#     return list(map(float, b.split(' ')))

# def sustreg(matrix, b):
#     length = len(matrix)
#     x_array = list()
#     cont = length - 1
#     for x in range(length):
#         summ = 0
#         for y in range(len(x_array)):
#             summ += x_array[y] * matrix[cont][length - 1 - y]
#         x_array.append((b[length - 1 - x] - summ)/matrix[length - 1 - x][length - 1 - x])
#         cont -= 1
#     x_array.reverse()
#     return x_array

# def sustprog(matrix, b):
#     length = len(matrix)
#     x_array = list()
#     cont = 0
#     for x in range(length):
#         summ = 0
#         for y in range(len(x_array)):
#             summ += x_array[y] * matrix[cont][y]
#         x_array.append((b[x] - summ)/matrix[x][x])
#         cont += 1
#     return x_array   
    
# matrix = create_matrix(matrix)
# l=np.identity(len(matrix))
# u=np.identity(len(matrix))


# for i in range(0,len(matrix)):
#     # if (matrix[i][i]-sum([l[i][s]*u[s][i] for s in range(0,i)]))<=0:
#     #     print('No se puede correr el método pues aparecen números cumplejos o división por cero')
#     # break    
#     l[i][i]=sqrt(matrix[i][i]-sum([l[i][s]*u[s][i] for s in range(0,i)])) 
#     u[i][i]=l[i][i]
    
#     for j in range(i+1,len(matrix)):
#         sum0=sum([l[i][s]*u[s][j] for s in range (0,1)])
#         u[i][i]=(matrix[i][j]-sum0)/l[i][i]   
 
# vector_b = vector_b(b)
# print('L = [\n', l, '\n]')
# print('U = [\n', u, '\n]') 
# z = sustprog(l, vector_b)
# x = sustreg(u, z)
# print('z = [\n', z, '\n]')
# print('x = [\n', x, '\n]')