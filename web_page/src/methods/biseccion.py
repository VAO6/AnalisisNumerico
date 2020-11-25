from math import *
class Biseccion:
    def __init__(self, function, a, b, iterations, error):
        self.function = function
        self.a = float(a) 
        self.b = float(b)
        self.iterations = int(iterations)
        self.error = 10**(error)
        self.iterations_counter = 0

    def condition(self):
        if self.evaluate(self.a) * self.evaluate(self.b) >= 0:
            return False
        return True
    
    def evaluate(self, parameter):
        x = parameter
        res = eval(self.function)
        return res

    def punto_medium(self, a, b):
        return 1 if self.evaluate(a) * self.evaluate(b) < 0 else -1

    def run(self):
        imprimir = []
        if not self.condition():
            imprimir.append('Error -> Doesnt pass the minimum conditions.')
            return imprimir
        imprimir = [' Iteration      a           Xm          b       f(a)*f(Xm)    Error    ']
        medium = (self.a+self.b)/2
        enter = self.condition()
        while enter and self.iterations_counter < self.iterations:
            aux = medium
            medium = (self.a+self.b)/2
            pto_medium = self.punto_medium(self.a, medium)
            if pto_medium == 1:
                self.b = medium
            else:
                self.a = medium
            if abs(medium-aux) < self.error and self.iterations_counter != 0:
                break
            self.iterations_counter += 1
            imprimir.append(f'{self.iterations_counter:^12}{self.a:^12.4f}{medium:^12.4f}{self.b:^12.4f}{pto_medium:^12}{abs(medium-aux):^12.4f}')
        return imprimir

