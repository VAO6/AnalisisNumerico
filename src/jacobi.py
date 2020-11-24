import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

matrix=input("Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3): ")
b=input("Enter the vector B separated by spaces. Example: (1 1 1): ")
x0=list(map(float, input("Enter X0: ").split(' ')))
tol=10**(int(input("How many tolerance do you want: 10^: ")))
it=int(input("How many iterations do you want to make? "))


def create_matrix(matrix):
    x = matrix.split(',')
    new_matrix = list()
    for i in range(len(x)):
        new_matrix.append(list(map(float, x[i].split(' '))))
    return new_matrix

def vector_b(b):
    return list(map(float, b.split(' ')))

def matrix_d(matrix):
    matrix_d = list()
    for x in range(len(matrix)):
        matrix_d.append(list())
        for y in range(len(matrix)):
            if x == y:
                matrix_d[x].append(matrix[x][y])
            else:
                matrix_d[x].append(0)
    return matrix_d

def matrix_u(mA, mD):
    return sum_matrix(minus_triangular_upper(mA), mD)

def matrix_l(mA, mD):
    return sum_matrix(minus_triangular_lower(mA), mD)

def matrix_t(mD, mL, mU):
    md = np.array(mD)
    md = inv(md)
    return np.matmul(md, np.array(sum_matrix(mL, mU))).tolist()

def matrix_c(mD, b):
    md = inv(np.array(mD)).tolist()
    return multiply_matrix(md, b)

def multiply_matrix(matrix, vector):
    new_vector = list()
    for line in matrix:
        summ = 0
        for y in range(len(matrix)):
            summ += line[y] * vector[y]
        new_vector.append(summ)
    return new_vector

def sum_matrix(m1, m2):
    length = len(m1)
    new_matrix = list()
    for x in range(length):
        if type(m1[0]) == list:
            new_matrix.append(list())
            for y in range(length):
                if type(m1[0]) == list:
                    new_matrix[x].append((m1[x][y] + m2[x][y]))
        else:
            new_matrix.append(m1[x] + m2[x])
    return new_matrix

def substract_matrix(m1, m2):
    length = len(m1)
    new_matrix = list()
    for x in range(length):
        if type(m1[0]) == list:
            new_matrix.append(list())
            for y in range(length):
                if type(m1[0]) == list:
                    new_matrix[x].append((m1[x][y] - m2[x][y]))
        else:
            new_matrix.append(m1[x] - m2[x])
    return new_matrix

def sum_matrix_vector(m1, vector):
    length = len(m1)
    new_matrix = list()
    for element in m1:
        new_matrix.append(list())
        for y in range(length):
            new_matrix[y].append((element[y] + vector[y]))
    return new_matrix

def minus_triangular_upper(matrix):
    matrix_d = list()
    for x in range(len(matrix)):
        matrix_d.append(list())
        for y in range(len(matrix)):
            if x <= y:
                matrix_d[x].append(-matrix[x][y])
            else:
                matrix_d[x].append(0)
    return matrix_d

def minus_triangular_lower(matrix):
    matrix_d = list()
    for x in range(len(matrix)):
        matrix_d.append(list())
        for y in range(len(matrix)):
            if x >= y:
                matrix_d[x].append(-matrix[x][y])
            else:
                matrix_d[x].append(0)
    return matrix_d

def list_to_vector(listt):
    return list(map(lambda x: [x], listt))

matrix = create_matrix(matrix)
matrix_d = matrix_d(matrix)
matrix_u = matrix_u(matrix, matrix_d)
matrix_l = matrix_l(matrix, matrix_d)
matrix_t = matrix_t(matrix_d, matrix_l, matrix_u)
vector_b = vector_b(b)
matrix_c = matrix_c(matrix_d, vector_b)
xant = x0
E = 1000
cont=0

print('T = [\n')
for x in range(len(matrix_t)):
    for element in matrix_t[x]:
        print(f'{element:.6f}\t\t', sep=' ', end='')
    print('\n')
print(']\n=====================\n')
print('C = [\n')
for element in matrix_c:
    print(f'{element:.6f}\t\t', sep=' ', end='')
print('\n')
print(']\n=====================\n')
print('| iter |      E     |\n')

while E > tol and cont<it:
    xact=sum_matrix(matrix_c, multiply_matrix(matrix_t, xant))
    E = LA.norm(np.array(substract_matrix(xant, xact)))
    xant = xact
    cont += 1
    print(f'|  {cont}   |   {E:.1e}  | ', sep=' ', end='')
    for x in xact:
        print(f'{x:.6f} ',  sep=' ', end='')
    print('\n')
    

x = xact
it = cont
err = E

print('x = [\n', x, '\n]')
print('it = [\n', it, '\n]')
print('err = [\n', err, '\n]')