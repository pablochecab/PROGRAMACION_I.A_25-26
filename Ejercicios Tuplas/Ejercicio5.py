def weekStats(weekTemps):
    # Por cada clave del diccionario
    listTemps = []
    for day in weekTemps:

        # Recojo la tupla de temperaturas
        temps = weekTemps[day]
        minTemp = min(temps)
        maxTemp = max(temps)

        # Añadimos todos los valores a la lista vacía.
        listTemps.append(minTemp)
        listTemps.append(maxTemp)

        # Avisamos si la diferencia es > 15.
        if maxTemp - minTemp > 15:
            print(f" El {day} hubo una amplitud térmica superior a 15 grados.")

    print(f" La temperatura más baja de la semana ha sido de: {min(listTemps)}")
    print(f" La temperatura más alta de la semana ha sido de: {max(listTemps)}")

    # Calculo de la media
    sumTemps = 0
    for temp in listTemps:
        sumTemps += temp
    avg = sumTemps / len(listTemps)
    print(f" La media de temperatura en la semana ha sido de: {avg}")

# Valores
weekTemps = {
    'Lunes': (3, 20),
    'Martes': (7, 29),
    'Miercoles': (6, 17),
    'Jueves': (1, 18),
    'Viernes': (11, 18),
    'Sabado': (9, 21),
    'Domingo': (10, 32)
    }

weekStats(weekTemps)
