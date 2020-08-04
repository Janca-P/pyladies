plaintext = str(input("Zadejte prosím slovo, které má být zašifrováno:"))
key_cipher = int(input("Zadejte prosím šifrovací klíč:"))
ciphertext = " "

for pismeno in plaintext:#používám cyklus pro každé písmeno v plaintext, mezi velkými a malými písmeny v ASCII jsou další znaky, které 
                            #v sifre nechcu
        if pismeno.isupper():
            pismeno_unicode = ord (pismeno) #převede na cislo v ASCII, velká písmena jsou 65 - 90
            znak_poradi = ord (pismeno) - ord ("A") #určí pořadí znaku od začátku abecedy
                                                #nastavení ord(A) mi zajistí šifrování opět do velkých písmen (napravo od 65)
            poradi_sifra = (znak_poradi + key_cipher) % 26 #nova pozice znaku v sifrovanem textu, posunuto o zadaný klíč, modulo mi zajišťuje šifrování
                                                #čísel v rozsahu 0 - 25 (anglická abeceda),pro velká písmena tedy 65 - 90
                                                # po dosáhnutí Z, začíná znovu od A
        

            sifra_unicode = poradi_sifra + ord("A") #jake cislo v ASCII po posunutí dle klíče (15.písmeno + 65 = 70)
            sifra_pismeno = chr(sifra_unicode) #převod na písmeno
            ciphertext = ciphertext + sifra_pismeno
        elif pismeno.islower():
            pismeno_unicode = ord (pismeno) #převede na cislo v ASCII, malá písmena 97 - 122
            znak_poradi = ord (pismeno) - ord ("a") 
            poradi_sifra = (znak_poradi + key_cipher) % 26 
            sifra_unicode = poradi_sifra + ord("a") 
            sifra_pismeno = chr(sifra_unicode)
            ciphertext = ciphertext + sifra_pismeno

       
print ("Plaintext = ", plaintext)
print ("key =", key)
print ("Ciphertext =", ciphertext)