#se importa la libreria random para elegir numero a la azar.
import random

# se crea funcion para contener todo el codigo y se imprime la vienvenida al juego.
def jugar_adivinanza():
    print("Bienvendio al juego")
    print("¡Estas listo, comenzemos!")

    # Se crea variable con input para  pregutarle al usuario que nivel de juego desea.
    nivel = int(input("¿En que nivel de dificultad quieres jugar hoy?, elige(1,2 o 3): "))

    # variable inicializada en 0 para medir los intentos.
    intentos = 0

    # aqui se usa condicional if para indicar  cantidad de intentos segun el nivel de juego.
    if nivel == 1:
        intentos = 10
        numero_secreto = random.randint(1, 100)
    elif nivel == 2:
        intentos = 7
        numero_secreto = random.randint(1, 200)
    elif nivel == 3:
        intentos == 5
        numero_secreto = random.randint(1, 300)
    else:
        print("Esta opcion es invalida, intenta de nuevo.")
        return
    
    # se crea un input para que el usuario ingrese su numero y saber si el numero es igual al numero secreto o si debe serguir intentato, los intentos van disminuyendo de 1 en 1 hasta agotarse, lo que indica que el usuario perdio.
    while intentos > 0: 
        intento = int(input( "Por favor,Ingresa tu numero"))
        intentos -=1

        if intento == numero_secreto:
            print("¡Felicidades, Adivinaste!")
            return

        elif intento < numero_secreto:
            print("El numero es mas grande, Intenta de nuevo.")

        else:
            print("El numero es mas pequeño, intenta de nuevo.")

        print("Intentos restantes:" , intentos)

    print("Lo siento, agotaste tus intentos. El numero era:" , numero_secreto)    

jugar_adivinanza()
    