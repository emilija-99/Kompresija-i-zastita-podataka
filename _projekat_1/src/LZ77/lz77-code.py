"""LZ77 Kompresija i Dekompresija

LZ77 je algoritam za kompresiju podataka koji koristi pomeranje i dužinu za kodiranje ponavljajućih sekvenci.
Definisanje duzine kliznog prozora i lookahead koji odredjuje koliko znakova se kodira.
Search buffer je istorija prethodnih znakova koji se koristi za pronalaženje ponavljanja.

"""
from pathlib import Path

_prozor = 256
lookahead_bufer = 16
search_bufer = _prozor - lookahead_bufer

def lz77Kompresija(podaci):
    i = 0
    output = []
    n = len(podaci)
    while i < n:
        best_len = 0
        best_off = 0

        start = max(0, i - _prozor)
        max_ahead = min(lookahead_bufer, n - i)

        for j in range(start, i):
            l = 0
            # strogo kontroliši obe strane i dužinu
            while l < max_ahead and podaci[j + l] == podaci[i + l]:
                l += 1
            if l > best_len:
                best_len = l
                best_off = i - j

            if best_len == lookahead_bufer:
                break

        if best_len > 0:
            nxt_idx = i + best_len
            next_byte = podaci[nxt_idx] if nxt_idx < n else None
            output.append((best_off, best_len, next_byte))
            i += best_len + (1 if next_byte is not None else 0)
        else:
            output.append((0, 0, podaci[i]))
            i += 1
    return output

def lz_77Dekodiranje(tokens):
    out = bytearray()
    for pomak, duzina, sledeci in tokens:
        if pomak > 0 and duzina > 0:
            start = len(out) - pomak
            for k in range(duzina):
                out.append(out[start + k])
        if sledeci is not None:
            out.append(sledeci)
    return out

def upisiFajl(tokens, out_path):
    lines = []
    for off, ln, ind in tokens:
        ind_repr = f"{ind}" if ind is not None else "EOF"
        lines.append(f"[{off}, {ln}, {ind_repr}]")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines) + "\n")


def zapisiDekodiranePodatke(lz77Dekodiranje): 
    with open(output_file_dekodiranje, "wb") as file:
        file.write(lz77Dekodiranje)


input_file = f"_projekat_1\\output\\random-ascii.bin"
output_file_kodiranje = f"_projekat_1\\output\\lz77-code\\lz77-kodiranje.txt"
output_file_dekodiranje = f"_projekat_1\\output\\lz77-code\\lz77-dekodiranje.txt"

with open(input_file, 'rb') as file:
    podaci = file.read()

fajl = Path(output_file_kodiranje)
lz77Kodiranje = lz77Kompresija(podaci)

if(fajl.exists()):
    print("Fajl je napravljen!")
else:
    upisiFajl(lz77Kodiranje, output_file_kodiranje)

lz_77Dekodiranje = lz_77Dekodiranje(lz77Kodiranje)
zapisiDekodiranePodatke(lz_77Dekodiranje)

