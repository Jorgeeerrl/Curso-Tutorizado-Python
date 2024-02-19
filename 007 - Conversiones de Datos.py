################## FUNCIONES PREDEFINIDAS ##################

# int() ------> Transforma un texto en un número entero
# float() ----> Transforma un texto en un número flotante
# str() ------> Transforma un número en un texto
# join() -----> Transforma una lista en un texto
# split() ----> Transforma un texto en una lista


############ EJEMPLOS ############

a="15"
b="35"
print(a+b)  # 1535 - Junta las dos cadenas de caracteres.
print(int(a)+int(b))  # 50 - Transforma los strings en enteros y ejecuta la operación.

a="15.25"
b="25.35"
print(float(a)+float(b))  # 40.60 - Transforma los strings en decimales y ejecuta la operación.

edad=25
print("mi Edad es "+str(edad)+" años") # Transforma la variable en string y lo concatena todo.

empleados=["Jorge","Javier","Jesús"]
print(" ".join(empleados)) # Entre comillas indicamos el método de separación de los elementos.

empleados="Ana, Pedro, Juan"
print(empleados.split())