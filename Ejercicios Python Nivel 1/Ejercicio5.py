numero_secreto = 7  

intento = int(input("Adivina el número: "))

while intento != numero_secreto:
    print("¡Frío, frío!")
    intento = int(input("Intenta de nuevo: "))

print(f"¡Bien hecho! El número era {numero_secreto}.")
