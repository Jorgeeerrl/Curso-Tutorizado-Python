####################################### CONTINUE #######################################

# Se utiliza para que cuando el bucle llegue a cierta condición, salte esa vuelta y continúe en la siguiente.
# Queremos contar el número de caracteres de una cadena de texto

nombre= "Jorge Roncal"

contador=0

for i in nombre:

    contador+=1 # Esto es lo mismo que poner: "contador=contador +1" gracias al +=

print(contador)

# Aquí nos imprimiría 9 porque el espacio cuenta como un carácter
# Si queremos que no lo cuente podemos usar el CONTINUE

contador=0

for i in nombre:

    if i==" ":
        continue # Aquí le decimos que si el elemento es un espacio, salte a la siguiente vuelta de bucle y no incremente el contador.
    
    contador+=1

print(contador)



################################## PASS ##################################

# Se utiliza de forma temporal, cuando debes definir una estructura pero de momento no queremos desarrollar lo que hace.

for i in nombre:

    pass # Aquí pondremos un pass para no hacer nada de momento.

class EjemploClase:

    pass # Aquí pondremos un pass para no hacer nada de momento.



################################## ELSE ##################################

# Programa para saber si un correo electrónico tiene arroba.

email=input("Introduce tu correo electrónico: ")

for i in email:  # Recorremos la cadena de texto.
    if i=="@": # Si el elemento es un arroba.
        arroba=True
        break # Salimos del bucle en cuanto la encuentra, no hace falta recorrerlo todo.
else: 
    arroba=False

# Este else pertenece al for. Se ejecuta si ha terminado de recorrer todo el bucle. 
# Si la encuentra, al no terminar el recorrido y salirse por el break no se ejecuta el else.
# Si no la encuentra, como lo ha recorrido todo, se ejecuta el else.

print(arroba)