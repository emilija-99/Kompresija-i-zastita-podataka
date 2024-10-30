def lzw_compress(podaci):
    recnik = {bytes([i]): i for i in range(256)}
    preth = bytes()
    rezultat_kompresije = []
    code = 256

# dinamicki azuriranje recnika i generisanje kompresovanih podataka
    for karakter in podaci:
        sekvenca_karaktera = preth + bytes([karakter])
         # proveravamo da li nova sekvanca karaktera postoji u recniku, ako postoji
         # potrebno je da azuriramo prethnodnu
        if sekvenca_karaktera in recnik:
            preth = sekvenca_karaktera
        # ako sekvenca karaktera ne postoji dodajemo kod prethodnika
        # u rezulata, sekvenca se dodaje u recnik sa novim kodom i kod uvecavamo za 1
        # azurairamo prethodnika sa na treuntni karakter
        else:
            rezultat_kompresije.append(recnik[preth])
            recnik[sekvenca_karaktera] = code
            code += 1
            preth = bytes([karakter])

    if preth:
        rezultat_kompresije.append(recnik[preth])
    
    return rezultat_kompresije

def lzw_decompress(kompresovani_podaci):
    # kreirano recnik i mapiramo karaktere
    recnik = {i: bytes([i]) for i in range(256)}
    # prethodnik je pocetna sekvenca koja se postavlja na prvi kod
    preth = bytes([kompresovani_podaci[0]])
    rezultat_dekompresije = [preth]
    code = 256

    for trenutni in kompresovani_podaci[1:]:
        # ako treutna sekvenca postoji u recniku,
        if trenutni in recnik:
            sekvenca = recnik[trenutni]
        elif trenutni == code:
            sekvenca = preth + preth[0:1]
        else:
            raise ValueError(f'Bad compressed trenutni: {trenutni}')
        
        rezultat_dekompresije.append(sekvenca)
        recnik[code] = preth + sekvenca[0:1]
        code += 1
        preth = sekvenca
    
    return b''.join(rezultat_dekompresije)

input_file_path = 'file.txt'
output_file_path_compressed = 'compressed_lzw.bin'
output_file_path_decompressed = 'decompressed_lzw.bin'

with open(input_file_path, 'rb') as file:
    data = file.read()

compressed_data = lzw_compress(data)

with open(output_file_path_compressed, 'wb') as file:
    for code in compressed_data:
        file.write(code.to_bytes(4, 'big'))

with open(output_file_path_compressed, 'rb') as file:
    compressed_data = []
    while chunk := file.read(4):
        code = int.from_bytes(chunk, 'big')
        compressed_data.append(code)

decompressed_data = lzw_decompress(compressed_data)

with open(output_file_path_decompressed, 'wb') as file:
    file.write(decompressed_data)
