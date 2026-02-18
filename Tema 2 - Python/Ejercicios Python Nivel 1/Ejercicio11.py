# Programa para calcular la altura de la pirámide

bloques = int(input("Ingrese la cantidad de bloques: "))

altura = 0
bloques_necesarios = 1

while bloques >= bloques_necesarios:
    bloques -= bloques_necesarios
    altura += 1
    bloques_necesarios += 1

print("La altura de la pirámide es:", altura)
