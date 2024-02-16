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


# Esto es una modificación para ver si cambia en el repositorio