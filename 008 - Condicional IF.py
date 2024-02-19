# Función que dice si un alumno aprueba o suspende un examen, en base al parámetro nota que pasamos al llamar a la función.

def evaluarAlumno(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspendido"
    return valoracion
       
print(evaluarAlumno(7))


######################################## INPUT ########################################

# Con INPUT podemos pedir al usuario que introduzca un valor por consola.

# Para no tener que estar modificando el print cada vez que queramos meter una nota, ponemos input
#    para hacer que el programa nos pregunte el valor por consola.

notaAlumno=int(input("La nota del alumno es: "))
print(evaluarAlumno(notaAlumno))  # Al hacer la llamada de esta manera le estamos diciendo internamente que nota=notaAlumno


########################################## ELSE ########################################

# Con ELSE también se podría. Cada Else sólo funciona con el if inmediatamente superior.

def evaluarAlumno(nota):
    valoracion="Desconocida"
    if nota<5:
        valoracion="Suspendido"
    else:
        valoracion="Aprobado"
    return valoracion

notaAlumno=int(input("La nota del alumno es: "))  # Nótese la función int()

print(evaluarAlumno(notaAlumno))


########################################## ELIF ########################################

# Si queremos encadenar estructuras if debemos usar el ELIF, y encadenaremos tantos como queramos, acabando 
#    con un else, que sólo se activará si no se cumplen ninguna de los condicionales if anteriores.


def evaluarAlumno(nota):
    valoracion="Desconocida"
    if nota<5:       
        valoracion="Suspendido"
    elif nota>10:
        valoracion="Nota incorrecta"
    else:
        valoracion="Aprobado"
    return valoracion

notaAlumno=int(input("La nota del alumno es: "))  # Nótese la función int()

print(evaluarAlumno(notaAlumno))

###############################################

print("Verificación de acceso")

nota_alumno=int(input("Introduce la nota "))

if nota_alumno<5:
    print("Suspendido")
elif nota_alumno<6:
    print("Suficiente")
elif nota_alumno<7:
    print("Bien")
elif nota_alumno<9:
    print("Notable")
else: # Sólo se activa si no se cumple ninguna de las condiciones
    print ("Sobresaliente")


##### ANIDAR CONDICIONES SIN AND/OR #####

print ("Obtención Carnet de Conducir")

edad=int(input("Introduce tu edad ")) 

if 18<=edad<90:  
    print("Puede intenar obtener el carnet")
else:
    print("Lo siento. Usted no cumple la edad")

# if 18<=edad<90:  ------>  Equivale a if edad>=18 and edad<90:
#                  ------>  Evalúa las condiciones por parejas (18<=edad, edad<90)
#                  ------>  no hay límite sobre cuantas parejas se pueden evaluar.   