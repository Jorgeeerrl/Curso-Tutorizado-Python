def evaluarAlumno(nota):
    valoracion="Aprobado"
    if nota<5:
        valoracion="Suspendido"
    return valoracion
       

print(evaluarAlumno(7))

# Para no tener que estar modificando el print cada vez en el código introducimos la orden input para
# hacer que el programa nos pregunte el valor por consola

notaAlumno=int(input("La nota del alumno es: "))
print(evaluarAlumno(notaAlumno))  # Al hacer la llamada de esta manera le estamos diciendo internamente que nota=notaAlumno

#con else también se podría:

def evaluarAlumno(nota):
    valoracion="Desconocida"
    if nota<5:
        valoracion="Suspendido"
    else:
        valoracion="Aprobado"
    return valoracion

notaAlumno=int(input("La nota del alumno es: "))  # Nótese la función int()

print(evaluarAlumno(notaAlumno))

# Si queremos encadenar estructuras if debemos usar el elif, y encadenaremos tantos como queramos,
# acabando con un else, que sólo se activará si no se cumplen ninguna de los condicionales if anteriores.


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
else:
    print ("Sobresaliente")

# Anidar condiciones prescindiendo del and

print ("Obtención Carnet de Conducir")

edad=int(input("Introduce tu edad ")) 

if 18<=edad<90:  # Equivale a if edad>=18 and edad<90:
    print("Puede intenar obtener el carnet")
else:
    print("Lo siento. Usted no cumple la edad")

