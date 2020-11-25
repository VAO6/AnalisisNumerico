from math import *
import numpy as np

class Secant:
    def __init__(self, function, a, b, iterations, error):
        self.function = function
        self.a = float(a) 
        self.b = float(b)
        self.iterations = int(iterations)
        self.error = 10**(error)
        self.iterations_counter = -1

    def replace(self):
        replacements = {
            'sin' : 'np.sin',
            'cos' : 'np.cos',
            'exp': 'np.exp',
            'sqrt': 'np.sqrt',
            'log':'np.log',
            '^': '**',
        }

        for old, new in replacements.items():
            if old in self.function:
                self.function = self.function.replace(old, new)

    def evaluate(self, parameter):
        x = parameter
        res = eval(self.function)
        return res

    #  def condition(self):
    #     if self.evaluate(self.a) - self.evaluate(self.b) != 0:
    #         return False
    #     return True

    # if not self.condition():
    #         imprimir.append('Error -> Doesnt pass the minimum conditions.')
    #         return imprimir

    def run(self):       
        imprimir = [' Iteration       x0          x1         f(x)       error    ']
        self.replace()
        while self.iterations_counter < self.iterations:
            feval = self.evaluate(self.a)
            feval_1=self.evaluate(self.b)
            
            rest1=self.b-self.a
            rest2=feval_1-feval
            aux = self.b - feval_1 * rest1/rest2
            error = abs(aux - self.a)
            feval2 = self.evaluate(aux)
            if error < self.error:
                break
            self.iterations_counter += 1
            # print(f'{self.iterations_counter}\t\t{self.a:.6f}\t{self.b:.6f}\t{feval_1:.6f}\t{error:.6f}')
            imprimir.append(f'{self.iterations_counter:^12}{self.a:^12.6f}{self.b:^12.6f}{feval_1:^12.6f}{error:^12.6f}')
            self.a = self.b
            self.b = aux
            
        return imprimir
