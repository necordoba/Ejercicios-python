import json

def  Notas():
    #se pide al usuario que ingrese numero de notas
    cantidad_notas = int(input("Digite cantidad de notas: "))
    # input para que el usuario ingrese numero de estudiantes
    cantidad_estudiantes = int(input("Ingrese numero de estudiantes: \n"))
    #se crea array  vacio para guardar las notas de TODOS los estudiantes
    notas_estudiantes = []
    # Se crea array vacio para guardar todos los estudiantes
    estudiantes =[]

    
    def estado(promedio):
        #funcion para clasificar el estado del estudiante 
        if promedio>=4.3: return "Sobresaliente"
        elif (promedio>=3.0) and (promedio<4.5): return "Aprobado"
        elif promedio<3.0: return "Reprobado"

    
    for estudiante in range(cantidad_estudiantes):
        # ciclo para ingresar nombre de cada estudiante 
        nombre_estudiante = input("Ingrese nombre del estudiante: \n")
        notas = []
        for nota in range(cantidad_notas):

            #ciclo para ingresar las notas de cada estudiante
            nota = float(input("Ingrese la nota  del estudiante: \n")) 
            notas_estudiantes.append(nota)
            notas.append(nota) 

        # se crea molde de un solo estudiante
        promedio = sum(notas)/len(notas)
        estudiante = {"nombre":nombre_estudiante,"notas":notas,"promedio":promedio,"estado":estado(promedio)}
        estudiantes.append(estudiante)

    
    formatted_data = json.dumps(estudiantes, indent=4)
    print(formatted_data)

    #promedio de notas grupales
    promedio_grupo = sum(notas_estudiantes)/len(notas_estudiantes)
    print("Las notas de todo el grupo son: " +str(notas_estudiantes))
    print("El promedio del grupo es: " +str(promedio_grupo))
  
Notas()

    

    

