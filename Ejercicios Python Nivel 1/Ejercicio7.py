palabra_secreta = "chupacabra"
palabra = input("Escribe una palabra: ")

"""while palabra != palabra_secreta:
    palabra = input("Escribe otra palabra: ")

print("Has dejado el bucle con éxito.")"""

while True: # Esta es una manera de hacer un bucle infinito
    palabra = input("Escribe una palabra: ")
    
    if palabra == palabra_secreta:
        print("Has dejado el bucle con éxito.")
        break  #Usamos el break para cortar el bucle infinito




