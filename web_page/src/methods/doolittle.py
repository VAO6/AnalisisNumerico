import numpy as np

class Doolittle:

    def __init__(self,matrix,b):
        self.matrix=matrix
        self.b= list(map(float, b.split(' ')))
        self.l=np.identity(len(self.b))
        self.u=np.identity(len(self.b))
    
    def create_matrix(self, matrix):
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
        L = []
        U = []
        for i in range(0,len(self.matrix)):
            self.l[i,i]=1
            for j in range(i,len(self.matrix)):
                sum0=sum([self.l[i][s]*self.u[s][j] for s in range(0,j)])
                self.u[i][j]=self.matrix[i][j]-sum0
            for j in range(i+1,len(self.matrix)):        
                sum1=sum([self.l[j][s]*self.u[s][i] for s in range(0,i)])
                self.l[j][i]=(self.matrix[j][i]-sum1)/self.u[i][i]
            if i == len(self.matrix) - 1:
                L.append(self.l.tolist())
                U.append(self.u.tolist())

        vector = self.b
        z = self.sustprog(self.l, vector)
        x = self.sustreg(self.u, z)

        return L, U, x