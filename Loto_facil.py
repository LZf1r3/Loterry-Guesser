## Coded by Lucas-Faiad

import random
def Loto():
    print("Bem vindo ao adivinhador de Loto facil LZ!")
    number_rows = int(
        input("Por gentileza digite a quantidade de numeros que deseja apostar:\n"))
    number_of_lottery = int(input("Por gentileza digite a quantidade de cartelas:\n"))

    while number_of_lottery > 0:
        rolls = random.sample(range(1, 25), number_rows)
        print(rolls)
        number_of_lottery -= 1

if __name__ == "__main__":
    Loto()