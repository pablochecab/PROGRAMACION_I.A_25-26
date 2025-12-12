def dataReader(username, age):
    diccionario = {
        username: int(age)
        }

    while username != "0":
        username = input("Escribe otro nombre (0 para terminar): ")
        if username == "0":
            break

        age = int(input("Escribe otra edad: "))
        diccionario[username] = age

    return diccionario

def getOldest(diccionario):

    oldest = max(diccionario.values())
    for nombre, edad in diccionario.items():
        if edad == oldest:
            return (nombre, edad)

def getYoungest(diccionario):

    youngest = min(diccionario.values())   # Primero sacamos la edad mínima
    for nombre, edad in diccionario.items(): # Luego buscamos quién tiene esa edad
        if edad == youngest:
            return (nombre, edad)

        

# Valores iniciales
username = input("Escribe un nombre (0 para terminar): ")
age = input("Escribe una edad: ")

# Llamamos a la función
diccionario = dataReader(username, age)

# Mostrar por pantalla:
print("Datos de los usuarios:", diccionario)

# Usuario con mayor edad
oldest = getOldest(diccionario)
print("Usuario con mayor edad: ", oldest)

# Usuario con menor edad
youngest = getYoungest(diccionario)
print("Usuario con menor edad: ", youngest)
