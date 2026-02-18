import random



def findHighestCalification(alumnos):

    # Por cada alumno que esté en el diccionario
    for alumno in alumnos:
        print("ALUMNO: ", alumno, alumnos[alumno])
        asignaturas = alumnos[alumno]
        # Lista en donde compararemos los valores.
        notas = []
        # Hasta que este bucle no acabe, no vuelve al primero.
        for asignatura in asignaturas:
            #Recogemos el valor de la tupla en la segunda posición y la guardamos en la lista que vamos a comparar.
            notas.append(asignatura[1])
            
        notaMax = max(notas)
        print(f" La nota más alta de {alumno} es de {notaMax}")
        

        
# Estructura: Diccionario -> Key con List de valor -> Tupla como valores de la list -> Valores en la tupla

alumnos = {
    "Juan": [("Matemáticas", random.uniform(0, 10)), 
             ("Historia", random.uniform(0, 10)), 
             ("Física", random.uniform(0, 10))],
    
    "Ana": [("Matemáticas", random.uniform(0, 10)), 
            ("Historia", random.uniform(0, 10)), 
            ("Física", random.uniform(0, 10))],
    
    "Luis": [("Matemáticas", random.uniform(0, 10)), 
             ("Historia", random.uniform(0, 10)), 
             ("Física", random.uniform(0, 10))]
}

findHighestCalification(alumnos)
