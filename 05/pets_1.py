pets_slovnik = {"Amos" : "bulterier", "Ben" : "koršpaněl", "Amy" : "ohař"}
for pes in pets_slovnik:
    print(pes + " " + "je" + " " + pets_slovnik[pes]) #bez upresneni se mi automaticky vraci klic - jmeno psa,hodnotu(rasu) vyvolavam klicem
kopie = pets_slovnik.copy()
kopie["Amy"] = "baset"
for pes in kopie:
    print(pes + " " + "je" + " " + kopie[pes])
del kopie["Amy"]
for pes in kopie:
    print(pes + " " + "je" + " " + kopie[pes])
#funkci nepoužívám, jelikož v zadání je používát jen věci, které jsme probraly