## Coded by Lucas-Faiad

import random
def Mega():
    print("Bem vindo ao adivinhador de Mega sena LZ!")
    numeros_tentados = int(
        input("Por gentileza digite a quantidade de numeros que deseja apostar:\n"))
    quantidade_de_loterias = int(input("Por gentileza digite a quantidade de cartelas:\n"))

    while quantidade_de_loterias > 0:
        rolls = random.sample(range(1, 60), numeros_tentados)
        print(rolls)
        quantidade_de_loterias -= 1

if __name__ == "__main__":
    Mega()