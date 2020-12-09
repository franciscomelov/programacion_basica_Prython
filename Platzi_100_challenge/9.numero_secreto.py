from random import randint
def adivina(n):
    contador = 0
    while True:
        contador += 1
        player = int(input("Adivina el numero: "))
        print("")

        if player == n:
            print(f'Adivinaste en {contador} intentos')
        elif n > player:
            print("el numero secreto es mayor")
        else:
            print("Elnumero secreto es menor")


n = randint(1, 100)
adivina(n)