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
# function_d = function_g.replace('log', 'ln')
# function_d = function_g.replace('exp', 'euler')
first_derivate = str(sym.diff(function_g, x))
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

from math import *
import sympy as sym
from sympy.solvers import solve


class Fixed_Point:
        
    def __init__(self, functionf, functiong, a, b, iterations, error):
        self.function_f = functionf
        self.function_g = functiong
        self.a = float(a)
        self.b = float(b)
        self.iterations = int(iterations)
        self.error = 10**(error)
        self.iterations_counter = 0
        self.x = sym.Symbol('x')
        self.function_d = self.function_g.replace('log', 'ln')
        self.function_d = self.function_g.replace('exp', 'euler')
        self.first_derivate = str(sym.diff(self.function_g, self.x))
        self.second_derivate = str(sym.diff(self.first_derivate, self.x))
        

    def replace(self, function):
        replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            'log':'np.log',
            '^': '**',
        }

        for old, new in replacements.items():
            if old in function:
                function = function.replace(old, new)
        return function


    def evaluate(self, function, xeval):
        x = xeval
        return eval(function)

    def condition(self):
        if not self.evaluate(self.function_g, self.a) >= self.a and not self.evaluate(self.function_g, self.a) <= self.b:
            return False
        if not self.evaluate(self.function_g, self.b) >= self.a and not self.evaluate(self.function_g, self.b) <= self.b:
            return False
        for x in self.critic_points(self.first_derivate):
            if not self.evaluate(self.function_g, x) >= self.a and not self.evaluate(self.function_g, x) <= self.b:
                return False
        for x in self.critic_points(self.second_derivate):
            if not self.evaluate(self.first_derivate, x) < 1:
                return False
        return True


    def critic_points(self, function):
        critic_points = list()
        x = sym.Symbol('x')
        critic = solve(function, x)
        for x in critic:
            critic_points.append(eval(str(x).replace('I', '1')))
        return critic_points
    
    def run(self):
        imprimir = [' Iteration        xi         f(xi)        error    ']
        enter=self.condition()
        xaux=self.a
        while self.iterations_counter < self.iterations and enter:
            xi=self.evaluate(self.function_g, xaux)
            fx = self.evaluate(self.function_f, xi)
            if abs(self.evaluate(self.function_g, xaux)-self.evaluate(self.function_g,xi))<self.error and self.iterations_counter != 0:
                break
            self.iterations_counter += 1
            imprimir.append(f'{self.iterations_counter:^12}{xi:^12.6f}{fx:^12.6f}{self.error:^12.6f}')
            aux = xi
        return imprimir

fp=Fixed_Point('exp(x-10.5)+sin(x)+x*3-2x', 'exp(x-10.5)+sin(x)+x*3-x',-1,0, 100,-7)
print(fp.run())
