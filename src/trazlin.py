from piv_par import Piv_par
import numpy as np

class TrazadoresLineales:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.ln = len(X)
        self.m = 2*(self.ln - 1)
        self.A = self.A()
        self.b = list(map(lambda x: 0, range(self.m)))
        self.title = ['Y'] + list(map(lambda x: 'dif(' + str(x) + ')', range(1, self.ln)))
        self.coef = np.zeros((self.ln-1,2)).tolist()

    def A(self):
        return np.zeros((self.m, self.m)).tolist()
    
    def aux(self, index):
        cont = 1
        for i in range(2*index-2, 2*index+2):
            if cont == 1:
                self.A[self.ln-1+index][i] = self.X[index]
                cont+=1
            elif cont == 2:
                self.A[self.ln-1+index][i] = 1
                cont+=1
            elif cont == 3:
                self.A[self.ln-1+index][i] = -self.X[index]
                cont+=1
            elif cont == 4:
                self.A[self.ln-1+index][i] = -1
                cont = 0
        

    def main(self):
        for i in range(self.ln-1):
            if i == 0:
                self.A[i+1][0] = self.X[i+1]
                self.A[i+1][1] = 1
            else:
                self.A[i+1][2*i] = self.X[i+1]
                self.A[i+1][2*i+1] = 1
            self.b[i+1]=self.Y[i+1]
        self.A[0][0] = self.X[0]
        self.A[0][1] = 1
        self.b[0]=self.Y[0]
        for i in range(1, self.ln-1):
            self.aux(i)
            self.b[self.ln-1+i] = 0
        pp = Piv_par(self.A, self.b)
        saux = pp.main()
        for i in range(self.ln-1):
            self.coef[i][0] = saux[2*i]
            self.coef[i][1] = saux[2*i+1]
        print('Trazadores:')
        for x in self.coef:
            print(f'{x[0]:.6f}x + {x[1]:.6f}')

if __name__ == "__main__":
    TrazadoresLineales([-1, 0, 3, 4], [15.5, 3, 8, 1]).main()

