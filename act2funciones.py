
# Importar el módulo random.
import random
# Crear una variable llamada puntos_vida_dragon 
# donde se guarden los puntos de vida del dragón (por ejemplo: 100)
puntos_vida_dragon = 100
# Crear la función tirarDado() que reciba un parámetro llamado lados. 
#   Dentro de la función:
#       Deberás retornar un valor aleatorio, entre 1 y 
#       el argumento recibido en el parámetro lados. 
#       Para esto deberás utilizar el módulo random con el método .randint()
def tirarDado(lados):
    return random.randint(1,lados)

# Crear la función atacarDragon() sin argumento. 
# Dentro de la función:
#     Deberás crear una variable llamada ataque 
#     que almacene la suma de tirar 
#     un dado de 20 lados más uno de 4 lados.
#     Por último, deberá retornar el valor 
#     contenido en la variable ataque
def atacarDragon():
    ataque = tirarDado(20)+tirarDado(4)
    return ataque

puntos_vida_dragon = puntos_vida_dragon - atacarDragon()
print("Los puntos de vida del dragón son: "+str(puntos_vida_dragon))
# Sobreescribir el valor de la variable puntos_vida_dragon 
# restando el ataque realizado. 
# Para esto deberás asignar a la variable: 
# su valor original - atacarDragon().
# Hacer un print() con el texto 
# "Los puntos de vida del dragón son: ______".
