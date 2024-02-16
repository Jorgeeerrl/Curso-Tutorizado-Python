# Programa que pide dos números y calcula los números primos que hay entre ellos

print ("Programa para calcular números primos")

# Pedimos los 2 números:

num1=int(input("Introduzca el primer número: "))
num2=int(input("Introduzca el segundo número: "))

# Esta función comprueba si el número que está recorriendo en la llamada es primo. De momento solo se define, luego se llamará.
def es_primo(numero): # número coge aquí el valor de i 
    for n in range(2,numero): # Recorre entre 2 y sí mismo para saber si es divisible por alguno de ellos, ya que un primo sólo es divisible por 1 y por sí mismo.
        if numero % n == 0: # En el momento encuentra un divisor, al no ser primo, se sale de la función con el false y pasa al siguiente
            return False
    print(str(numero) + " es primo") # Si no se cumple la condición anterior, el número es primo y se imprime.
    return True

# Llamamos a la función recorriendo los números entre los 2 números definidos. Por cada uno de ellos se ejecuta el bucle
# de arriba que comprueba si es primo

for i in range(num1,num2):
    es_primo(i)

