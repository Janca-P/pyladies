

zvirata = ["had", "pes", "kočka", "králík"]
zvirata.append("andulka")
print(zvirata)
zvirata_od_druheho = {}#prazdny slovnik, ktery naplnim
for zvire in zvirata:
    klic = zvire[1] #druhe pismeno
    zvirata_od_druheho[klic] = zvire #vytvoreni dvojice klic:hodnota
print(zvirata_od_druheho)

seznam = list(zvirata_od_druheho.items()) #abecedni razeni (sort) mi funguje jenom v seznamu - převedu funkcí list
                                          #dlouho mi to printovalo jenom klice - musim zadat .items
seznam.sort()
print(seznam)

zvirata_hodnoty_seznam = []
for zvire in zvirata_od_druheho.values():
    zvirata_hodnoty_seznam.append(zvire)
print(zvirata_hodnoty_seznam)




