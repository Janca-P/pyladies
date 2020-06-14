zvirata = ["pes", "kočka", "králík", "had"]
zvirata_jina = ["koza", "pes", "pták", "had"]

zvirata_oba = []
for zvire in zvirata:
    if zvire in zvirata_jina:
        zvirata_oba.append(zvire)
print(zvirata_oba)
     
zvirata_1 = []
for zvire in zvirata:
    if zvire not in zvirata_jina:
        zvirata_1.append(zvire)
print(zvirata_1)

zvirata_2 = []
for zvire in zvirata_jina:
    if zvire not in zvirata:
        zvirata_2.append(zvire)
print(zvirata_2)
    
zvirata.sort()
print(zvirata)