import os
import math

def izracunajEntropiju(putanja_do_fajla):
    duzina = 0
    buff = {}

    with open(putanja_do_fajla, 'rb') as file:
        while True:
            content = file.read(1)
            if not content:
                break
            byte = ord(content)
            buff[byte] = buff.get(byte, 0) + 1
            duzina += 1

    H = 0
    for broj_ponavljanja in buff.values():
        if broj_ponavljanja:
            Hi = broj_ponavljanja / duzina
            H -= Hi * math.log2(Hi)

    return H

putanja_do_fajla = os.path.join('', 'file.txt')
entropy = izracunajEntropiju(putanja_do_fajla)
print("Entropija naseg fajl-a iznosi:", entropy)
