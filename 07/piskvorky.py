from random import randrange
import ai
import util

pole_1 = ("-")*20
symbol = "x" or "o"
cislo_policka = randrange (0, 20)

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole: #nejsou 3 symboly za sebou, ale došlo hrací pole
        return "!"
    else:
        return "-"

def tah_hrace(pole):#hráčovi pro zjednodušení přiřazuji x
    """Zeptá se hráče, na jakou pozici chce hrát a vrátí nové hrací pole se zaznamenaným tahem"""
    while True:
        try:
            cislo_policka = int(input("Zadejte číslo políčka, na které chcete hrát(0 - 19):"))#pole se čísluje od 0, takže jen do 19
            if cislo_policka < 0 and cislo_policka > len(pole): #musí tahat v rámci pole a to musí být neobsazené: "-"
                print("Zadané políčko je mimo hrací pole!")
            elif pole[cislo_policka] != "-":
                print("Obsazené políčko!")
                cislo_policka = int(input("Zadejte číslo políčka, na které chcete hrát(0 - 19):"))
            else:
                return util.tah(pole, cislo_policka, "x")#přiřazené x     
        except ValueError:
            print("Nezadal/a jste číslo!")
        
def piskvorky_1d(pole):
    """Zobrazí pole a jeho stav vždy po každém tahu hráče nebo počítače"""
    while True: #používám while, protože hraju do té doby než nastane vyhodnocení
        print(pole)
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != "-": #pokud už nejde hrát, musím to nějak stopnout
            break
        pole = ai.tah_pocitace(pole)
        if vyhodnot(pole) != "-":#stop
            break
    if vyhodnot(pole) == "x":#vyhodnocení situace, když políčko není "-"
        print("Výhra!")
    if vyhodnot(pole) == "o":
        print("Prohra, vyhrál počítač!")
    if vyhodnot(pole) == "!":
        print("Remíza!")



