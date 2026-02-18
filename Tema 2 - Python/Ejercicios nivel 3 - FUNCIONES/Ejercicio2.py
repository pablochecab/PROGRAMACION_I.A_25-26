"""Neecesitamos esta función para determinar si el año es bisiesto o no
para saber la cantidad de días que va a tener febrero."""
def isBisiesto(year):
    if year > 1582:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    else:
        return "Debes escoger un año superior a 1582"
    
def daysOfMonth(year, month):
    months= ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    if year > 1582:
        # Comprobamos si el año es bisiesto.
        isBisiesto(year)
        print(isBisiesto(year))
        if year == True:
            # Si además el mes introducido es febrero:
            if month == 'Febrero':
                return "29 días"
        
        if month in ("Enero", "Marzo", "Mayo", "Julio", "Agosto", "Octubre", "Diciembre"):
            return "31 días"

        else:
            return "30 días"
    else:
        return "Debes escoger un año superior a 1582"
        
year_user = int(input("Escribe un año: "))
month_user = (input("Escribe un mes: "))
print(daysOfMonth(year_user, month_user))
    
