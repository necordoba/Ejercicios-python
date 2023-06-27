#Inertir una cadena de textoo.

# Crear una variable para alamcenar la palabra ingresada.
cadena = str(input("Ingrese una palabra"))

# permite extraer una parte de la cadena original. En este caso, al usar [::-1], indicamos que deseamos tomar toda la cadena, pero con un paso de -1, lo que significa que recorreremos la cadena de derecha a izquierda. Esto logra el efecto de invertir la cadena.
cadena_invertidad = cadena[::-1]

# se muestra la cadena invertida
print("La cadena invetida es:", cadena_invertidad)


