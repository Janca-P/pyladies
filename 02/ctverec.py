strana = float ( input ("Zadej cislo"))
cislo_je_spravne = strana > 0
if cislo_je_spravne:
    print ("obvod čtverce se stranou", strana, "je", strana * 4)
    print ("obsah čtverce se stranou", strana, "je", strana * strana)
else:
    print ("Strana musí být kladná, jinak z toho nebude čtverec!")
print ("Děkujeme za použití geometrické kalkulačky")