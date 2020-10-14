from math import *
import sympy as sym

function=input("Enter a function (natural logarithm: log(), euler: exp()): ")
x0=float(input("Enter a value that will be the starting point X0: "))
tol=10**(int(input("How many tolerance do you want: 10^: ")))
it=int(input("How many iterations do you want to make? "))
count=0
x = sym.Symbol('x')
function_d = function.replace('log', 'ln')
function_d = function.replace('exp', 'euler')
derivate = str(sym.diff(function_d, x))
derivate = derivate.replace('ln', 'log').replace('euler', 'exp')

def evaluate_function(xeval):
    x = xeval
    return eval(function)

def evaluate_derivate(xeval):
    x = xeval
    return eval(derivate)

def conditions():
    if evaluate_derivate(x) == 0:
        return False

print('Iteracion\tXi\tf(Xi)\tf\'(Xi)\tError')
enter = conditions()
while enter and count < it:
    feval = evaluate_function(x0)
    deval = evaluate_derivate(x0)
    aux = x0 - feval/deval
    error = abs(aux - x0)
    feval2 = evaluate_function(aux)
    if error < tol:
        break
    count += 1
    print(f'{count}\t\t{x0:.6f}\t{feval:.6f}\t{deval:.6f}\t{error:.6f}')
    x0 = aux
