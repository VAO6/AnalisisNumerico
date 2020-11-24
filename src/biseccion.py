from math import *

funcion = input("Enter function f(x) = ")
a = float(input("Enter the upper limit (a): "))
b = float(input("Enter the lower limit (b): "))
iterations = int(input("Enter the numbers of iterations: "))
error = 10**(int(input("How many tolerance do you want: 10^: ")))
iterations_counter = 0

def condition():
    if evaluate(a) * evaluate(b) >= 0:
        print('Error -> Doesnt pass the minimum conditions.')
        return False
    return True
   
def evaluate(parameter):
    x = parameter
    res = eval(funcion)
    return res

def punto_medium(a, b):
    return 1 if evaluate(a) * evaluate(b) < 0 else -1

print('Iteration\ta\tXm\tb\tf(a)*f(Xm)\tError')
medium = (a+b)/2
enter = condition()
while enter and iterations_counter < iterations:
    aux = medium
    medium = (a+b)/2
    pto_medium = punto_medium(a, medium)
    if pto_medium == 1:
        b = medium
    else:
        a = medium
    if abs(medium-aux) < error and iterations_counter != 0:
        break
    iterations_counter += 1
    print(f'{iterations_counter}\t\t{a:.4f}\t{medium:.4f}\t{b:.4f}\t{pto_medium}\t\t{abs(medium-aux):.4f}')