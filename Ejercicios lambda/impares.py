class Impares:
    def impares(totalNum, numero):
        if numero % 2 == 0:
            raise ValueError("El primer número debe ser impar.")
        firstNum = numero
        for i in range(totalNum):
            print(firstNum)
            firstNum += 2

    impares(5, 3)
