from math import *
import numpy as np

matrix=input("Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3): ")
b=input("Enter the vector B separated by spaces. Example: (1 1 1): ")

def create_matrix(matrix):
    x = matrix.split(',')
    new_matrix = list()
    for i in range(len(x)):
        new_matrix.append(list(map(float, x[i].split(' '))))
    return new_matrix

def vector_b(b):
    return list(map(float, b.split(' ')))

def sustreg(matrix, b):
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

def sustprog(matrix, b):
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
    
matrix = create_matrix(matrix)
l=np.identity(len(matrix))
u=np.identity(len(matrix))

print('Etapa 0: ')
print(matrix)
for i in range(0,len(matrix)):
    l[i,i]=1
    print('Etapa'+str(i+1))
    for j in range(i,len(matrix)):
        sum0=sum([l[i][s]*u[s][j] for s in range(0,j)])
        u[i][j]=matrix[i][j]-sum0
    for j in range(i+1,len(matrix)):        
        sum1=sum([l[j][s]*u[s][i] for s in range(0,i)])
        l[j][i]=(matrix[j][i]-sum1)/u[i][i]
    print('L=')
    print(l)
    print('U=')
    print(u)
    print()

    
vector_b = vector_b(b)
z = sustprog(l, vector_b)
x = sustreg(u, z)

print('After applying progressive and regressive substitution')
print()
print('x = [\n', x, '\n]')    

# Matriz de vandermonde

# 0.125000                0.250000                0.500000        1.000000

# 1.000000                1.000000                1.000000        1.000000

# 27.000000               9.000000                3.000000        1.000000

# 125.000000              25.000000               5.000000        1.000000