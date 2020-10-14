from math import *
import sympy as sym
from sympy.solvers import solve

print('This is the method to evaluate "Punto Fijo"')
function_f = input("Enter the function f(x) = ")
function_g = input("Enter the function g(x) = ")
a = float(input("Enter the inferior limit (a): "))
b = float(input("Enter the superior limit (b): "))
iterations = int(input("Enter the number of maximum iterations: "))
error = 10**(int(input("How many tolerance do you want: 10^: ")))
iterations_counter = 0
x = sym.Symbol('x')
function_d = function_g.replace('log', 'ln')
function_d = function_g.replace('exp', 'euler')
first_derivate = str(sym.diff(function_d, x))
second_derivate = str(sym.diff(first_derivate, x))

def condicion():
    if not evaluate_function(function_g, a) >= a and not evaluate_function(function_g, a) <= b:
        return False
    if not evaluate_function(function_g, b) >= a and not evaluate_function(function_g, b) <= b:
        return False
    for x in critic_points(first_derivate):
        if not evaluate_function(function_g, x) >= a and not evaluate_function(function_g, x) <=b:
            return False
    for x in critic_points(second_derivate):
        if not evaluate_function(first_derivate, x) < 1:
            return False
    return True
    
    
def critic_points(function):
    critic_points = list()
    x = sym.Symbol('x')
    critic = solve(function, x)
    for x in critic:
        critic_points.append(eval(str(x).replace('I', '1')))
    return critic_points
   
def evaluate_function(function, xeval):
    x = xeval
    return eval(function)

print('Iteration\tXi\tf(Xi)\tError')
enter = condicion()
xaux = a
while iterations_counter < iterations and enter:
    xi = evaluate_function(function_g, xaux)
    fx = evaluate_function(function_f, xi)
    if abs(evaluate_function(function_g, xaux)-evaluate_function(function_g, xi)) < error and iterations_counter != 0:
        break
    iterations_counter += 1
    print(f'{iterations_counter}\t\t{xi:.6f}\t{fx:.6f}\t{error:.6f}')
    xaux = xi
