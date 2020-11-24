class Piv_par:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.b = vector

    def create_matrix(self, matrix):
        new_matrix = list()
        if type(self.matrix) is not list:
            x = self.matrix.split(',') 
            vector = self.b.split(' ')
            for i in range(len(x)):
                new_matrix.append(list(map(float, x[i].split(' '))))
                new_matrix[i].append(float(vector[i]))
        else:
            x = 0
            for element in self.matrix:
                new_matrix.append(element)
            x = 0
            for element in new_matrix:
                element.append(self.b[x])
                x+=1
        return new_matrix

    def multiply_line(self,multiplier, line, x):
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
            x_array.append((self.matrix[length - 1 - x][length] - summ)/self.matrix[length - 1 - x][length - 1 - x] if self.matrix[length - 1 - x][length - 1 - x] != 0 else 0)
            cont -= 1
        x_array.reverse()
        return x_array

    def run(self):
        self.matrix = self.create_matrix(self.matrix)
        A = []
        for i in range(len(self.matrix)):
            for j in range(i+1, len(self.matrix)):
                aux=0
                if(abs(self.matrix[i][i])<abs(self.matrix[j][i])):
                    self.change_lines(i,j)

            for p in range(i+1,len(self.matrix)):
                multiplier = self.matrix[p][i]/self.matrix[i][i]
                self.multiply_line(multiplier, p, i)
                for x in range(len(self.matrix)):
                    a = []
                    for element in self.matrix[x]:
                        a.append(f'{element:.4f}')
                    if x == len(self.matrix) - 1:
                        A.append(a)
                
        x_vector = self.find_x()
        return A, x_vector