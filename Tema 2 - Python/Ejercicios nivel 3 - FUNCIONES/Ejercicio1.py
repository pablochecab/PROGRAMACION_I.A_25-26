def isBisiesto(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

test_data = [1900, 2000, 2016, 1987, 2003, 1954, 2020, 2012, 1912, 1965] # Rellena esta lista con más años
test_results = [False, True, True, False, False, False, True, True, False, True] # Rellena esta lista con los resultados esperados para esos años

# codifica aquí la prueba de tu función
for year in test_data:
    print(isBisiesto(year))
