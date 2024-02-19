###########################################  MÉTODO  .setdefault  ####################################################

# .setdefault - Nos muestra el valor de una clave. Crea un valor si no existe la clave.
# busca una clave y si existe arroja su valor, y si no existe arroja como valor lo que ponemos en 2º lugar en el ().

miDiccionario={"España":"Madrid", "Francia":"Paris", "Inglaterra":"Londres"}

valor=miDiccionario.setdefault("España","No existe la clave") # valor almacena el valor de la clave "España".
print(valor)  # Arrojará "Madrid".

valor=miDiccionario.setdefault("Colombia","No existe la clave") # valor almacenará el mensaje que hemos creado.
print(valor)  # Arrojará "No existe la clave".

valor=miDiccionario.setdefault("Ciudades del mundo",["Londres","Roma","Helsinki","Berlín"])
print(valor)  # Ahora devuelve una lista con las 4 ciudades pq la clave Suecia no existe.
print(miDiccionario)  # Al hacerlo vemos que ha agregado lasa dos últimas parejas como elementos nuevos.
                      # Esta es otra de las utilidades de .setdefault, AGREGAR ELEMENTOS QUE NO EXISTEN AL DICCIONARIO.

# De esta manera podemos crear un diccionario vacío e ir agragándole elementos:

miDiccionario={}

miDiccionario.setdefault("Ciudades del mundo",["Londres","Roma","Helsinki","Berlín"])
miDiccionario.setdefault("Más ciudades del mundo",["Pekín","Valencia","Munich","Milán"])
print(miDiccionario)


# Aplicando esto último al ejercicio anterior tenemos otra posible solución:

paises={}

pais=input("Introduce el país: ") # España

while pais!="salir":
    
    ciudad=input("Introduce ciudad: ") # Valencia

    lista_ciudades=paises.setdefault(pais,[ciudad]) # 1- Le pregunta al diccionario paises la clave almacenada en pais
                                                    #    y la guarda en la lista lista_ciudades.
                                                    # 2- Si la clave no existe la añade al diccionario como un nuevo elemento con el 
                                                    # valor [ciudad], que es una lista que contendrá todas las ciudades que compartan esa clave.
    if lista_ciudades!=[ciudad]: # Comprueba si la lista lista_ciudades es diferente de la almacenada en el diccionario
                                 # para esa clave concreta. Si lo fuera querría decir que la ciudad nueva no estaba en la lista-valor de ese pais.
        paises[pais].append(ciudad) # Si lo es, añade la ciudad.
    
    pais=input("Introduce el país: ")  # Si fuera igual, es decir, no fuera diferente, no añadiría nada y pasaría a aquí, 
                                       #    para después volver a comprobar si es != a salir.

print(paises)



