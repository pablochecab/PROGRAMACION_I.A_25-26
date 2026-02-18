def clasificar_persona(edad, estado_civil):
    if edad < 18:
        return "Menor de edad"
    
    elif edad >= 18 and edad <= 65:
        if estado_civil == "soltero":
            return "Adulto soltero"
        
        elif estado_civil == "casado":
            return "Adulto casado"
    
        else:
            return "Estado civil desconocido"
    
    else:
        return "Persona mayor"

edades = [17, 25, 70]
estados = ["soltero", "casado" , ""]

for edad in edades:
    # Estando soltero
    print(f" {edad} , {estados[0]} , = {clasificar_persona(edad, estados[0])}")

    # Estando casado
    print(f" {edad} , {estados[1]} , = {clasificar_persona(edad, estados[1])}")

    # Estado civil desconocido:
    print(f" {edad} , {estados[2]} , = {clasificar_persona(edad, estados[2])}")

# Ejecución utilizando try y catch

def introducirDatos():
    i = False
    while i == False:
        try:
            edad = int(input("Escribe tu edad: "))
            estado = str(input("Escribe tu estado civil: "))
        except (ValueError, TypeError):
            print("ERROR. Debes introducir un numero entero.")
            continue
        # Si llega hasta aquí quiere decir que ha superado el except.
        i = True
    # Devolvemos (esto se convierte en una tupla.)
    return edad, estado;

print(introducirDatos())

