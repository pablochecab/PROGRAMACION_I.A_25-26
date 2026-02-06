year = int(input("Inserta el año: "))

if year < 1582:
    print(f"El año {year} está fuera del calendario gregoriano.")
else:
    if year % 4 != 0:
        print(f"El año {year} es común.")
    elif year % 100 != 0:
        print(f"El año {year} es bisiesto.")
    elif year % 400 != 0:
        print(f"El año {year} es común.")
    else:
        print(f"El año {year} es bisiesto.")
