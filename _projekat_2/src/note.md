##### Konstuisanje matice H LDPC koda 

n = 15
n-k = 9
wr = 5
wc = 3

LDPC kodovi su linerni kodovi sa kontolnom matricom H.
Regularni LDCP kodovi zadovoljavaju svojstvo da svaki red, odnosno kolona matrice H sadrzi wr, odnosno wc jedinica.
Matrica je retka ako vazi wr << m i wc << n

Algoritam:
Prvih (n-k)/wc redova dobijaju se tako sto se napre upise we jedinica
u prvi red kolone (kolone sa indeksima od 1 do wr), zatim se predje u sledeci red i opet se upise wr jedinica (kolone sa indeksima wr+1 do 2wr), itd.
Ostalih wc-1 grupa redova dobijaju se permutacijom kolona prve grupe redova

Trazeno:
Generisanje 2. i 3. grupe redova koristiti standardni generator
pseudoslucajnih brojeva sa fiksniranim seed-om, jednakim broju indeksa.

Grupe kolona:
I Grupa:
1. 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0
2. 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0 
3. 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1

II Grupa:
4. 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0
5. 1 0 1 0 1 0 1 0 0 0 0 0 0 0 1
6. 0 1 0 1 0 1 0 0 0 1 1 0 0 0 0

III Grupa:
7. 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0
8. 1 0 1 0 1 0 1 0 0 0 0 0 0 0 1
9. 0 1 0 1 0 1 0 0 0 1 1 0 0 0 0


Na osnovu ovako konstruisane matrice H, generisati tabelu sindroma i korektora i odrediti
kodno rastojanje ovog koda.

Nakon konstrukcije matrice H oblika:
              c6  c8       c13
 1: 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0
 2: 0 0 0 0 0 1 1 1 1 1 0 0 0 0 0
 3: 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1
 4: 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0
 5: 1 0 1 0 1 0 1 0 0 0 0 0 0 0 1
 6: 0 1 0 1 0 1 0 0 0 1 1 0 0 0 0
 7: 0 0 0 0 0 0 0 1 1 0 0 1 1 1 0
 8: 1 0 1 0 1 0 1 0 0 0 0 0 0 0 1
 9: 0 1 0 1 0 1 0 0 0 1 1 0 0 0 0

Potrebno je generisati tabelu sindroma i korektora i odrediti kodno rastojanje.
Generisanje sindroma:
vektor e: kombinacije duzine n - korektor
wh(e) -> na osnovu vekrora c1...cn - racunas koliko ima ne nula
sT = H'eT - radis vektorko XOR nad elementima koji su ne nula 

e: 000010100001000
wh(e) = 3

c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 c11 c12 c13 c14 c15
0 0 0 0 0 0 0 1 1 0 0 1 1 1 0

sindrom = c6 + c8 + c13 = 
(010001001) + 
(010010010) + 
(001100100) =
 011111110 

