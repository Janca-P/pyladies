def tah(pole, cislo_policka, symbol):
    """Vrátí herní pole s daným symbolem na dané pozici"""
    if cislo_policka >= 0 and cislo_policka <= 19:
        pole_seznam = list(pole) #udělám si z řetězce seznam,aby se mi to líp upravovalo
        pole_seznam[cislo_policka] = symbol #tímhle obsazuji pole "-" na symbol
        pole = "".join(pole_seznam) #vrátí seznam s nově umístěným symbolem
        return pole
    else:
        print("Chyba!")