def fibonacci(cantidad):    
    numero1 = 1
    numero2 = 1
    for i in range(cantidad):
        print(numero1)
        numero3 = numero1 + numero2
        numero1 = numero2
        numero2 = numero3

fibonacci(10)

