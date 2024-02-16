import random

random_num=random.randint(1,100)
# print(random_num) ---> Si dejamos esta línea se puede ver el número aleatorio en la consola

user_num=int(input("Introduzca un número entre 1 y 100: "))
intentos=1

while random_num!=user_num:

    if user_num<random_num:
        print("El número aleatorio es mayor")
        user_num=int(input("Introduzca un número: "))

    else:
        print("El número alatorio es menor")
        user_num=int(input("Introduzca un número: "))

    intentos=intentos+1


print("El número era el " + str(random_num) + " y ha necesitado " + str(intentos) + " intentos")
