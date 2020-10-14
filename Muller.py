import math
from UI.functions.Function import Function
import numpy

class Muller:

    def __init__(self,):
        pass

    def sign(self,value):
        return value/abs(value)
    def evaluate(self,x1,x2,x3,function_string,tol,steps) -> float:
        #Checks for any invalid values
        function_eval = Function(function_string)
        if (tol > 1 and tol < 0):
            return None 
        
        #initializing variables
        h = x3 - x2
        y1 = function_eval.evaluate(x1)
        y2 = function_eval.evaluate(x2)

        for k in range(steps):
            y3 = function_eval.evaluate(x3)
            a = (y3-y2)/h
            b = (y1-y3)/(x1-x3)
            b = b-a
            b = b/(x1-x2)
            c = a +(b*h)
            q = c**2-(4*y3*b)
            if q<0: q=0
            h = -2*y3/(c+self.sign(c)*math.sqrt(q))
            print(f"{k}||{x3}||{y3}||{h}")
            if abs(h) < tol:
                print (f"la raiz es {x3}, encontrada en la iteracion {k}")
                return
            x1 = x2
            x2 = x3
            x3 = x3+h
            y1 = y2
            y2 = y3
        print("metodo paro con el maximo de pasos")
        return


x = Muller()
x.evaluate(7,8,9,"2*x**3-2*x-5",0.001,100)
print(x.evaluate.__annotations__['return'])