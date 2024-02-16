# El símbolo # indica que es un comentario y no se ejecutará
# Python es "Case Sensitive", es decir, distingue entre mayúsculas y minúsculas.
# Todo son Objetos (variables, funciones, Todo)
# El texto o string siempre va "entrecomillado". Pueden ser '' o "" o ''' '''. Las triples permiten saltos de línea.
# El símbolo \ indica un salto de línea y así puedes separar una instrucción en varias líneas.
# El símbolo ; encadena varias instrucciones en una sola línea.
    # Ésto es una Indentación.


### VARIABLES ###

# Para definir (asignarle un valor) una variable se utiliza el símbolo = y se permite minúsculas, mayúsculas, _ y números.
# A asignarle el primer valor a una variable se le denomina INICIALIZARLA o iniciar la variable. 

nombre="Jorge"  # La acabamos de iniciar


### FUNCIONES ###

# Son un conjunto de líneas de código (Bloque de código) que funciona como una unidad para realizar una tarea específica.
# Pueden devolver valores
# Pueden tener Parámetros (Argumentos)
# Se denominan Métodos cuando están definidas en una clase

# Primero se declara la función
# Sintaxis ---> def nombre_funcion(parámetros):
#                   instrucción 1
#                   instrucción 2
#                   return (Si devuelve valores)

def suma():
    numero1=10
    numero2=20
    print(numero1+numero2)

# Una vez definida la función, la llamamos cuando queramos poniendo simplemente su nombre

suma()

### FUNCIÓN CON PARÁMETROS ###
def suma(num1,num2):
    print(num1+num2)

# Y se llama con los parámetros que queramos

suma(10,20)
suma(100,200)

### FUNCIÓN CON RETURN ###

def suma(num1,num2):
    resultado=num1+num2
    return resultado

print(suma(10,20)) 
print(suma(25,50))
suma(35,358) 

# El programa está arrojando también el 393 de la tercera llamada a la función por el return, 
# pero no aparece en consola porque no tiene print.