slovo = "python"



def hadani (slovo):
    """Vyzývá hráče k hádání písmen, dokud neuhodne celé slovo, v případě úspěchu nahradí příslušné místo v poli písmenem"""
    pocet_neuspechu = 0
    pole = "-" * len(slovo)
    while pole != slovo: #dokud se neuhádne celé slovo
        print(pole)
        pismeno = input("Zadejte pismeno:")
        pole_seznam = list(pole) #převod řetězce na seznam
        if pismeno in slovo:
            for symbol in range(len(slovo)): #projíždí písmena ve slově
                if slovo[symbol] == pismeno:
                    pole_seznam[symbol] = pismeno #záměna - za písmeno
                    pole = "".join(pole_seznam) #převod zpět na řetězec
        
        else: 
            pocet_neuspechu += 1
            print("Počet neúspěchů:", pocet_neuspechu)
            print ("Zkuste znovu!")

def obrazek_sibenice():
    with open ("obrazky_sibenice.txt", encoding="utf-8") as file_:
        content = file_.read()
        sibenice = content.split("------------------")
    return (sibenice[pocet_neuspechu])

hadani("python")
