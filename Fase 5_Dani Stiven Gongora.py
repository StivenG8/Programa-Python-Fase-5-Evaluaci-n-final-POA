#Dani Stiven Gongora Guerrero
#CC1002408880
#FUNDAMENTOS DE PROGRAMACIÓN - (213022B_2201)
#Fase 5 - Evaluación Final POA
#Problema 5 - Registro de Horas Semanales 

#Función 
def procesar_jornadas(matriz_horas):  
#Calcula el total de horas semanales por persona y clasifica la jornada.

    #Lista vacía para almacenar los resultados de cada recurso (nombre, total horas, clasificación)
    resultados = []
    #Horas semanales 
    umbral_horas = 42
    
    for fila in matriz_horas:
        # "nombre" es el nombre respectivamente de cada recurso
        nombre = fila[0]
        #Suma de las horas de la semana
        # Las horas son todos los elementos de la fila excepto el primero (el nombre)
        horas_trabajadas = fila[1:]

        total_horas = sum(horas_trabajadas)
        
        # Clasificar la jornada
        if total_horas > umbral_horas:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"

        # Adjuntara los resultados a la lista de resultados como una tupla (nombre, total horas, clasificación)    
        resultados.append((nombre, total_horas, clasificacion))
        
    return resultados
#Función 
def main():
    # Datos de los recursos y horas trabajadas por día organizada de Lunes a Viernes
    #Datos
    matriz_horas = [
        ["Stiven", 8, 8, 8, 8, 9],    
        ["Luis", 9, 9, 8, 9, 8],   
        ["Howard", 8, 7, 8, 8, 7],  
        ["Carolina", 10, 8, 10, 8, 9],
        ["Daniela", 7, 8, 9, 8, 7]  
    ]
    #Entregra los datos a la funcion procesar_jornadas para obtener los resultados de cada recurso
    resultados = procesar_jornadas(matriz_horas)
    
    print(" Registro de Horas Semanales y Clasificación de Jornada")
    for nombre, total_horas, clasificacion in resultados:
        print(f"Recurso: {nombre} | Total Horas: {total_horas} | Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()
