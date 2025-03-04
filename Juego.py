import random 
print ("Bienvenido a Black Jack")

numeros = [1,2,3,4,5,6,7,10,10,10]
cantidad = [4,4,4,4,4,4,4,4,4,4]

palos = ["Bastos", "Copas", "Oros", "Espada"]
baraja = []

for palo in palos:
    for numero in numeros:
        baraja.append(f"{numero} de {palo}")


def barajar():
    random.shuffle(baraja)

    return baraja.copy()

def mano(repartir):
    print("Mano de jugador: ")
    return repartir.pop()
print (mano())
