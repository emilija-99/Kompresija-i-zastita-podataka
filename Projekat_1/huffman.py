class Simbol:
    def __init__(self, karakter, frekvencija):
        # karakter koji se kodira
        # broj ponavljanja datog karaktera u taksu
        # kod koji ce biti dodeljen karakteru tokom Huffmanovog kodiranja
        # pointeri levo,desno za stablno koje gradimo
        
        self.karakter = karakter
        self.frekvencija = frekvencija
        self.code = ""
        self.levo = None
        self.desno = None
        
def huffmanKodiranje(podaci):
    # racunamo broj pojavljivanja svakog simbola u ulaznim podacima
    frekvencija = {}
    for karakter in podaci:
        if karakter in frekvencija:
            frekvencija[karakter] += 1
        else:
            frekvencija[karakter] = 1
    
    # kreiramo listu objekata za svaki karakter
    simboli = [Simbol(karakter, frekvencija) for karakter, frekvencija in frekvencija.items()]
    
    # sortiranje simbola na osnovu broja pojavljivanja tako da simbol
    # sa najmanjim brojem ponavljanja bude prvi
    simboli.sort(key=lambda x: x.frekvencija)
    
    # sve dok imamo vise od jednog simbola potrebno je da uklanjamo
    # one simbole koji imaju najmanji broj ponavljanja
    # na taj nacin kreiramo stablo i zbir ponavljanja postavje novi cvor
    # dodajemo novi cvor u listu i ponavljamo sortiranje
    while len(simboli) > 1:
        levo = simboli.pop(0)  
        desno = simboli.pop(0)  
        
        novi_cvor = Simbol(None, levo.frekvencija + desno.frekvencija)
        novi_cvor.levo = levo
        novi_cvor.desno = desno
        
        simboli.append(novi_cvor)
        simboli.sort(key=lambda x: x.frekvencija)
    
    # dodeljujemo kodove svakom simbolu
    # simboli koji se nalaze levo u stablu se kodiraju sa "0",
    # dok se simboli koji se nalaze desno u stablu kodiraju sa "1"
    
    def dodeliKodove(cvor, kod=""):
        if cvor is None:
            return
        if cvor.karakter is not None:
            cvor.code = kod
            dict_kodova[cvor.karakter] = kod
        dodeliKodove(cvor.levo, kod + "0")
        dodeliKodove(cvor.desno, kod + "1")
    
    dict_kodova = {}
    
    dodeliKodove(simboli[0])
    
    encoded_podaci = ''.join(dict_kodova[karakter] for karakter in podaci)
    
    return encoded_podaci, dict_kodova

def sacuvajEncodedPodatke(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        podaci = file.read()
    
    encoded_podaci, dict_kodova = huffmanKodiranje(podaci)
    
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
output_file_path = 'encoded_fajl_huff.bin'
sacuvajEncodedPodatke(input_file_path, output_file_path)
