from random import randrange
import util
def tah_pocitace(pole):#nedefinuji symbol, zbylo na počítač o
    """Vrátí herní pole se zaznamenaným tahem počítače"""
    pozice = randrange(0, 20) #na začátku mám import random, vybírám z 19 políček - píšu 20 (n - 1)
    while True:
        pozice = randrange(len(pole))
        if pole[pozice] == "-":
            return util.tah (pole, pozice, "o")#přiřazené o
        else:
            print("Pozice obsazena!")