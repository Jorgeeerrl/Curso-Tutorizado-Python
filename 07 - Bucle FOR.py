
for i in [25,60,90]: # la variable contador i cuenta el número de elementos de lo que hayamos puesto, tomando ese valor a cada vuelta de bucle.
    print("Hola Alumnos")  # lo imprimirá 3 veces porque es el nº de elementos de, en este caso, la lista.

# Si introducimos la variable contador en el print imprime a cada vuelta de bucle el valor del elemento que recorre la variable en ese momento.

for meses_agno in ["Enero", "Febrero", "Marzo", "Abril"]:
    print(meses_agno)

# Usamos RANGE Para repetir un bucle x veces sin tener que crear una lista/tupla/loquesea con x elementos para recorrer:

for i in range(0,19):
    print("Hola mendrugo")
    print("Cómo te va la vida")
    print("Que te peten")

### EJERCICIO ###
    
### Crea una función que reciba dos listas por parámetros. La función debe comparar ambas listas, 
### devolviendo True si las listas son idénticas y False si no lo son.
    

def comparaListas (lista1, lista2):  # Función con parámetros.

    if(len(lista1)!=len(lista2)):  # Si tuvieran distinto nº de elementos ya no serían iguales y arrojaría el false .
        return False
    else:

        for i in range(1,len(lista1)):   # Asignamos al bucle recorrer la variable i elemento a elemento desde el 1 hasta el len que comparten ambas listas.
            if(lista1[i]!=lista2[i]): # durante el bucle i va tomando los valores de cada posición de ambas listas y viendo si son iguales.
                return False
    
    return True

alumnosA=["Juan", "Pedro", "Ana"]
alumnosB=["Juan", "Pedro", "Ana"]

print(comparaListas(alumnosA,alumnosB))