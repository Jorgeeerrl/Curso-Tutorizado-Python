# IN se utiliza para realizar búsquedas dentro de una lista:

Trabajadores=["Paula", "Manuel", "Pedro", "Ana", "Sandra"]

if "Pedro" in Trabajadores:
    print("Sí, Pedro está en la lista")
else:
    print("Pedro no se ha encontrado en la lista")

# o búsquedas dentro de un string:

Lenguajes_Trim1="Java, Python, PHP, C#, HTML"

if "PHP" in Lenguajes_Trim1:
    print("PHP está")
else:
    print("PHP no está")

# o búsquedas de carácteres concretos:

if "#" in Lenguajes_Trim1:
    print("# Está")
else:
    print("No está")


# NOT se utiliza para justo lo contrario

if "SQL" not in Lenguajes_Trim1:
    print("No está en la lista")
else:
    print("Está en la lista")


if not "SQL" in Lenguajes_Trim1:  # También así, aunque es menos natural
    print("No está en la lista")