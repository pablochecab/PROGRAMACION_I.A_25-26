millas = float(input("Ingresa la cantidad de millas: "))
kilometros = float(input("Ingresa la cantidad de kilómetros: "))

km_equivalente = round(millas * 1.61, 2)
millas_equivalente = round(kilometros / 1.61, 2)

print(f"{millas} millas equivalen a {km_equivalente} km")
print(f"{kilometros} km equivalen a {millas_equivalente} millas")
