cislo = input("Zadejte rodné číslo:")
lomitko = cislo[6]
den_narozeni = cislo[4:6] #vypíše pozici 4,5, ale už ne koncovou 6
mesic_narozeni = cislo[2:4]
rok_narozeni = cislo[0:2] 
pohlavi = cislo[2]
if len(cislo) == 11 and lomitko == "/":
    True
else: print("Rodné číslo musí obsahovat 11 znaků včetně lomítka!")
#rok
if int(cislo[0]) != 0: #rozlišit, jestli je narozen od 1900 nebo od 2000
    print("Rok narozeni: 19" + rok_narozeni) #1900
elif int(cislo[0]) == 0:
    print("Rok narozeni: 20" + rok_narozeni) #2000
else:
    print("Rodné číslo v nesprávném formátu!")
#mesic
if int(mesic_narozeni) > 12:
    mesic_narozeni = int(mesic_narozeni) - 50
    print("Měsíc narození: ",mesic_narozeni)
elif int(mesic_narozeni) > 0 and int(mesic_narozeni) <= 12:
    print("Měsíc narození: ", mesic_narozeni)
else:
    print("Rodné číslo v nesprávném formátu!")
#den
if int(den_narozeni) > 0 and int(den_narozeni) < 32:
    print("Den narozeni: " + den_narozeni)
else:
    ("Rodné číslo v nesprávném formátu!")
if int(pohlavi) < 5:
    print("Pohlaví: Muž")
else :
    print ("Pohlaví: Žena")

#overeni, Je-li rozdíl součtu číslic na sudém a lichém místě dělitelný jedenácti, pak je rodné číslo dělitelné jedenácti
cislo_bez_lomitka = (cislo[0:6] + cislo[7:12])#píšu 12, aby se mi vyprintoval 11.znak
licha = cislo_bez_lomitka[::2] #zadávám odstup prvků [start:stop:step]
suda = cislo_bez_lomitka[1::2]

soucet_licha = 0 #chci mít exponencialni soucet, zacinam na 0
for cislo in licha:#chci ty čísla vypsat postupně, takže loop
    soucet_licha = soucet_licha + int(cislo)
    print(soucet_licha)
soucet_suda = 0
for cislo in suda:
    soucet_suda = soucet_suda + int(cislo)
rozdil = soucet_suda - soucet_licha
if rozdil % 11 == 0:
    print("Rodné číslo je dělitelné 11!")
else: 
    print("Špatně zadané rodné číslo!")

if cislo_bez_lomitka.isdigit():
    True
else:
    print("Špatně zadané rodné číslo!")
    
