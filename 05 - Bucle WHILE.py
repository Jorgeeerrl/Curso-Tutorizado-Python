
contador=0

while contador<10:
    print("Hola")
    contador=contador+1  # si elimináramos esta línea entraría en un bucle infinito

print("Hemos salido del bucle")

# Otro ejemplo

edad=int(input("Introduce tu edad: "))  # Solo queremos admitir valores positivos

while edad<0 or edad>100:
    print("Has introducido una edad negativa no válida") # nos dice que la edad es negativa y no válida
    edad=int(input("Introduce tu edad: ")) # nos vuelve a preguntar que ingresemos la edad

print("Gracias, puedes pasar")
print("Edad del usuario " + str(edad))

# BREAK rompe el bucle

while edad<0 or edad>100:
    print("Has introducido una edad negativa no válida") # nos dice que la edad es negativa y no válida
    edad=int(input("Introduce tu edad: ")) # nos vuelve a preguntar que ingresemos la edad
    break

print("Gracias, puedes pasar")
print("Edad del usuario " + str(edad))

# Queremos hacer la raiz cuadrada de un número que nos pedirá el programa. Los negativos no tienen
# raíz cuadrada. Queremos un máximo de 3 intentos.

import math  # importamos el módulo math de funciones matemáticas

print("Hayando la raíz cuadrada de un valor número")

numero=int(input("Introduce un número: "))

intentos=1  # ponemos 1 ya que hemos realizado ya uno

while numero<0:
    print("El número es negativo")
    numero=int(input("Introduce un número: "))
    intentos=intentos+1
    if intentos==3:
        break

if intentos==3:
    print("Lo siento. No se puede hacer el cálculo")

else:
    print(math.isqrt(numero))  # Utilizamos la función isqrt para calcular la raíz cuadrada