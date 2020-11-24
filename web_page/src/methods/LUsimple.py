class LUSimple:
    def __init__(self, matrix, vector):
        self.matrix = matrix
        self.b = vector
        self.count = 0

    def create_matrix(self, matrix):
        x = matrix.split(',')
        new_matrix = list()
        for i in range(len(x)):
            new_matrix.append(list(map(float, x[i].split(' '))))
        return new_matrix

    def vector_b(self, b):
        return list(map(float, b.split(' ')))

    def matrix_u(self, matrix):
        matrix_u = list()
        for x in range(len(matrix)):
            matrix_u.append(list())
            for y in range(len(matrix)):
                matrix_u[x].append(0)
        return matrix_u

    def matrix_l(self, matrix):
        matrix_l = list()
        for x in range(len(matrix)):
            matrix_l.append(list())
            for y in range(len(matrix)):
                if x == y:
                    matrix_l[x].append(1)
                else:
                    matrix_l[x].append(0)
        return matrix_l

    def multiply_line(self, multiplier, line, x):
        z = x
        for y in range(len(self.matrix)-x):
            self.matrix[line][x] = self.matrix[line][x] - (multiplier * self.matrix[z][x])
            x+=1

    def change_lines(self, l1, l2):
        self.matrix[l2], self.matrix[l1] = self.matrix[l1], self.matrix[l2]

    def sustreg(self, matrix, b):
        length = len(matrix)
        x_array = list()
        cont = length - 1
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * matrix[cont][length - 1 - y]
            x_array.append((b[length - 1 - x] - summ)/matrix[length - 1 - x][length - 1 - x])
            cont -= 1
        x_array.reverse()
        return x_array

    def sustprog(self, matrix, b):
        length = len(matrix)
        x_array = list()
        cont = 0
        for x in range(length):
            summ = 0
            for y in range(len(x_array)):
                summ += x_array[y] * matrix[cont][y]
            x_array.append((b[x] - summ)/matrix[x][x])
            cont += 1
        return x_array

    def run(self):
        matrix = self.create_matrix(self.matrix)
        matrix_l = self.matrix_l(matrix)
        matrix_u = self.matrix_u(matrix)

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                multiplier = matrix[j][i]/matrix[i][i]
                matrix_l[j][i] = multiplier
                self.multiply_line(multiplier, j, i)
            for x in range(i, len(matrix[0])):
                matrix_u[i][x] = matrix[i][x]
                if x+1 < len(matrix[0]):
                    matrix_u[i+1][x+1] = matrix[i+1][x+1]
            print('Etapa ' + str(i) + '\n')
            print('A = [\n')
            for x in range(len(matrix)):
                for element in matrix[x]:
                    print(f'{element:.6f}\t\t', sep=' ', end='')
                print('\n')
            print(']\n=====================\n')
            print('L = [\n')
            for x in range(len(matrix)):
                for element in matrix_l[x]:
                    print(f'{element:.6f}\t\t', sep=' ', end='')
                print('\n')
            print(']\n=====================\n')
            print('U = [\n')
            for x in range(len(matrix)):
                for element in matrix_u[x]:
                    print(f'{element:.6f}\t\t', sep=' ', end='')
                print('\n')
            print(']\n=====================\n')

        matrix_u[len(matrix)-1][len(matrix)-1] = matrix[len(matrix)-1][len(matrix)-1]
                    
        vector_b = self.vector_b(self.b)
        z = self.sustprog(matrix_l, vector_b)
        x = self.sustreg(matrix_u, z)
        print('z = [\n', z, '\n]')
        print('x = [\n', x, '\n]')