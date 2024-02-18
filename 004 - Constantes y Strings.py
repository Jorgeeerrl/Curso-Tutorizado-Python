# Las CONSTANTES como tal no existen, y se definen en mayúsculas
# Se suelen declarar en un módulo externo que luego se inserta en el programa principal. 

PI=3.1416
GRAVEDAD=9.8

### CONCATENACIÓN DE STRINGS ### ---> Son cadenas de caracteres y se concatenan con el signo +

print("Mi nombre es " + "Jorge")

nombre="Jorge"
print("Mi nombre es " + nombre)

# edad=18
# print("Mi edad es " + edad) # Esto da error porque sólo se pueden concatenar strings y edad es un valor numérico.

edad="18"
print("Mi edad es " + edad) # Así sí se podría porque ya es tipo string.


# str() convierte en string lo que incluyamos en el paréntesis. Así también concatenaríamos strings y valores numéricos.

edad=18
print("Mi edad es " +str(edad)+" años")

salario=2500
comision=1500
print("Mi sueldo total es "+str(salario+comision)) # Nótese que aquí el + no está concatenando, actúa como operador de suma.

