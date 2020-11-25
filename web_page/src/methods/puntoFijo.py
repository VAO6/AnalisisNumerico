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
        self.first_derivate = str(sym.diff(self.function_d, self.x))
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
            xaux = xi
        return imprimir