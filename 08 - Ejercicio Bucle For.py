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