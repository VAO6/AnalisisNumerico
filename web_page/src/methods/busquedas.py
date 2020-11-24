class Busquedas:
    def __init__(self, function, x, delta, iterations):
        self.func = function
        self.x = float(x) 
        self.delta = float(delta)
        self.it = int(iterations)

    def inic(self):
        x = self.x
        result=eval(self.func)
        return result

    def sec(self, xa):
        x = xa
        result=eval(self.func)
        return result

    def run(self):
        # imprimir = [' Iteraciones      Xo         Xo+d     f(Xo)*f(xo+d)']
        imprimir = []
        imprimir.append(' Iteraciones      Xo         Xo+d     f(Xo)*f(xo+d)')

        if self.inic() == 0:
            imprimir.append(str(self.x)+" is a root")
        else:
            xa=self.x+self.delta
            count=0
            result1=self.sec(xa)

            while (result1*self.inic()>0) & (count<=self.it):
                self.x=xa
                result1=self.inic()
                xa=self.x+self.delta
                result1=self.sec(xa)
                imprimir.append(f'{count:^12}{self.x:^12.4f}{xa:^12.4f}{str(1 if result1*self.inic() > 0 else -1)}')
                count=count+1
                
            if result1==0:
                imprimir.append(str(xa)+" is a root")
            elif (self.inic()*result1<0):
                imprimir.append("There is a root between "+str(self.x)+" and "+str(xa))
            else:
                imprimir.append("With "+str(self.it)+" iterations, this method can't find a root")
        
        return imprimir