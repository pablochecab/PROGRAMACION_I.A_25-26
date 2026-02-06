palabra_sin_vocales = ""
# Indicar al usuario que ingrese una palabra
# y asignarla a la variable palabra_usuario.
palabra_usuario = str(input("Escribe una palabra:"))
palabra_usuario = palabra_usuario.upper()

for letter in palabra_usuario:
    if letter in "AEIOU":
            continue
    print(letter, end="")
