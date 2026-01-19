#!/usr/bin/env python 3
""" Este módulo realiza las siguientes funciones matemáticas:
    - Factorial
    - Hipotenusa
    Ejecutable solo directamente.
"""
# linea shabang, shebang, hashbang o poundbang
import math
dir(math)

''' Calcula el factorial de un número entero '''
import math

def factorial(n):
    try:
        # Si el número no es un entero
        if not isinstance(n, int):
            print("El parámetro debe ser un número entero")
            return

        # Si el número es menor que 0
        if n < 0:
            print("El número debe ser mayor o igual que cero")
            return

        return math.factorial(n)

    except TypeError:
        print("SALTA EXCEPCIÓn")


''' Calcula la hipotenusa de un triángulo rectángulo '''
def hipotenusa(a,b):

    if not isinstance(a, int):
        print("El parámetro A debe ser un número entero")
    
    if not isinstance(b, int):
        print("El parámetro B debe ser un número entero")

    if a < 0 or b < 0:
        print("Los lados no pueden ser negativos")
    
    return math.hypot(a,b)



# Añade las instrucciones necesarias para probar factorial() e hipotenusa()
if __name__ == "__main__":
    # Todo lo que está aqui dentro no se ejecuta si lo llamo desde fuera.
    print("Factorial: ", factorial("hola"))
    print("Hipotenusa: ", hipotenusa(10, 15))
    print("SE ME VE PORQUE ESTOY SIENDO EJECUTADO DESDE BASICS :)")

    # Pruebas

    

