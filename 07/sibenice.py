import random

seznam = ["pes", "kočka", "pták"]
slovo = random.choice(seznam)
retezec = "-" * len(slovo)
pismeno = input("Zadejte písmeno:")
 
def nahrazeni_pismenem (slovo, retezec):
    pocet_neuspechu = 0  
    for pismeno in slovo (len(slovo)):
        if pismeno in (slovo):
            retezec_seznam = list(retezec)
            retezec[slovo.index(pismeno)] = pismeno
            retezec = " " .join(retezec_seznam)
            return (retezec)
        elif "-" not in retezec:
            print("Gratuluji!")
        else:
            pocet_neuspechu = pocet_neuspechu + 1
            print("Počet neúspěchů", pocet_neuspechu)

nahrazeni_pismenem(slovo, retezec)
print(nahrazeni_pismenem)




