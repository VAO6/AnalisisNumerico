class diferenciasDivididas:

    def __init__(self, X, Y):
        self.X = list(map(float, X.split(' ')))
        self.Y = list(map(float, Y.split(' ')))
        self.ln = len(self.X)
        self.matrix_d()
        self.title = ['Y'] + list(map(lambda x: 'dif(' + str(x) + ')', range(1, self.ln)))

    def matrix_d(self):
        self.matrix_d = list()
        for x in range(self.ln):
            self.matrix_d.append(list())
            for y in range(self.ln):
                if y == 0:
                    self.matrix_d[x].append(self.Y[x])
                else:
                    self.matrix_d[x].append(0)
        return self.matrix_d

    def auxy(self, index):
        aux = list()
        aux2 = list()
        for i in range(index, self.ln):
            aux.append(self.matrix_d[i][index])
        for j in range(self.ln - index - 1):
            aux2.append(aux[j+1] - aux[j])
        return aux2
    
    def auxx(self, index):
        aux = list()
        for i in range(self.ln - index - 1):
            aux.append(self.X[i+1+index]-self.X[i])
        return aux
        

    def run(self):
        imprimir = []
        for i in range(1, self.ln):
            auxy = self.auxy(i - 1)
            auxx = self.auxx(i - 1)
            for j in range(self.ln - i):
                self.matrix_d[j+i][i] = auxy[j]/auxx[j]
        coef = list(map(lambda x: self.matrix_d[x][x], range(self.ln)))
        tit = []
        for title in self.title:    
            tit.append(title)
        imprimir.append(tit)
        for x in self.matrix_d:
            tit = []
            for element in x:
                tit.append(element)
            imprimir.append(tit)
        x = coef
        polinomio = []
        
        for y in range(len(coef)):
            pol = []
            if y == 0:
                pol.append(f'{coef[y]:.6f} ')
            else:
                pol.append((' ' if coef[y] < 0 else ' + ') + f'{coef[y]:.6f}')
                for j in range(y):
                    pol.append('(x'+ ('+' if self.X[y] >= 0 else '')+str(self.X[j])+')')
            polinomio.append(pol)
        return imprimir, x, polinomio