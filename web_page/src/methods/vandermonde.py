from piv_par import Piv_par
import numpy as np

matrix=input('Enter the values that correspond to the x axis, separeted by a space. (Example: 1 1.1 1.2): ')
y=input('Enter the values that are the result of the function evaluated in Xi, separated by a space. (Example: 1 2 3): ')

def matrix_x(matrix):
    x = list(map(float, matrix.split(' ')))
    n = len(x)
    new_matrix = list()
    for y in range(n):
        new_matrix.append(list())
        for z in range(n):
            new_matrix[y].append(x[y]**(n-1-z))
    return new_matrix

def vector_b(b):
    return list(map(float, b.split(' ')))

X = matrix_x(matrix)
Y = vector_b(y)

print('Matriz de vandermonde\n')
for x in range(len(X)):
    for element in X[x]:
        print(f'{element:.6f}\t\t', sep=' ', end='')
    print('\n')
print('\n=====================\n')

pp = Piv_par(X, Y)
x = pp.main()
print('\nPolinomio\n')
for y in range(len(x)):
    print(f'{x[y]:.6f}x^' + str(len(x) - y) + (' + ' if x[y] < 0 else ' '), sep=' ', end='')