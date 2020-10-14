from math import *

func = input("Enter function f(x) = ")
x = float(input("Enter a value that will be the starting point X0: "))
delta = float(input("Wich will be your delta/Difference: "))
it = int(input("Enter the numbers of iterations: "))

def inic():
    result=eval(func)
    return result

def sec():
    x=xa
    result=eval(func)
    return result

print('Iteraciones\tXo\tXo+d\tf(Xo)*f(xo+d)')

if inic() == 0:
    print(str(x)+" is a root")
else:
    xa=x+delta
    count=0
    result1=sec()

    while (result1*inic()>0) & (count<=it):
        x=xa
        result1=inic()
        xa=x+delta
        result1=sec()
        print(f'{count}\t\t{x:.4f}\t{xa:.4f}\t{ 1 if result1*inic() > 0 else -1 }')
        count=count+1
        
    if result1==0:
        print(str(xa)+" is a root")
    elif (inic()*result1<0):
        print("There is a root between "+str(x)+" and "+str(xa))
    else:
        print("With "+str(it)+" iterations, this method can't find a root")
