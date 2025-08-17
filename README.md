# Kompresija i zastita podataka

##### Struktura seminarskih je odradjena u dva foldera:
- _projekat_1
- _projekat_2

Svaki od foldera prestavlja izradu jednog zadatka.

Projekti su strukturisani u foldere:

###### _projekat_1:
/src - implementacija zadataka po folderima (svaki folder u sebi sadrzi naziv python programa i note - kratki zapisi o svakoj implementaciji)
    /bajt-entopy 
    /huffmanov-code
    /LZ77
    /LZW
    /shannon-fano
    /power-shell-skripta - na ovaj nacin je generisan fajl 1-10MB koji je bio potreban za izradu
/ouput - generisanje .bin i .txt za dekodiranje i kodiranja
    /huffmanov-code
    /lz77-code
    /lzw-code
    /shannon-fano
    /random-ascii.bin - fajl koji je koriscen za kodiranje i dekodiranje
/docs - sadrzi tekst projektnog zadatka i literaturu

###### _projekat_2:
/src
    /gallaber_decoder_B.py - celokupna izrada zadatka
    /H_matrica.py - implementacija H matice
    /note.md - kratki zapisi o implementaciji i primenjenoj teoriji
/output 
/docs - sadrzi pdf dokument sa zadatkom

##### Pokretanje programa u terminalu
Mozete pokretati iz root-a foldera /Kompresija-i-zastita-podataka
Pokretanje Projekta 1
1. Racunanje bajt entropije:
`\Kompresija-i-zastita-podataka> python3 .\_projekat_1\src\bajt-entropy\bajt-entorpy.py`
2. Huffman kodiranje:
`python3 .\_projekat_1\src\huffmanov-code\huffman-code.py`
3. Shannon Fano:
`python3 .\_projekat_1\src\shannon-fano\shannon-fano.py`
4. LZ77
`python3 .\_projekat_1\src\LZ77\lz77-code.py`
5. LZW
`python3 .\_projekat_1\src\LZW\lzw-codee.py`

Pokretanje Projekta 2
`python3 .\_projekat_2\src\gallaber_decoder_B.py`