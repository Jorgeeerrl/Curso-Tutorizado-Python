# El programa permite al usuario ingresar información sobre países y sus ciudades asociadas. 
# Utiliza un bucle while para solicitar al usuario que introduzca el nombre de un país y luego la ciudad correspondiente. 
# La información se almacena en un diccionario llamado CiudadesPaises, donde las claves son los países y los valores son 
# listas de ciudades asociadas a cada país. El programa continúa solicitando la entrada del usuario hasta que se ingresa 
# "salir". Finalmente, imprime el diccionario con la información recopilada sobre los países y ciudades.

paises = []
CiudadesPaises = {}

pais = input("Introduce el país: ")

while pais != "salir":
    ciudad = input("Introduce la ciudad: ")

    if pais not in CiudadesPaises:
        CiudadesPaises[pais] = [ciudad]  # Añade el elemento pais:ciudad al diccionario y establece que los valores son listas.
        paises.append(pais) # Añade el país a la lista de paises para comprobar si los nuevos paises que ponemos ya existen en el diccionario.
    else:
        CiudadesPaises[pais].append(ciudad) # Esto añade la ciudad a la lista-valor que corresponde a la clave-país.

    pais = input("Introduce el país (o escribe 'salir' para terminar): ")

print(CiudadesPaises)