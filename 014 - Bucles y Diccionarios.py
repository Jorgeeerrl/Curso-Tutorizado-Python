######################################## BUCLES Y DICCIONARIOS ########################################

paisescapitales={"Espana":"Madrid", "Francia":"Paris", "Inglaterra":"Londres", "Italia":"Roma", "Portugal":"Lisboa"}

for clave in paisescapitales:
    print(clave)

# Imprime las claves recorriendo el diccionario.


for clave in paisescapitales:
    capital=paisescapitales[clave] # Aquí le decimos que la variable capital sea el valor de cada posición [] del diccionario
    print(clave)                   # conforme lo va recorriendo.
    print(capital)

# Imprime cada clave con su valor.


print(paisescapitales.items)  

# Esto nos imprime el diccionario completo, todos sus ítems. Otra forma más bonita sería:


for clave, capital in paisescapitales.items():
    print(clave+ "--->" +capital)