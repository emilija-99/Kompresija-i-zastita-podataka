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
        ind = self.indicator
        if isinstance(ind, (bytes, bytearray)):
            ind = ind.hex() if ind and not (32 <= ind[0] <= 126) else ind.decode('latin-1', 'replace')
        return f"offset={self.offset}, length={self.length}, indicator='{ind}'"

""" Funckija rekurzivno računa dužinu ponavljanja znakova u tekstu
    text - originalni tekst
    window - prozor u kojem se traže ponavljanja
    text_index - trenutni indeks u originalnom tekstu
    window_index - trenutni indeks u prozoru
    Vraća dužinu ponavljanja znakova u prozoru
"""
def duzinaOdIndeksa(text: bytes, window: bytes, text_index: int, window_index: int) -> int:
    if text_index >= len(text) or window_index >= len(window) \
       or text[text_index:text_index+1] != window[window_index:window_index+1]:
        return 0
    return 1 + duzinaOdIndeksa(text, window + text[text_index:text_index+1],
                               text_index + 1, window_index + 1)

def dekodirajPodatak(text: bytes, search_buff: bytes) -> Podaci:
    if not text:
        return Podaci(-1, -1, b"")  

    length, offset = 0, 0
    if not search_buff:
        return Podaci(0, 0, text[0:1])  

    for i in range(len(search_buff)):
        found_offset = len(search_buff) - i
        if search_buff[i:i+1] == text[0:1]:
            found_length = duzinaOdIndeksa(text, search_buff, 0, i)
            if found_length >= length:
                offset, length = found_offset, found_length

    indikator = text[length:length+1] if length < len(text) else b""
    return Podaci(offset, length, indikator)
"""Funkcija LZ77kompresija prima tekst i vraća listu tokena koja sadrži informacije o offsetu, dužini i indikatoru."""

def LZ77kompresija(text: bytes):
    output = []
    search_buff = b""

    while text:
        token = dekodirajPodatak(text, search_buff)
        search_buff += text[: token.length + (1 if token.indicator else 0)]
        if len(search_buff) > search_bufer:
            search_buff = search_buff[-search_bufer:]

        text = text[token.length + (1 if token.indicator else 0):]
        output.append(token)
    return output

def LZ77dekompresija(tokens):
    out = bytearray()
    for t in tokens:
        if t.offset > 0 and t.length > 0:
            start = len(out) - t.offset
            # kopiraj prethodni segment
            for k in range(t.length):
                out.append(out[start + k])
        if t.indicator:
            # t.indicator je bytes (dužine 1)
            out.extend(t.indicator)
    return bytes(out)

def upisiFajl(tokens, out_path):
    lines = []
    for t in tokens:
        indicator_byte = t.indicator[0] if t.indicator else 0
        # za preglednost prikaži štampljive karaktere, ostalo kao \xHH
        if 32 <= indicator_byte <= 126:
            ind_str = chr(indicator_byte)
        else:
            ind_str = f"\\x{indicator_byte:02x}"
        lines.append(f"[{t.offset}, {t.length}, {ind_str}]")
    with open(out_path, 'a', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')


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
    
in_file = f"_projekat_1\\output\\random-ascii1.bin"
out_file = f"_projekat_1\\output\\lz77-code\\lz77-kompresija-output.txt"

with open(in_file, 'rb') as file:
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