# Programa que implementa la conjetura de Collatz

c0 = int(input("Ingresa un número natural: "))

if c0 <= 0:
    print("Debes ingresar un número natural mayor que 0.")
else:
    pasos = 0  # contador de pasos
    while c0 != 1:
        if c0 % 2 == 0:      # si es par
            c0 = c0 // 2
        else:                # si es impar
            c0 = 3 * c0 + 1
        print(c0, end=" - ")
        pasos += 1

    print("Pasos:", pasos)
