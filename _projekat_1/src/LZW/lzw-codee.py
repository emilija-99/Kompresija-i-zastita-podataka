import json

def lzwKodiranje(podaci):
    tabela_kodova = {chr(i): i for i in range(256)}
    print("Tabela kodova:", tabela_kodova)

    podatak = ""
    rezultat = []

    for znak in podaci:
        podatakSimbol = podatak + znak
        print("Trenutni podatak:", podatak, "Simbol:", znak, "Podatak+Simbol:", podatakSimbol)
        if podatakSimbol in tabela_kodova:
                podatak = podatakSimbol
        else:
            rezultat.append(tabela_kodova[podatak])
            tabela_kodova[podatakSimbol] = len(tabela_kodova)
            podatak = znak
    
    if podatak:
        rezultat.append(tabela_kodova[podatak])
    return rezultat

def lzwDekodiranje(kodovi):
    tabela_kodova = {i: chr(i) for i in range(256)}

    sledeci = 256
    trenutni_kod = chr(kodovi[0])
    rezultat = [trenutni_kod]

    for kod in kodovi[1:]:
        if kod in tabela_kodova:
            upis = tabela_kodova[kod]
        elif kod == sledeci:
            upis = trenutni_kod + trenutni_kod[0]
        else:
            raise ValueError("Kod nije u tabeli kodova: {}".format(kod))
        rezultat.append(upis)

        if sledeci <= 0xFFFF:
            tabela_kodova[len(tabela_kodova)] = trenutni_kod + upis[0]
            sledeci += 1
        
        trenutni_kod = upis
    return ''.join(rezultat).encode('latin-1')


input_file_path = f"_projekat_1\\output\\random-ascii.bin"
enkodirani_file = f"_projekat_1\\output\\lzw-code\\lzw_enkodirani.bin"
dekodirani_file = f"_projekat_1\\output\\lzw-code\\lzw_dekodirani.bin"

with open(input_file_path, 'r', encoding='latin-1', newline='') as file:
    podaci = file.read()

print("Ucitani podaci:", podaci)
lzw_kodirani_podaci = lzwKodiranje(podaci)

with open(enkodirani_file, 'w', encoding='utf-8') as f:
    json.dump(lzw_kodirani_podaci, f)

lzwDekodiranje = lzwDekodiranje(lzw_kodirani_podaci)
with open(dekodirani_file, 'wb') as f:
    f.write(lzwDekodiranje)