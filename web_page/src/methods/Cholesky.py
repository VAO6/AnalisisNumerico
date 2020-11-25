from math import sqrt
import numpy as np

class Cholesky:

    def __init__(self,matrix,b):
        self.matrix=matrix
        self.b= list(map(float, b.split(' ')))
        self.l=np.identity(len(self.b))
        self.u=np.identity(len(self.b))

    def create_matrix(self,matrix):
        x = self.matrix.split(',')
        new_matrix = list()
        for i in range(len(x)):
            new_matrix.append(list(map(float, x[i].split(' '))))
        return new_matrix

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
        L = []
        U = []
        for i in range(0,len(self.matrix)):
            if (self.matrix[i][i]-sum([self.l[i][s]*self.u[s][i] for s in range(0,i)]))<=0:
                break    
            self.l[i][i]=sqrt(self.matrix[i][i]-sum([self.l[i][s]*self.u[s][i] for s in range(0,i)])) 
            self.u[i][i]=self.l[i][i]
            
            for j in range(i+1,len(self.matrix)):
                sum0=sum([self.l[i][s]*self.u[s][j] for s in range (0,1)])
                self.u[i][i]=(self.matrix[i][j]-sum0)/self.l[i][i]   
        
        vector = self.b
        L.append(self.l.tolist())
        U.append(self.u.tolist())
        z = self.sustprog(self.l, vector)
        x = self.sustreg(self.u, z)

        return L, U, x