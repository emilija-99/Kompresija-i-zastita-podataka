def LZW_Kodiranje(podaci):
    print(f"Ulazni podaci: {podaci}")
    recnik = {bytes([i]): i for i in range(256)}
    preth = bytes()
    rezultat_kompresije = []
    code = 256

    """ Dinamički ažuriramo rečnik i generisemo kodirane skevence """
    for karakter in podaci:
        sekvenca_karaktera = preth + bytes([karakter])
        print(f"Trenutni karakter: {chr(karakter)}, prethodna sekvenca: {preth}, nova sekvenca: {sekvenca_karaktera}")
        """
            Proveravamo da li nova sekvanca karaktera postoji u rečniku, 
            ako postoji potrebno je da ažuriramo prethodnika na trenutni karakter
            i nastavljamo sa sledećim karakterom.
        """
        if sekvenca_karaktera in recnik:
            preth = sekvenca_karaktera
        else:
            """
            Ako sekvenca karaktera ne postoji dodajemo je u rečnik i dodajemo kod prethodnika u rezultat kompresije.
            Ažuriramo prethodnika na trenutni karakter i povećavamo kod za sledeći unos.
            """
            rezultat_kompresije.append(recnik[preth])
            recnik[sekvenca_karaktera] = code
            code += 1
            preth = bytes([karakter])
            print(f"Nova sekvenca dodata u rečnik: {sekvenca_karaktera}, kod: {recnik[sekvenca_karaktera]}")
    if preth:
        rezultat_kompresije.append(recnik[preth])

    print(f"Broj kodova u rečniku: {len(recnik)}")
    for kod in recnik:
        print(f"Kod: {kod}, vrednost: {recnik[kod]}")

    return rezultat_kompresije

def LZW_Dekodranje(kompresovani_podaci):
    """Kreiramo rečnik sa početnim kodovima (0-255)"""
    recnik = {i: bytes([i]) for i in range(256)}
    
    """ Prevodimo kompresovane podatke u sekvence bajtova 
        i dekodiramo ih koristeći rečnik.
    """
    preth = bytes([kompresovani_podaci[0]])
    rezultat_dekompresije = [preth]
    code = 256

    for trenutni in kompresovani_podaci[1:]:
        if trenutni in recnik:
            sekvenca = recnik[trenutni]
        elif trenutni == code:
            sekvenca = preth + preth[0:1]
        else:
            raise ValueError(f'Izvršeno je loše kodiranje karaktera: {trenutni}')
        
        rezultat_dekompresije.append(sekvenca)
        recnik[code] = preth + sekvenca[0:1]
        code += 1
        preth = sekvenca
    
    return b''.join(rezultat_dekompresije)

input_file_path = 'C:\\Users\\Emilija\\Documents\\New folder\\_projakat_1\\output\\random-ascii.bin'
output_file_path = 'C:\\Users\\Emilija\\Documents\\New folder\\_projakat_1\\output\\lzw-code\\lzw-kompresija.bin'

with open(input_file_path, 'rb') as file:
    text = file.read()

print(f"Učitani podaci: {text}")
if not text:
    raise ValueError("Fajl je prazan ili ne postoji.")
else:
    lzwKodiranje = LZW_Kodiranje(text)

with open(output_file_path, 'wb') as f:
    for kod in lzwKodiranje:
        if kod < 0 or kod > 0xFFFF:
            raise ValueError(f"Kod {kod} ne staje u 16 bita.")
        f.write(kod.to_bytes(2, byteorder='big'))

kodiraniPodaci = []
with open(output_file_path, 'rb') as f:
    while True:
        chunk = f.read(2)
        if not chunk:
            break
        if len(chunk) != 2:
            raise ValueError("Neispravan fajl (neparan broj bajtova).")
        kodiraniPodaci.append(int.from_bytes(chunk, 'big'))

dekodirani = LZW_Dekodranje(kodiraniPodaci)