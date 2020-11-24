from math import *

function=input("Enter a function (natural logarithm: log(), euler: exp()): ")
x0=float(input("Enter a value that will be the first aprocimation X0: "))
x1=float(input("Enter a value that will be the second aproximation X1: "))
tol=10**(int(input("How many tolerance do you want: 10^: ")))
it=int(input("How many iterations do you want to make? "))
count=-1

def evaluate_function(xeval):
    x = xeval
    return eval(function)

print('Iteracion\tXi\t\tf(Xi)\t\tError')
while True and count < it:
    feval = evaluate_function(x0)
    feval_1=evaluate_function(x1)
    rest1=x1-x0
    rest2=feval_1-feval
    aux = x1 - feval_1 * rest1/rest2
    error = abs(aux - x0)
    feval2 = evaluate_function(aux)
    if error < tol:
        break
    count += 1
    print(f'{count}\t\t{x0:.6f}\t{feval_1:.6f}\t{error:.6f}')
    x0 = x1
    x1 = aux
