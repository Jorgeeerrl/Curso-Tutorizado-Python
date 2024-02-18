# Son estructuras de datos que almacenan valores de sistinto tipo, e incluso listas, tuplas y otros dicionarios.
# Los datos se almacenan asociados a una clave, creándose una asociación clave:valor para cada elemento almacenado.
# Los elementos almacenados no están ordenados, pq al tener una clave individual para acceder a su valor, esto carece de importancia.
# Sería similar a una tabla de 2 columnas de una base de datos:

# Clave:valor
# España:Madrid
# Francia:Toulousse
# Inglaterra:Londres
# Italia:Roma
# Portugal:Lisboa

# Sintaxis -----> diccionario = {clave1:valor1,clave2:valor2,clave3:valor3,...}

Capitales={"Espana":"Madrid", "Francia":"Toulousse", "Inglaterra":"Londres", "Italia":"Roma", "Portugal":"Lisboa"}



Capitales["Colombia"]="Bogotá" # Agrega un elemento al diccionario.

Capitales["Francia"]="París" # Modifica un elemento del diccionario.

print(Capitales)

del Capitales["Colombia"] # Elimina un elemento del diccionario.

print(Capitales)


### UTILIZAR TUPLAS COMO CLAVES EN UN DICCIONARIO ###

claveCapitales=("España","Francia","Inglaterra","Italia","Portugal") # Creamos una Tupla
capitalesMundo={claveCapitales[0]:"Madrid",claveCapitales[1]:"París",claveCapitales[2]:"Londres",claveCapitales[3]:"Roma",claveCapitales[4]:"Lisboa"}
print(capitalesMundo)


### OPERACIONES CON DICCIONARIOS ###

print(capitalesMundo["Inglaterra"]) # Imprime el valor de la clave "Inglaterra"

print(capitalesMundo.keys()) # Imprime un listado con las claves del diccionario.

print(capitalesMundo.values()) # Imprime un listado con los valores del diccionario.

print(capitalesMundo.items()) # Imprime los elementos del diccionario.

print(len(capitalesMundo)) # Imprime la longitud del diccionario, el nº de elementos.



########## DICCIONARIOS ANIDADOS ##########

datosJordan={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":[1991,1992,1993,1996,1997,1998]}
print(datosJordan)

# Hemos anidado una lista al diccionario, asignándole a la clave Anillos la lista como valor.

# También podríamos incluir otro diccionario como clave en lugar de la lista.

datosEquipo = {23: "Jordan", "Nombre": "Michael", "Historia": {"Temporadas": 15, "Puntos": 32292, "Asistencias": 5633}}
print(datosEquipo["Historia"])
print(datosEquipo["Historia"]["Asistencias"]) # Así puedes ir recorriendo las claves y subclaves para solicitar un valor concreto.


print(datosEquipo.keys())
print(datosEquipo.values())
print(datosEquipo.items())