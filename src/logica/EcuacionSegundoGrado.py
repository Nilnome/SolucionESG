import math
class EcuacionSegundoGrado:
    def calculoECS(self, a, b, c):
        discriminante = math.pow(b, 2) - 4 * a * c
        if discriminante >= 0:
            raizdisciminante = math.sqrt(discriminante)
            x1 = (-b + raizdisciminante) / ( 2 * a)
            x2 = (-b - raizdisciminante) / ( 2 * a)
            return x1, x2
        else :
            return None, None
