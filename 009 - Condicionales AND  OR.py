################################################### AND #############################################

# AND anida condiciones y obliga a que se cumplan todas para que se ejecute el resto de las instrucciones.

print("Obtención Carnet de Conducir")

edad=int(input("Introduce tu edad: "))
vision=input("Ves correctamente? (si/no): ")

if edad>=18 and edad<90 and vision=="si":
    print("Puedes intentar obtenerlo")
else:
    print("Lo siento. Te jodes")



################################################### OR #############################################

# OR anida condiciones y obliga que se cumpla al menos una de las condiciones.

print("Obtención Beca de Estudios")

nota_media=int(input("Introduce tu nota media: "))
hermanos_en_centro=int(input("Introduce Nº de Hermanos en el Centro: "))
distancia_al_centro=int(input("Introduce distancia: "))
renta_familiar=int(input("Introduce tu renta anual: "))

if nota_media>8 or hermanos_en_centro>3 or distancia_al_centro>10 or renta_familiar<20000:
    print("Obtienes la Beca")
else:
    print("Te jodes")



####################################################################################################

# Se pueden combinar entre ellos de cualquier manera. 
# Por ejemplo cambiamos la línea de condicionales por una combinación de and, or y operadores lógicos (los paréntesis):

print("Obtención Beca de Estudios")

nota_media=int(input("Introduce tu nota media: "))
hermanos_en_centro=int(input("Introduce Nº de Hermanos en el Centro: "))
distancia_al_centro=int(input("Introduce distancia: "))
renta_familiar=int(input("Introduce tu renta anual: "))

if (nota_media>8 and hermanos_en_centro>3) and (distancia_al_centro>10 or renta_familiar<20000):
    print("Obtienes la Beca")
else:
    print("Te jodes")

# Primero ejecutaría cada paréntesis arrojando un Frue o False, y luego entrararía en juego el and que une ambos paréntesis.