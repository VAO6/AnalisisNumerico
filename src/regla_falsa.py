from math import *

function = input("Enter function f(x) = ")
a = float(input("Enter the upper limit (a): "))
b = float(input("Enter the lower limit (b): "))
iterations = int(input("Introduce numero de iterations: "))
error = float(input('Introduce el error de aceptacion: '))
iterations_counter = 0

def condition():
    if evaluate(a) * evaluate(b) >= 0:
        print('No cumple con los parámetros del método. Error.')
        return
    print('Cumple con la condición f(a) * f(b) < 0')
   
def evaluate(parametro):
    x = parametro
    res = eval(function)
    return res

def punto_medio(a, b):
    return 1 if evaluate(a) * evaluate(b) < 0 else -1

print(evaluate(a))
condition()
print('Iteracion\ta\tXm\tb\tf(a)*f(Xm)\tError')
medio = (a+b)/2

while True and iterations_counter < iterations:
    aux = medio
    medio = a - ((evaluate(a)*(b - a))/(evaluate(b) - evaluate(a)))
    
    pto_medio = punto_medio(a, medio)
    if pto_medio == 1:
        b = medio
    else:
        a = medio
    if abs(medio-aux) < error and iterations_counter != 0:
        break
    iterations_counter += 1
    print(f'{iterations_counter}\t\t{a:.4f}\t{medio:.4f}\t{b:.4f}\t{pto_medio}\t\t{abs(medio-aux):.4f}')
        