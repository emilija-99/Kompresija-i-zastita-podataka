import math

class Simbol:
    def __init__(self, karakter, verovatnoca):
        # klasa simbol ima karakter koji se kodira
        # za svaki karakter računamo verovatnoću pojavljivanja karaktera i 
        # code koji će nam služiti za kodiranje
        self.karakter = karakter
        self.verovatnoca = verovatnoca
        self.code = ""

def shannonFanoKodiranje(podaci):
    # broj ponavljanja određenog karaktera
    broj_ponavljanja = {}
    for karakter in podaci:
        broj_ponavljanja[karakter] = broj_ponavljanja.get(karakter, 0) + 1
    
    ukupan_broj_karaktera = len(podaci)
    
    # lista simboli = predstavlja jedan karakter sa njegovom verovatnoćom
    simboli = [Simbol(karakter, count / ukupan_broj_karaktera) for karakter, count in broj_ponavljanja.items()]
    
    # sortiranje simbola u opadajućem rasporedu prema njihovoj verovatnoći
    simboli.sort(key=lambda x: x.verovatnoca, reverse=True)
    
    def ponoviRekurzivno(simboli):
        if len(simboli) == 1:
            return
        
        # računamo ukupnu verovatnoću svih simbola u trenutnom skupu
        ukupna_verovatnoca = sum(sym.verovatnoca for sym in simboli)
        
        _verovatnoca = 0
        
        # razlika između ove dve vrste verovatnoća meri koliko su skupovi blizu po svojoj verovatnoći
        # Deljenje skupa na dva skupa i poređenje njihove verovatnoće nam govori o tome koliko će naše kodiranje biti efikasno
        min_diff = float('inf')
        
        split_index = 0
        
        for i in range(len(simboli) - 1):
            _verovatnoca += simboli[i].verovatnoca
            diff = abs((ukupna_verovatnoca - _verovatnoca) - _verovatnoca)
            if diff < min_diff:
                min_diff = diff
                split_index = i
        
        # dodeljujemo "0" i "1" kodovima u levoj i desnoj polovini
        for i in range(split_index + 1):
            simboli[i].code += "0"
        for i in range(split_index + 1, len(simboli)):
            simboli[i].code += "1"
        
        # ponavljamo rekurzivno za levu i desnu stranu skupa
        ponoviRekurzivno(simboli[:split_index + 1])
        ponoviRekurzivno(simboli[split_index + 1:])
    
    ponoviRekurzivno(simboli)
    
    # kreiranje rečnika simbola za kodove
    dict_kodova = {sym.karakter: sym.code for sym in simboli}
    
    print("dict_kodova", dict_kodova)
    encoded_podaci = ''.join(dict_kodova[karakter] for karakter in podaci)
    
    return encoded_podaci, dict_kodova

def sacuvajEncodedPodatke(input_file_path, output_file_path):
    # Čitaj txt fajl
    with open(input_file_path, 'r', encoding='utf-8') as file:
        podaci = file.read()
    
    # Primeni shannon fano kodiranje
    encoded_podaci, dict_kodova = shannonFanoKodiranje(podaci)
    
    with open(output_file_path, 'wb') as file:
        for karakter, code in dict_kodova.items():
            file.write(f"{ord(karakter)}:{code}\n".encode())  # Sačuvaj karaktere kao kodove
        file.write(b"\n")
        
        padded_encoded_podaci = encoded_podaci + '0' * ((8 - len(encoded_podaci) % 8) % 8) 
        byte_array = bytearray()
        for i in range(0, len(padded_encoded_podaci), 8):
            byte = int(padded_encoded_podaci[i:i+8], 2)
            byte_array.append(byte)
        
        file.write(byte_array)

input_file_path = 'file.txt'
output_file_path = 'encoded_fajl_shannon_fano.bin'
sacuvajEncodedPodatke(input_file_path, output_file_path)
