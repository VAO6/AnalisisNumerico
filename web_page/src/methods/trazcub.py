from math import *
from .piv_par import Piv_par
import numpy as np

class TrazadoresCubicos:

    def __init__(self, X, Y):
        self.X = list(map(float, X.split(' ')))
        self.Y = list(map(float, Y.split(' ')))
        self.ln = len(self.X)
        self.m = 4*(self.ln - 1)
        self.A = self.A()
        self.b = list(map(lambda x: 0, range(self.m)))
        self.coef = np.zeros((self.ln-1,4)).tolist()

    def A(self):
        return np.zeros((self.m, self.m)).tolist()
    
    def aux(self, index):
        cont = 1
        for i in range(4*index-4, 4*index+4):
            if cont == 1:
                self.A[self.ln-1+index][i] = self.X[index]**3
                cont+=1
            elif cont == 2:
                self.A[self.ln-1+index][i] = self.X[index]**2
                cont+=1
            elif cont == 3:
                self.A[self.ln-1+index][i] = self.X[index]
                cont+=1
            elif cont == 4:
                self.A[self.ln-1+index][i] = 1
                cont +=1
            elif cont == 5:
                self.A[self.ln-1+index][i] = -self.X[index]**3
                cont+=1
            elif cont == 6:
                self.A[self.ln-1+index][i] = -self.X[index]**2
                cont += 1
            elif cont == 7:
                self.A[self.ln-1+index][i] = -self.X[index]
                cont+=1
            elif cont == 8:
                self.A[self.ln-1+index][i] = -1
                cont = 1
    
    def aux2(self, index):
        cont = 1
        for i in range(4*index-4, 4*index+4):
            if cont == 1:
                self.A[2*self.ln-3+index][i] = 3*self.X[index]**2
                cont+=1
            elif cont == 2:
                self.A[2*self.ln-3+index][i] = self.X[index]*2
                cont+=1
            elif cont == 3:
                self.A[2*self.ln-3+index][i] = 1
                cont+=1
            elif cont == 4:
                self.A[2*self.ln-3+index][i] = 0
                cont+=1
            elif cont == 5:
                self.A[2*self.ln-3+index][i] = -3*self.X[index]**2
                cont+=1
            elif cont == 6:
                self.A[2*self.ln-3+index][i] = -self.X[index]*2
                cont+=1
            elif cont == 7:
                self.A[2*self.ln-3+index][i] = -1
                cont+=1
            elif cont == 8:
                self.A[2*self.ln-3+index][i] = 0
                cont=1
        
    
    def aux3(self, index):
        cont = 1
        for i in range(4*index-4, 4*index+4):
            if cont == 1:
                self.A[3*self.ln-5+index][i] = self.X[index]*6
                cont+=1
            elif cont == 2:
                self.A[3*self.ln-5+index][i] = 2
                cont+=1
            elif cont == 3:
                self.A[3*self.ln-5+index][i] = 0
                cont+=1
            elif cont == 4:
                self.A[3*self.ln-5+index][i] = 0
                cont+=1
            elif cont == 5:
                self.A[3*self.ln-5+index][i] = -self.X[index]*6
                cont+=1
            elif cont == 6:
                self.A[3*self.ln-5+index][i] = -2
                cont+=1
            elif cont == 7:
                self.A[3*self.ln-5+index][i] = 0
                cont+=1
            elif cont == 8:
                self.A[3*self.ln-5+index][i] = 0
                cont=1
    

    def run(self):
        trazadores = []
        for i in range(self.ln-1):
            if i == 0:
                self.A[i+1][0] = self.X[i+1]**3
                self.A[i+1][1] = self.X[i+1]**2
                self.A[i+1][2] = self.X[i+1]
                self.A[i+1][3] = 1
            else:
                self.A[i+1][4*i] = self.X[i+1]**3
                self.A[i+1][4*i+1] = self.X[i+1]**2
                self.A[i+1][4*i+2] = self.X[i+1]
                self.A[i+1][4*i+3] = 1
            self.b[i+1]=self.Y[i+1]
        self.A[0][0] = self.X[0]**3
        self.A[0][1] = self.X[0]**2
        self.A[0][2] = self.X[0]
        self.A[0][3] = 1
        self.b[0]=self.Y[0]
        for i in range(1, self.ln-1):
            self.aux(i)
            self.b[self.ln-1+i] = 0
        for i in range(1, self.ln-1):
            self.aux2(i)
            self.b[2*self.ln-3+i] = 0
        for i in range(1, self.ln-1):
            self.aux3(i)
            self.b[2*self.ln-3+i] = 0
        self.A[self.m-2][0] = self.X[0]*6
        self.A[self.m-2][1] = 2
        self.b[self.m-2] = 0
        self.A[self.m-1][self.m-4] = self.X[self.ln-1]*6
        self.A[self.m-1][self.m-3] = 2
        self.b[self.m-1] = 0
        pp = Piv_par(self.A, self.b)
        A, saux = pp.run()
        for i in range(self.ln-1):
            self.coef[i][0] = saux[4*i]
            self.coef[i][1] = saux[4*i+1]
            self.coef[i][2] = saux[4*i+2]
            self.coef[i][3] = saux[4*i+3]
        for x in self.coef:
            trazadores.append(f'{x[0]:.6f}x^3 + {x[1]:.6f}x^2 + {x[2]:.6f}x + {x[3]:.6f}')

        return saux, trazadores