import math

class Simbol:
    def __init__(self, karakter, verovatnoca):
        """Simbol ima karakter koji se kodira
        za svaki karakter računamo verovatnoću pojavljivanja karaktera i 
        code koji će nam služiti za kodiranje
        """
        self.karakter = karakter
        self.verovatnoca = verovatnoca
        self.code = ""

def shannonFanoKodiranje(podaci):
    # duzina podataka je 1
    if len(podaci) == 1:
        s, _ = podaci[0]
        return {s:'0'}
    
    # svakom karakteru dodeli broj pojavljivanja
    broj_ponavljanja = {}

    for karakter in podaci:
        broj_ponavljanja[karakter] = broj_ponavljanja.get(karakter, 0) + 1
    
    # print("Broj pojavljivanja karaktera u podatku:")
    # print("\n".join(f"{k}:{v}" for k,v in sorted(broj_ponavljanja.items(), key=lambda kv:kv[1],reverse=True)))
    
    ukupan_broj_karaktera = len(podaci)
    print(f"Broj karaktera u podatku: {ukupan_broj_karaktera}")  
    
    # lista simboli = predstavlja jedan karakter sa njegovom verovatnoćom
    simboli = [Simbol(karakter, count / ukupan_broj_karaktera) for karakter, count in broj_ponavljanja.items()]
    
    print("Verovatnoca pojavljivanja karaktera:")
    print("\n".join(f"{s.karakter}:{s.verovatnoca:.6f}" for s in simboli))

    # sortiranje simbola u opadajućem rasporedu prema njihovoj verovatnoći
    simboli.sort(key=lambda x: x.verovatnoca, reverse=True)
    
    def ponoviRekurzivno(simboli):
        if len(simboli) == 1:
            return
        
        # računamo ukupnu verovatnoću svih simbola u trenutnom skupu
        ukupna_verovatnoca = sum(sym.verovatnoca for sym in simboli)
        
        _verovatnoca = 0
        
        # Razlika između ove dve vrste verovatnoća meri koliko su skupovi blizu po svojoj verovatnoći
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
    sorted_dict = sorted(dict_kodova.items())

    map_verovatnoca = {s.karakter: s.verovatnoca for s in simboli}
    
    for kod in sorted_dict:
        print(f"Karakter: {kod[0]} | Verovatnoca: {map_verovatnoca[kod[0]]} | Code: {kod[1]}")

    encoded_podaci = ''.join(dict_kodova[karakter] for karakter in podaci)
    return encoded_podaci, dict_kodova

def sacuvajEncodedPodatke(input_file_path, output_file_path):
    # Čitaj txt fajl
    with open(input_file_path, 'r', encoding='utf-8') as file:
        podaci = file.read()
    
    # Primeni shannon fano kodiranje
    encoded_podaci, dict_kodova = shannonFanoKodiranje(podaci)
    print(f"Encoded: \n{encoded_podaci}")

    Ls = 0
    frekvencija = {karakter: podaci.count(karakter) for karakter in set(podaci)}
    for karakter, frek in frekvencija.items():
        for slovo, kod in dict_kodova.items():
            if karakter == slovo:
                print(f"Karakter: {karakter}, Frekvencija: {frek}, Kod: {kod}")
                Ls += frek * len(kod)

    print(f"Prosečna dužina Shannon-Fano kodova (Ls): {Ls / len(podaci)}")


    dekoded_podaci = decodirajShannonFano(dict_kodova, encoded_podaci)
    
    upisiDekodiranePodatke(dekoded_file_path, dekoded_podaci)
    
    uporediFajlove(dekoded_podaci, podaci)
    
    with open(output_file_path, 'wb') as file:
        for karakter, code in dict_kodova.items():
            file.write(f"{(karakter)}:{code}\n".encode())  # Sačuvaj karaktere kao kodove
        file.write(b"\n")
        
        padded_encoded_podaci = encoded_podaci + '0' * ((8 - len(encoded_podaci) % 8) % 8) 
        byte_array = bytearray()
        
        for i in range(0, len(padded_encoded_podaci), 8):
            byte = int(padded_encoded_podaci[i:i+8], 2)
            byte_array.append(byte)
        
        file.write(byte_array)


def decodirajShannonFano(dict_kodova, encoded_podaci):
    rev = {code:ch for ch,code in dict_kodova.items()}
    out,buf = [],""
    for b in encoded_podaci:
        buf+=b 
        if(buf in rev):
            out.append(rev[buf])
            buf = ""
    decoded = "".join(out)

    return decoded

def upisiDekodiranePodatke(output_file_path, dekoded_podaci):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(dekoded_podaci)
            

def uporediFajlove(decode, input_file):
    print(f"Broj karaktera pre kodiranje iznosi: {len(input_file)}\nBroj karaktera nakon dekodiranja iznosi: {len(decode)}")
    if len(input_file) != len(decode):
        print("Kodiranje nije uspesno.")
        razlika = []
        for i in range (0,len(input_file)):
            if(input_file[i] != decode[i]):
                razlika.append({"pozicija": i, "original": input_file[i], "dekode":decode[i]})
        
        if(len(razlika)>0):
            print(f"Razlika izmedju originalnog teksta i dekodiranog teksta: \n")
            for i in range(0, len(razlika)):
                print(f"Pozicija: {razlika[i].pozicija}, Originalna vrednost: {razlika[i].original}, Dekodirana vrednost: {razlika[i].decode} \n")
    else:
        print("Uspeno je izvrseno kodiranje i dekodiranje fajla bez gubitaka.")

input_file_path = 'C:\\Users\Emilija\\Documents\\New folder\\_projakat_1\\output\\random-ascii.bin'
output_file_path = 'C:\\Users\Emilija\\Documents\\New folder\\_projakat_1\\output\\shannon-fanno\\encoded_shannon_fano.bin'
dekoded_file_path = 'C:\\Users\Emilija\\Documents\\New folder\\_projakat_1\\output\\shannon-fanno\\decoded_shannon_fano.txt'
sacuvajEncodedPodatke(input_file_path, output_file_path)
