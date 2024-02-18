################################# TUPLAS #################################

# Son listas INMUTABLES, no se pueden modificar.
# No permiten mover, añadir o quitar elementos (no append, extend, remove)
# El resultado de una extracción de elementos de una tupla es una nueva tupla.
# Los elementos siguen las mismas reglas de índices que en las listas.



###### TUPLAS VS LISTAS ######

# Son + rápidas de ejecutar
# Ocupan - espacio en memoria y recursos (mejor optimización)
# Formatean strings
# Pueden usarse como Claves en un diccionario.

miTupla=("Jorge","Mer","Neo","Enzo")
#          [0]    [1]   [2]    [3]   ----> ÍNDICES (Posición en la lista)
print(miTupla)

miTupla="Jorge","Mer","Neo","Enzo" # Se pueden omitir los paréntesis pero 
print(miTupla)                     # se recomiendan por visibilidad.



### CONVERTIR LISTAS Y TUPLAS ### Así podemos manipular sus elementos o protegerlos de ello, según interese.

FamiliaTupla=("Jorge","Mer","Neo","Enzo")
FamiliaLista=list(FamiliaTupla) # Convierte la Tupla en una lista y así podemos modificarla
print(FamiliaLista)

FamiliaTupla=tuple(FamiliaLista)
print(FamiliaTupla)



### OPERACIONES FRECUENTES ###

print("Neo" in FamiliaTupla) # True o False si el elemento existe o no en la tupla.

print(len(FamiliaTupla))    # Cantidad de elementos de la tupla.

print(FamiliaTupla.count("Neo")) # Cantidad de veces que aparece el elemento.

print(FamiliaTupla.index("Neo")) # Posición del elemento.



### DESEMPAQUETADO DE TUPLAS ###

# Permite almacenar en Variables de una forma rápida los valores almacenados en una Tupla.

MisDatos=("Jorge","Roncal",46,1977)
Nombre, Apellido, Edad, Nacimiento=MisDatos
print(Apellido)
print(Edad)

# Hemos almacenado esos valores en las variables Nombre, Apellido, Edad, Nacimiento, en orden.

