from math import *
import sympy as sym

print('This is the method to evaluate "Raices multiples"')
function = input("Enter the function f(x) = ")
x0 = float(input("Enter the starting point (x0)): "))
iterations = int(input("Enter the number of maximum iterations: "))
error = 10**(int(input("How many tolerance do you want: 10^: ")))
iterations_counter = 0
x = sym.Symbol('x')
function_d = function.replace('log', 'ln')
function_d = function.replace('exp', 'euler')
first_derivate = str(sym.diff(function_d, x))
first_derivate =  first_derivate.replace('ln', 'log').replace('euler', 'exp')
second_derivate = str(sym.diff(first_derivate, x))
second_derivate =  second_derivate.replace('ln', 'log').replace('euler', 'exp')

def evaluate_function(function, xeval):
    x = xeval
    return eval(function)

print('Iteration\tXi\t\tf(Xi)\t\tf\'(Xi)\t\tf\'\'(Xi)\t\tError')
xaux = x0
while iterations_counter < iterations:
    xn = xaux - ((evaluate_function(function, xaux)*evaluate_function(first_derivate, xaux))/(evaluate_function(first_derivate, xaux)**2 - (evaluate_function(function, xaux)*evaluate_function(second_derivate, xaux))))
    xerror = abs(evaluate_function(function, xaux)-evaluate_function(function, xn))
    print(f'{iterations_counter}\t\t{xaux:.6f}\t{evaluate_function(function, xaux):.6f}\t{evaluate_function(first_derivate, xaux):.6f}\t{evaluate_function(second_derivate, xaux):.6f}\t{xerror if iterations_counter != 0 else 0:.6f}')
    xaux = xn
    if xerror < error and iterations_counter != 0:
        break
    iterations_counter += 1