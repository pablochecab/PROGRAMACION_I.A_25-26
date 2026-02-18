ingresos = float(input("Escribe tus ingresos: "))

if ingresos < 85528:
    impuesto = ingresos * 0.18 - 556.20
    if impuesto > 0:
        print(f"Tu impuesto a pagar es de: {impuesto}")
        
elif ingresos > 85528:
    impuesto = 14839.20 + 85528 * 0.32
    if impuesto > 0:
        print(f"Tu impuesto a pagar es de: {impuesto}")
