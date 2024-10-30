def lz77_compress(podaci, velicina_prozora=255, lookahead_buff=15):
    kompresovani_podaci = []
    i = 0
    n = len(podaci)

    while i < n:
        duzina_ponavljanja = 0
        distanca = 0
        start = max(0, i - velicina_prozora)
        for j in range(start, i):
            duzina = 0
            while (i + duzina < n) and (podaci[j + duzina] == podaci[i + duzina]) and (duzina < lookahead_buff):
                duzina += 1
            if duzina > duzina_ponavljanja:
                duzina_ponavljanja = duzina
                distanca = i - j
        
        if duzina_ponavljanja > 0:
            if i + duzina_ponavljanja < n:
                kompresovani_podaci.append((distanca, duzina_ponavljanja, podaci[i + duzina_ponavljanja]))
            else:
                kompresovani_podaci.append((distanca, duzina_ponavljanja, 0))  # Koristi 0 ako nema više karaktera
            i += duzina_ponavljanja + 1
        else:
            kompresovani_podaci.append((0, 0, podaci[i]))
            i += 1

    return kompresovani_podaci

def lz77_decompress(kompresovani_podaci):
    dekompresovani_podaci = []
    for distanca, duzina, next_karakter in kompresovani_podaci:
        start = len(dekompresovani_podaci) - distanca
        for i in range(duzina):
            dekompresovani_podaci.append(dekompresovani_podaci[start + i])
        dekompresovani_podaci.append(next_karakter)
    return bytes(dekompresovani_podaci)

input_file_path = 'file.txt'
output_file_path_kompresovani_podaci = 'comp_lz77.bin'
output_file_path_dekompresovani_podaci = 'decomp_lz77.bin'

with open(input_file_path, 'rb') as file:
    podaci = file.read()

kompresovani_podaci = lz77_compress(podaci)

with open(output_file_path_kompresovani_podaci, 'wb') as file:
    for distanca, duzina, karakter in kompresovani_podaci:
        file.write(distanca.to_bytes(2, 'big'))
        file.write(duzina.to_bytes(1, 'big'))
        file.write(karakter.to_bytes(1, 'big'))

with open(output_file_path_kompresovani_podaci, 'rb') as file:
    kompresovani_podaci = []
    while chunk := file.read(4):
        distanca = int.from_bytes(chunk[0:2], 'big')
        duzina = chunk[2]
        karakter = chunk[3]
        kompresovani_podaci.append((distanca, duzina, karakter))

dekompresovani_podaci = lz77_decompress(kompresovani_podaci)

with open(output_file_path_dekompresovani_podaci, 'wb') as file:
    file.write(dekompresovani_podaci)
