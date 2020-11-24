from math import *
import sympy as sym

class Newton:
    def __init__(self, function, x, tol, iterations):
        self.function = function
        self.x0 = float(x) 
        self.tol = 10**(tol)
        self.it = int(iterations)
        self.count=0
        self.x = sym.Symbol('x')
        self.function_d = self.function.replace('log', 'ln')
        self.function_d = self.function.replace('exp', 'euler')
        self.derivate = str(sym.diff(self.function_d, self.x))
        self.derivate = self.derivate.replace('ln', 'log').replace('euler', 'exp')

    def evaluate_function(self, xeval):
        x = xeval
        return eval(self.function)

    def evaluate_derivate(self, xeval):
        x = xeval
        return eval(self.derivate)

    def conditions(self):
        if self.evaluate_derivate(self.x0) == 0:
            return False
        return True

    def run(self):
        imprimir = []
        imprimir.append('Iteracion\tXi\tf(Xi)\tf\'(Xi)\tError')
        enter = self.conditions()
        while enter and self.count < self.it:
            feval = self.evaluate_function(self.x0)
            deval = self.evaluate_derivate(self.x0)
            aux = self.x0 - feval/deval
            error = abs(aux - self.x0)
            feval2 = self.evaluate_function(aux)
            if error < self.tol:
                break
            self.count += 1
            imprimir.append(f'{self.count:^12}{self.x0:^12.6f}\t{feval:^12.6f}\t{deval:^12.6f}\t{error:^12.6f}')
            self.x0 = aux
        return imprimir

