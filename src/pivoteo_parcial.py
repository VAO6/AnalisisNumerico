from math import *

matrix=input("Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3): ")
b=input("Enter the vector B separated by spaces. Example: (1 1 1): ")

def create_matrix(matrix):
    x = matrix.split(',')
    vector = b.split(' ')
    new_matrix = list()
    for i in range(len(x)):
        new_matrix.append(list(map(float, x[i].split(' '))))
        new_matrix[i].append(float(vector[i]))
    return new_matrix

def multiply_line(multiplier, line):
    x = 0
    for element in matrix[line]:
        matrix[line][x] = element * multiplier
        x+=1

def change_lines(l1, l2):
    matrix[l2], matrix[l1] = matrix[l1], matrix[l2]


def substract_lines(first_line, second_line):
    for x in range(len(matrix[first_line])):
        matrix[first_line][x] = matrix[first_line][x] - matrix[second_line][x]

def find_x():
    length = len(matrix)
    x_array = list()
    cont = length - 1
    for x in range(length):
        summ = 0
        for y in range(len(x_array)):
            summ += x_array[y] * matrix[cont][length - 1 - y]
        x_array.append((matrix[length - 1 - x][length] - summ)/matrix[length - 1 - x][length - 1 - x])
        cont -= 1
    x_array.reverse()
    return x_array

matrix = create_matrix(matrix)

for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        aux=0
        if(abs(matrix[i][i])>abs(matrix[j][i])):
            matrix[i][i]=matrix[i][i]
        else:
            change_lines(i,j)

    for p in range(i+1,len(matrix)):
        multiplier = matrix[i][i]/matrix[p][i]
        multiply_line(multiplier, p)
        substract_lines(p,i)
        print('A = [\n')
        for x in range(len(matrix)):
            for element in matrix[x]:
                print(f'{element:.6f}\t\t', sep=' ', end='')
            print('\n')
        print(']\n=====================\n')
        
x_vector = find_x()
print('x = [\n', x_vector, '\n]')
