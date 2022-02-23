import math

#criando a classe
class Equacao:
    a = 0
    b = 0
    c = 0

    #metodo consrtutor
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    #metodo para encontrar Delta e as raizes
    def equacao(a, b, c):
        d = pow(b, 2) - 4*a*c
        x1 = (-b + math.sqrt(d)) / 2*a
        x2 = (-b - math.sqrt(d)) / 2*a
        return x1,x2

    


