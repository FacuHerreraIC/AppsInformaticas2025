# Importar el módulo random.
import random 
# Crear las variables num1, num2, num3, num4 y num5, 
# donde cada una guarde un número aleatorio generado con la 
# función random.randint(0, 20) para generar un número aleatorio entre 0 y 20 (ambos incluidos).
num1 = random.randint(0,20)
num2 = random.randint(0,20)
num3 = random.randint(0,20)
num4 = random.randint(0,20)
num5 = random.randint(0,20)
# Hacer un print() de cada variable para mostrar su valor.
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
# Sumar los números generados y guardar el resultado en una variable llamada total.
# Hacer un print() con el texto "La suma de los números generados es: " y concatenar el resultado de la suma.
total = num1+num2+num3+num4+num5
print("La suma de los números generados es: "+str(total))