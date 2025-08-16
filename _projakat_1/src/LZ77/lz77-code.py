"""LZ77 Kompresija i Dekompresija

LZ77 je algoritam za kompresiju podataka koji koristi pomeranje i dužinu za kodiranje ponavljajućih sekvenci.
Definisanje duzine kliznog prozora i lookahead koji odredjuje koliko znakova se kodira.
Search buffer je istorija prethodnih znakova koji se koristi za pronalaženje ponavljanja.

"""
_prozor = 20
lookahead_bufer = 15
search_bufer = _prozor - lookahead_bufer

class Podaci:
    def __init__(self, offset, length, indicator):
        self.offset = offset
        self.length = length
        self.indicator = indicator

    """ __repr__ metoda koja omogućava lakše ispisivanje objekta Podaci"""
    def __repr__(self):
        return f"offset={self.offset}, length={self.length}, indicator='{self.indicator}'"

""" Funckija rekurzivno računa dužinu ponavljanja znakova u tekstu
    text - originalni tekst
    window - prozor u kojem se traže ponavljanja
    text_index - trenutni indeks u originalnom tekstu
    window_index - trenutni indeks u prozoru
    Vraća dužinu ponavljanja znakova u prozoru
"""
def duzinaOdIndeksa(text, window, text_index, window_index):
    if text_index >= len(text) or text[text_index] != window[window_index]:
        return 0
    else:
        return 1 + duzinaOdIndeksa(text, window + text[text_index], text_index + 1, window_index + 1)

def dekodirajPodatak(text, search_buff):
    """Ulazni tekst je prazan, vraća se Podaci sa offsetom -1 i length -1"""
    if not text:
        return Podaci(-1, -1, "")
    
    length, offset = 0, 0

    """Ako je search_buff prazan, vraća se Podaci sa offsetom 0 i length 0"""
    if not search_buff:
        return Podaci(offset, length, text[0])

    """Prolazi kroz search_buff i traži prvi znak koji se poklapa sa prvim znakom u text
       Ako se pronađe poklapanje, računa se dužina ponavljanja znakova u search_buff
       Ako se ne pronađe poklapanje, vraća se Podaci sa offsetom 0 i length 0"""    
    for i, character in enumerate(search_buff):
        found_offset = len(search_buff) - i
        if character == text[0]:
            found_length = duzinaOdIndeksa(text, search_buff, 0, i)
            if found_length >= length:
                offset, length = found_offset, found_length
    return Podaci(offset, length, text[length] if length < len(text) else '')

"""Funkcija LZ77kompresija prima tekst i vraća listu tokena koja sadrži informacije o offsetu, dužini i indikatoru."""

def LZ77kompresija(text):
    output = []
    search_buff = ""
    
    while text:
        # Tokeni se generišu na osnovu trenutnog teksta i search_buff (istorije prethodnih znakova)
        token = dekodirajPodatak(text, search_buff)
        # Azuriramo search_buff sa novim tokenom + indikatorom (length + 1)
        # Smanjujemo tekst za dužinu tokena + 1 (za indikator)
        search_buff += text[: token.length + 1]
        if len(search_buff) > search_bufer:
            search_buff = search_buff[-search_bufer:]
        
        text = text[token.length + 1:]
        
        output.append(token)
    return output

def LZ77dekompresija(tokens):
    output = ""
    for token in tokens:
        if token.offset > 0:
            for _ in range(token.length):
                output += output[-token.offset]
        
        output += token.indicator
    return output

def upisiFajl(tokens, out_path):
    out = ""
    for t in tokens:
        offset = t.offset
        length = t.length
        indicator = t.indicator.encode('utf-8')[0] if t.indicator else 0
        out+= f"[{offset}, {length}, {chr(indicator)}]"+ '\n'
    with open(out_path, 'a') as file:
        file.write(out)

def ucitajTokeneIzBinarnogFajla(in_path):
    with open(in_path, 'rb') as file:
        text = file.read()

    tokeni = []
    for i in range(0, len(text), 3):
        if(i != "\n" and i != "\r\n"):
            offset = text[i]
            length = text[i + 1]
            indicator = chr(text[i + 2]) if text[i + 2] != 0 else ''
            print(f"Token: offset={offset}, length={length}, indicator='{indicator}'")
            i += 5  # pomeramo se za 3 bajta (offset, length, indicator)
        # offset = text[i]
        # length = text[i + 1]
        # indicator = chr(text[i + 2]) if text[i + 2] != 0 else ''
        # tokeni.append(Podaci(offset, length, indicator))
    # return tokeni
    
in_file = 'C:\\Users\Emilija\\Documents\\New folder\\_projakat_1\\output\\random-ascii.bin'
out_file = 'C:\\Users\\Emilija\\Documents\\New folder\\_projakat_1\\output\\lz77-code\\lz77-kompresija-output.txt'

with open(in_file, 'r') as file:
    podaci = file.read()

lz77Kodiranje = LZ77kompresija(podaci)
upisiFajl(lz77Kodiranje, out_file)

# tokeni = ucitajTokeneIzBinarnogFajla(out_file)
# print(f"Broj tokena: {len(tokeni)}")

print("Kodiranje LZ77: ")
for i in range(len(lz77Kodiranje)):
    print(lz77Kodiranje[i])

lz_77Dekodiranje = LZ77dekompresija(lz77Kodiranje)


if podaci == lz_77Dekodiranje:
    print("Dekodiranje je uspešno izvršeno.")
else:
    duzina = len(podaci)
    dekodiranje_duzina  = len(lz_77Dekodiranje)
    min = min(duzina, dekodiranje_duzina)

    razlika = None
    for i in range(min):
        if podaci[i] != lz_77Dekodiranje[i]:
            razlika = i
            break

    if razlika is not None:
        print(f"Razlika na poziciji {razlika}: "
              f"očekivano={repr(podaci[razlika])}, "
              f"dekodirano={repr(lz_77Dekodiranje[razlika])}")

    if duzina != dekodiranje_duzina:
        print(f"Različite dužine → original={duzina}, dekodirano={dekodiranje_duzina}")
