########  EJERCICIO BUCLE FOR 2  ########

# Crea un programa de Python que pida 2 números por consola. El programa debe imprimir todos los números primos comprendidos 
#    entre los 2 números introducidos por consola.
# Los números primos son aquellos que solo son divisibles por 1 y por ellos mismos.
# Por ejemplo, si introducimos como primer número el 1 y como segundo número el 10, el programa imprimirá en consola todos los 
#    números primos comprendidos entre 1 y 10, esto es: 1, 2, 3, 5, 7.
# Si por el contrario, introducimos como primer número el 10 y como segundo número el 20, el programa imprimirá en consola todos 
#    los números primos comprendidos entre 10 y 20, esto es:



print ("Programa para calcular números primos")

# Pedimos los 2 números:

num1=int(input("Introduzca el primer número: "))
num2=int(input("Introduzca el segundo número: "))

# La siguiente función comprueba si el número que está recorriendo en la llamada es primo. De momento solo se define, no se ejecuta.

def es_primo(numero): # número coge aquí el valor de i 
    for n in range(2,numero): # Recorre entre 2 y sí mismo para saber si es divisible por alguno de ellos, ya que un primo sólo es divisible por 1 y por sí mismo.
        if numero % n == 0: # En el momento encuentra un divisor, al no ser primo, se sale de la función con el false y pasa al siguiente
            return False
    print(str(numero) + " es primo") # Si no se cumple la condición anterior, el número es primo. Se imprime y pasa al siguiente.
    return True

# Llamamos a la función recorriendo los números entre los 2 números definidos. Por cada uno de ellos se ejecuta el bucle
# de arriba que comprueba si es primo

for i in range(num1,num2): # Esto dice que para cada valor de i en ese rango ejecute la función es_primo tomando el valor de i como parámetro.
    es_primo(i)

# Como se puede ver, para cada valor de i en el bucle de abajo, se ejecuta el bucle de arriba dividiéndolo por todos los números entre 2 y sí mismo, 
#    e imprimiendo el valor de i si es primo.