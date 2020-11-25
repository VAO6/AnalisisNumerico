from math import *
import sympy as sym

class Multiple_roots:

    def __init__(self, function, a, iterations, error):
        self.function = function
        self.a = float(a)
        self.iterations = int(iterations)
        self.error = 10**(error)
        self.iterations_counter = 0
        self.x = sym.Symbol('x')
        self.function_d = self.function.replace('log', 'ln')
        self.function_d = self.function.replace('exp', 'euler')
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

    def run(self):
        imprimir = [' Iteration      xi           f(xi)          f\'(xi)        f\'\'(Xi)      Error    ']
        xaux = self.a
        while self.iterations_counter < self.iterations:
            if (self.evaluate(self.first_derivate, xaux)**2 - (self.evaluate(self.function, xaux)*self.evaluate(self.second_derivate, xaux)))==0:
                imprimir.append('This method cant be applied under the entered parameters')
                break
            xn = xaux - ((self.evaluate(self.function, xaux)*self.evaluate(self.first_derivate, xaux))/(self.evaluate(self.first_derivate, xaux)**2 - (self.evaluate(self.function, xaux)*self.evaluate(self.second_derivate, xaux))))
            xerror = abs(self.evaluate(self.function, xaux)-self.evaluate(self.function, xn))
            imprimir.append(f'{self.iterations_counter}{xaux:.6f}{self.evaluate(self.function, xaux):.6f}{self.evaluate(self.first_derivate, xaux):.6f}{self.evaluate(self.second_derivate, xaux):.6f}{xerror if self.iterations_counter != 0 else 0:.6f}')
            xaux = xn
            if xerror < self.error and self.iterations_counter != 0:
                break
            self.iterations_counter += 1
        return imprimir
