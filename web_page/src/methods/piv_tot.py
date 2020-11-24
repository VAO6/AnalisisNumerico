class Piv_tot:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.b = vector
            
    def create_matrix(self, matrix):
        x = matrix.split(',')
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

    def change_columns(self, col1, col2):
        for line in self.matrix:
            line[col1], line[col2] = line[col2], line[col1]


    def substract_lines(self, first_line, second_line):
        for x in range(len(self.matrix[first_line])):
            self.matrix[first_line][x] = self.matrix[first_line][x] - self.matrix[second_line][x]

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
        change_lines_index = list()
        A = []
        for m in range(len(self.matrix)):
            a=0
            b=0
            maximun=self.matrix[m][m]
            for i in range(m, len(self.matrix)):
                for j in range(m, len(self.matrix)):
                    if(abs(self.matrix[i][j])>=abs(maximun)):
                        maximun=self.matrix[i][j]
                        a=i
                        b=j
                        
            for y in range(m, len(self.matrix)):
                for p in range(m, len(self.matrix)):
                    if(y==p):
                        self.change_columns(y,b)
                        change_lines_index.append((y,b))
                        self.change_lines(y,a)
                    break
                break
            for n in range(m+1 ,len(self.matrix)):
                multiplier= self.matrix[n][m]/self.matrix[m][m]
                self.multiply_line(multiplier,n,m)
                for x in range(len(self.matrix)):
                    a = []
                    for element in self.matrix[x]:
                        a.append(f'{element:.4f}')
                    if x == len(self.matrix) - 1:
                        A.append(a)

        x_vector = self.find_x()
        for element in change_lines_index:
            x_vector[element[0]], x_vector[element[1]] = x_vector[element[1]], x_vector[element[0]]  
        
        return A, x_vector