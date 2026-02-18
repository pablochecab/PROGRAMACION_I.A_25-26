from random import randint

# La máquina piensa un número entre 0 y 100
numero_secreto = randint(0, 100)

print("He pensado un número entre 0 y 100.")

intentos = 0
adivinado = False

# Bucle hasta que el usuario acierte
while not adivinado:
    try:
        numero_usuario = int(input("Introduce tu número: "))
        intentos += 1

        if numero_usuario < numero_secreto:
            print("Más alto.")
        elif numero_usuario > numero_secreto:
            print("Es menor.")
        else:
            print(f"Lo has conseguido en {intentos} intentos.")
            print(f"El número era: {numero_secreto}")
            adivinado = True
