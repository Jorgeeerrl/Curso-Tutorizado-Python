### EJERCICIO ###
    
# Crea una función que reciba dos listas por parámetros. La función debe comparar ambas listas, devolviendo True si
#   las listas son idénticas y False si no lo son.

def comparaListas (lista1, lista2):  # Función con parámetros. Solo la definimos de momento.

    if(len(lista1)!=len(lista2)):  # Si tuvieran distinto nº de elementos ya no serían iguales y arrojaría el false .
        return False
    else:

        for i in range(1,len(lista1)): # Asignamos al bucle recorrer la variable i elemento a elemento desde el 1 hasta el len que comparten ambas listas.
            if(lista1[i]!=lista2[i]):  # Durante el bucle i va tomando los valores de cada posición de ambas listas y viendo si son iguales.
                return False
    
    return True

alumnosA=["Juan", "Pedro", "Ana"]
alumnosB=["Juan", "Pedro", "Ana"]

print(comparaListas(alumnosA,alumnosB)) # Aquí la llamamos pasando como parámetros las listas. 

# De esta manera es mejor porque es más reutilizable, pero también podríamos haber creado las listas lo primero y haber hecho la 
#   función comparaListas con sus nombres en los parámetros:

lista1=["Juan", "Pedro", "Ana"]
lista2=["Juan", "Pedro", "Ana"]

def comparaListas(lista1, lista2): 

    if(len(lista1)!=len(lista2)):  
        return False
    else:

        for i in range(1,len(lista1)): 
            if(lista1[i]!=lista2[i]):  
                return False
    
    return True

print(comparaListas(lista1,lista2))