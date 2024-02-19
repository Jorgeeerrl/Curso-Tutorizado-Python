# Los tramos impositivos de un país en concreto son los que figuran en la siguiente tabla:

#        Renta	                Tipo impositivo
# Menos de 12000€	                  7%
# Entre 12000€ y 18000€	             15%
# Entre 18000€ y 35000€	             21%
# Entre 35000€ y 70000€	             35%
# Mas de 70000€	                     45%

# Crea un programa que pregunte por consola la renta. En función de la renta introducida, el programa devolverá el texto:
#   “A la renta (aquí iría la renta introducida) le corresponde un (aquí iría el tipo impositivo) de tipo impositivo.
# Ejemplo: En caso de introducir por consola 13500, el programa devolverá el texto: “A la renta 13500 le corresponde un 
#    15% de tipo impositivo”.
# El programa debe permitir la introducción de rentas decimales.


print("Cálculo Impositivo según renta")
renta=float(input("Introduzca su renta anual: "))
if renta>70000:
    print("Su tipo impositivo es el 45%")
elif renta>=35000:
    print("Su tipo impositivo es el 35%")
elif renta>=18000:
    print("Su tipo impositivo es el 21%")
elif renta>=12000:
    print("Su tipo impositivo es el 15%")
else:
    print("Su tipo impositivo es el 7%")