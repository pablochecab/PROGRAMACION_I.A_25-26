# Asistencia a clase del estudiante.
def getStudentAssistance(student):

    total = len(student)
    assistance = 0
    
    for tupla in student:
        if tupla.count(True):
            assistance += 1
            
    return assistance / total * 100

def getStudentAttitude(student):

    total = len(student)

    for tupla in student:
        bueno = tupla.count("Bueno")
        regular = tupla.count("Regular")
        malo = tupla.count("Malo")

def getStudentStats(studentData):
    
    
studentData = {
    'Pablo': [
        ("Inglés", True, "Bueno"),
        ("Historia", False, "Regular"),
        ("Lengua", True, "Bueno"),
        ("Matemáticas", True, "Bueno")
    ],
    
    'Marcos': [
        ("Historia", False, "Regular"),
        ("Matemáticas", True, "Bueno"),
        ("Inglés", True, "Bueno"),
        ("Lengua", True, "Malo")
    ],
    
    'Leonardo': [
        ("Lengua", True, "Bueno"),
        ("Inglés", True, "Bueno"),
        ("Matemáticas", True, "Bueno"),
        ("Historia", False, "Regular")
    ]
}

# El valor 'Pablo' realmente va a ser el i del for.
print(getStudentAssistance(studentData['Pablo']))
