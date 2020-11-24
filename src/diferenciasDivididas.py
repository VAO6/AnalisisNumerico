import sys

class diferenciasDivididas:

    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.ln = len(X)
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
        

    def main(self):
        for i in range(1, self.ln):
            auxy = self.auxy(i - 1)
            auxx = self.auxx(i - 1)
            for j in range(self.ln - i):
                self.matrix_d[j+i][i] = auxy[j]/auxx[j]
        coef = list(map(lambda x: self.matrix_d[x][x], range(self.ln)))
        for title in self.title:    
            print(title + '\t\t\t', sep=' ', end='')
        print('\n')
        for x in self.matrix_d:
            for element in x:
                print(f'{element:.6f}\t\t', sep=' ', end='')
            print('\n')
        print(']\n=====================\n')
        print('x = [\n', coef, '\n]')

        print('\nPolinomio\n')
        for y in range(len(coef)):
            if y == 0:
                print(f'{coef[y]:.6f} ', sep=' ', end='')
            else:
                print((' ' if coef[y] < 0 else ' + ') + f'{coef[y]:.6f}', sep=' ', end='')
                for j in range(y):
                    print('(x'+ ('+' if self.X[y] < 0 else '-')+str(self.X[y])+')', sep=' ', end='')

if __name__ == "__main__":
    diferenciasDivididas([-1, 0, 3, 4], [15.5, 3, 8, 1]).main()
