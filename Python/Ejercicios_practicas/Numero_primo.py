#se crea variable para almacenar numero ingresado.
num = int(input("Ingresa un numero"))
#Inicializamos esta avriable como verdadera.
primo = True

#creamos un ciclo for para saber si el numero es divisible por es divisible por i sin dejar residuo, es decir, si num es divisible por i. Si es divisible, significa que num no es un número primo y se establece la variable es_primo como False. Luego se utiliza break para salir del bucle, ya que no es necesario seguir comprobando más números.
for  i in range(2, num):
    if num % i == 0:
        primo = False
        break
    # mostramos en consola si es primo.
if primo:
        print(num, "Es un numero primo")
        # mostranos si no es primo.
else:
        print(num, "No es un numero primo")