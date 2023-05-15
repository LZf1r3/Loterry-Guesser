## Coded by: Lucas Faiad

import random
class Lottery:
    def __init__(self):
        self.numbers = None
        pass


    def select_lottery(self):
        print("Please, select the type of lottery:")
        type_lottery = str(input("(1)Mega-sena (2)Loto-facil (3)..."))
        type_lottery.strip().lower()
        if  type_lottery == "mega-sena" or type_lottery == "1":
            self.numbers = 60
            Mega_Cena.exec
        else:
            print("ERROR")


    def exec(self):
        Lottery.select_lottery
        print("Oi")

class Mega_Cena(Lottery):
    def __init__(self):
        self.bet = int(input("Quantos numeros voce deseja marcar?\n"))

    @property
    def sorteando(self):
        guessed = random.sample(range(1,60),self.bet)
        print(guessed)
    
    @property
    def exec(self):
        Mega_Cena.sorteando

Lottery.select_lottery(self=self)