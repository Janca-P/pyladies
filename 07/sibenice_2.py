slovo = "python"
pole = "-" * len(slovo)
pocet_neuspechu = 0

while pole != slovo: #dokud se neuhádne celé slovo
    print(pole)
    pismeno = input("Zadejte pismeno:")
    pole_seznam = list(pole) #převod řetězce na seznam
    if pismeno in slovo:
        for symbol in range(len(slovo)): #projíždí písmena ve slově
            if slovo[symbol] == pismeno:
               pole_seznam[symbol] = pismeno #záměna - v řetězci za písmeno
               pole = "".join(pole_seznam) #převod zpět na řetězec
    else: 
        print ("Zkuste znovu!")
        pocet_neuspechu += 1
    
print(pole)
print ("Počet trestných bodů:", pocet_neuspechu)
with open ("obrazky_sibenice.txt", encoding="utf-8") as file_:
    content = file_.read()
sibenice = content.split("------------------")
print(sibenice[pocet_neuspechu])