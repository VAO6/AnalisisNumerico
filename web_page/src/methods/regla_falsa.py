class ReglaFalsa:
    def __init__(self, function, a, b, iterations, error):
        self.function = function
        self.a = float(a) 
        self.b = float(b)
        self.iterations = int(iterations)
        self.error = 10**(error)
        self.iterations_counter = 0

    def condition(self):
        if self.evaluate(self.a) * self.evaluate(self.b) >= 0:
            return ['No cumple con los parámetros del método. Error.']
    
    def evaluate(self, parametro):
        x = parametro
        res = eval(self.function)
        return res

    def punto_medio(self, a, b):
        return 1 if self.evaluate(self.a) * self.evaluate(self.b) < 0 else -1

    def run(self):
        imprimir = []
        self.condition()
        imprimir.append(' Iteracion      a           Xm          b       f(a)*f(Xm)     Error   ')
        medio = (self.a+self.b)/2

        while True and self.iterations_counter < self.iterations:
            aux = medio
            medio = self.a - ((self.evaluate(self.a)*(self.b - self.a))/(self.evaluate(self.b) - self.evaluate(self.a)))
            
            pto_medio = self.punto_medio(self.a, medio)
            if pto_medio == 1:
                self.b = medio
            else:
                self.a = medio
            if abs(medio-aux) < self.error and self.iterations_counter != 0:
                break
            self.iterations_counter += 1
            imprimir.append(f'{self.iterations_counter:^12}{self.a:^12.4f}{medio:^12.4f}{self.b:^12.4f}{pto_medio:^12}{abs(medio-aux):^12.4f}')
        return imprimir
                