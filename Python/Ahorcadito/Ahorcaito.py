
def game(palabra):
    import win_lost # modulo donde se almacenan los mensajes de "win"-"lost"  
    intentos=len(palabra)
    sombra=[]

    def generator_sombra():
        #metodo para crear array con campos vacios para ver el proceso del juego
        for letra in palabra:
            sombra.append("_")
        print(sombra)
        
    generator_sombra()
    print(f"\033[92mintentos {intentos}\033[0m")
    arr_palabra=list(palabra)

    while intentos > 0:
    # for x in range(100):
        if sombra == arr_palabra:
            #si se completo la palabra 
            print(f"\033[92m{win_lost.win}\033[0m")
            break
        else:
            #si no se completo la palabra
            opcion=input("digite una letra: ")
            if opcion in arr_palabra:
                #si la letra existe en la palabra
                for i in range(len(arr_palabra)):
                    if  opcion == arr_palabra[i]:             
                        sombra[i]=opcion
                print("\033[92mLetra correcta\033[0m")
                print(f"\033[92mintentos {intentos}\033[0m")
            else:
                #si la letra no existe en la palabra
                intentos-=1
                print("\033[91mLetra incorrecta\033[0m")
                print(f"\033[91mintentos {intentos}\033[0m")
                if intentos==0:
                    #si los intentos son iguales a "0" PERDISTE
                    print(f"\033[91m{win_lost.lost}\033[0m")
                    #   break
            print(sombra)
game("otorrinolaringologo")
