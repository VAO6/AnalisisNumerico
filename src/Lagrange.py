import numpy as np
import sympy as sym

a=input('Enter the values that correspond to the x axis, separeted by a space. (Example: 1 1.1 1.2): ')
b=input('Enter the values that are the result of the function evaluated in Xi, separated by a space. (Example: 1 2 3): ')

def create_xi(xi):
    return list(map(float, xi.split(' ')))

xi=create_xi(a)
fi=create_xi(b)

n = len(xi)
x = sym.Symbol('x')
polyn = 0
dividerL = np.zeros(n, dtype = float)
for i in range(0,n,1):
    numerator = 1
    denominator = 1
    for j  in range(0,n,1):
        if (j!=i):
            numerator = numerator*(x-xi[j])
            denominator = denominator*(xi[i]-xi[j])
    placeLi = numerator/denominator
    polyn = polyn + placeLi*fi[i]
    dividerL[i] = denominator

polyn_red = polyn.expand()

print('Expanded Lagrange polynomial: ')
print(polyn)
print()
print('Lagrange Polynomial: ')
print(polyn_red)

