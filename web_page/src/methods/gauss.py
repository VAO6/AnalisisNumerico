class Gauss:
    def __init__(self, matrix, b):
        self.matrix=matrix
        self.b=b
        self.count=0

    def create_matrix(self, matrix):
        x = self.matrix.split(',')
        vector = self.b.split(' ')
        new_matrix = list()
        for i in range(len(x)):
            new_matrix.append(list(map(float, x[i].split(' '))))
            new_matrix[i].append(float(vector[i]))
        return new_matrix

    def multiply_line(self, multiplier, line, x):
        z = x
        for y in range(len(self.matrix)-x + 1):
            self.matrix[line][x] = self.matrix[line][x] - (multiplier * self.matrix[z][x])
            x+=1

    def change_lines(self, l1, l2):
        self.matrix[l2], self.matrix[l1] = self.matrix[l1], self.matrix[l2]

    def find_x(self):
        length = len(self.matrix)
        x_array = list()
        cont = length - 1
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * self.matrix[cont][length - 1 - y]
            x_array.append((self.matrix[length - 1 - x][length] - summ)/self.matrix[length - 1 - x][length - 1 - x])
            cont -= 1
        x_array.reverse()
        return x_array

    def run(self):
        self.matrix = self.create_matrix(self.matrix)
        A = []
        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                if self.matrix[i][i] == 0:
                    self.change_lines(i, j)
                multiplier = self.matrix[j][i]/self.matrix[i][i]
                self.multiply_line(multiplier, j, i)
                for x in range(len(self.matrix)):
                    a = []
                    for element in self.matrix[x]:
                        a.append(f'{element:.4f}')
                    if x == len(self.matrix) - 1:
                        A.append(a)
        x_vector = self.find_x()
        
        return A, x_vector