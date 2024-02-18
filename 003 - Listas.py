################################# LISTAS #################################

# Son estructuras de datos que permiten almacenar gran cantidad de valores de cualquier tipo. Ej. miLista=["Jorge", 357, True, 3.14].
# En otros lenguajes, se denominan Arrays, pero los arrays contienen valores del mismo tipo.
# Se pueden expandir dinámicamente añadiendo nuevos elementos, a diferencia también de los arrays.

# Sintaxis ---> nombreLista=[elem1,elem2,elem3,...]
#                             [0]   [1]   [2]  ----> ÍNDICES (Posición en la lista)

miLista=["Jorge","Mer","Neo","Enzo"]
print(miLista) # ---> Imprime la lista completa
print(miLista[0]) # ---> Imprime el primer elemento de la lista.
print(miLista[2]) # ---> Imprime el tercer elemento de la lista.
print(miLista[-1]) # ---> Imprime el último elemento de la lista (no cuenta desde el 0).
print(miLista[-3]) # ---> Imprime el tercer elemento de la lista por la cola.

print(miLista[0:3]) # ---> Imprime una porción de la lista.
                    #      El primer dígito = posición inicial en el índice de los elementos a listar (Inclusive).
                    #      El segundo dígito = posición final en el índice de los elementos a listar (No inclusive).
                    #    Ejemplos:


miLista=["Jorge","Merche","Neo","Enzo","Pilar","Julián"]


print(miLista[1:2]) # ---> Debe imprimir 'Merche'
print(miLista[0:2]) # ---> Debe imprimir 'Jorge' y 'Merche'
print(miLista[0:3]) # ---> Debe imprimir 'Jorge', 'Merche' y 'Neo'
print(miLista[1:4]) # ---> Debe imprimir 'Merche', 'Neo' y 'Enzo'
print(miLista[2:6]) # ---> Debe imprimir 'Neo', 'Enzo', 'Pilar' y 'Julián' 
                    #      Ojo que cuando queremos el último elemento ponemos un índice que no existe, pero
                    #      al ser no inclusive, no hay problema.

print(miLista[:3])  # ---> Python entiende que empieza desde la posición [0] y listaría los 3 primeros elementos.
print(miLista[2:])  # ---> Python entiende que es hasta el final y listará los 2 últimos elementos.


print(miLista[:])   # ---> Imprime la lista completa.
print(len(miLista)) # ---> Imprime la longitud de la lista.



miLista.append("Sonia") # ---> Añade un elemento al final de la lista.
print(miLista[:])


miLista.insert(2,"Pablo") # ---> Inserta un elemento en una posición dada [2].
print(miLista[:])


miLista.remove("Pablo") # ---> Elimina un elemento de la lista. Ojo, si hay más de un Pablo, los elimina todos.
print(miLista[:])


miLista.extend(["Pablo","Nacho","Begoña"]) # ---> Concatena listas. La amplía. Añade nuevos elementos en forma 
print(miLista[:])                          # ---> de una nueva lista al final de la existente.


print(miLista.index("Nacho")) # ---> Imprime la posición del elemento 'Nacho' [8].
                              # ---> Si el elemento no existe, arroja un error.
                              # ---> Si el elemento se repite, imprime la posición del primero.


print(miLista.count("Nacho")) # ---> Imprime la cantidad de veces que aparece el elemento 'Nacho' [1].


miLista.pop()     # ---> Elimina el último elemento de la lista.
print(miLista[:])


miLista.sort()    # ---> Ordena la lista de menor a mayor.
print(miLista[:])


miLista.reverse() # ---> Revierte la lista.
print(miLista[:])
miLista.reverse() # ---> Revierte la lista.
print(miLista[:])


print("Jorge" in miLista) # ---> Imprime True o False si el elemento existe o no en la lista.


del miLista[8] # ---> Elimina el elemento de la lista en la posición [8].
print(miLista[:])


##### UNIÓN DE LISTAS #####

miLista=["Jorge","46","Neo","12"]
miLista2=["Pilar","65"]

miLista3=miLista+miLista2
print(miLista3[:])

###  Repetir listas ###

miLista4=["Jorge","Mer","Neo","Enzo"]*3
print(miLista4[:])







