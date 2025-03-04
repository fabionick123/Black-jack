import random
class Carta:
    valor = [1,2,3,4,5,6,7,10,10,10]
    cantidad = [4,4,4,4,4,4,4,4,4,4]

    mano = []

    

    def __init__(self, palo, valor, nombre):
        self.palo = palo
        self.valor = valor
        self.nombre = nombre
    def __str__(self):
        return f"{self.nombre}"