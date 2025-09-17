import random

puntos_vida_dragon = 100

def tirarDado(lados):
    return random.randint(1,lados)


def atacarDragon():
    ataque = tirarDado(20)+tirarDado(4)
    return ataque

puntos_vida_dragon = puntos_vida_dragon - atacarDragon()
print("Los puntos de vida del dragón son: "+str(puntos_vida_dragon))

