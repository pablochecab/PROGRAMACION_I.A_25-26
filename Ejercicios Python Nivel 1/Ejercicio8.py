palabra = str(input("Escribe una palabra:"))
palabra = palabra.upper()
              

for letra in palabra:
    if letra in "AEIOU":
            continue
    print(letra, end="")
