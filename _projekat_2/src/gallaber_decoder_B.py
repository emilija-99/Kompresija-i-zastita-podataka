import sys
from itertools import combinations
sys.path.insert(1, 'C:\\Users\\Emilija\\Documents\\Kompresija-i-zastita-podataka\\_projekat_2\\src')
import H_matrica as H
import sindrom_korektor as sk
import random

H = H.H
# vektor e se generise kao kombinacije nula i jedinica
# posto imamo n = 15, onda imamo 2^15 = 32768 kombinacija

# Nalaženje korekcionog vektora e takvkvog da je min dh(y-e,y) = min wh(e)
# Vektor sT = H * yT raćunamo na osnovu primljene reći y - sindorm
# Vektor e takav da je wh(e) minimalno i HeT + sT naziva korektor

def sindrom(H, e):
    m, n = len(H), len(H[0])
    sindrom = [0]*m
    return tuple(
        sum((H[r][c] & e[c]) for c in range(n)) % 2
        for r in range(m)
    )

def generisiSveKombinacijeZaKorektor(tezina, n):
    kombinacije = []
    for t in range(1, tezina + 1):
        for pozicije in combinations(range(n), t):
            kombinacija = [0] * n
            for pozicija in pozicije:
                kombinacija[pozicija] = 1
            kombinacije.append(kombinacija)
    
    # prikazivanje kombinacija
    # for i, kombinacija in enumerate(kombinacije):
    #     print(f"{i + 1}: {kombinacija}")
    return kombinacije

def izracunavanjeSindroma(H, e):
    m, n = len(H), len(H[0])
    sindrom = [0] * m
    for i in range(m):
        sindrom[i] = sum(H[i][j] * e[j] for j in range(len(e))) % 2
    return tuple(sindrom)

def sindromKorektorTabela(H):
    m,n = len(H), len(H[0])
    sindromTabela = {}

    tezina = 2 * (n - m) + 1
    errorKombinacije = generisiSveKombinacijeZaKorektor(tezina, n)
    # print("LEN:" , len(errorKombinacije))
    for e in errorKombinacije:
        sindrom = izracunavanjeSindroma(H, e)
        # print("sindrom : ",sindrom)
        tezina_e = sum(e)
        #  generisanje se zaustavlja kada dva vektora e daju iste tezina za sindrom
        if sindrom not in sindromTabela or tezina_e < sindromTabela[sindrom][0]:
            sindromTabela[sindrom] = (tezina_e, e)

    print("Tabela sindroma i korektora:")
    for sindrom, (tezina, korektor) in sorted(sindromTabela.items()):
        sindrom_str = ''.join(map(str, sindrom))
        korektor_str = ''.join(map(str, korektor))
        print(f'Sindrom: {sindrom_str} -> Korektor: {korektor_str} (težina: {tezina})')

    return sindromTabela

# xor nad vektorima - broji razlike u ne nela vrednostima vektora x,y
def hammingRastojanje(x, y):
    distanca = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            distanca += 1
    return distanca
# parity check - proverava da li je vektor x validan prema H matrici
def parityCheck(H, x):
    # return [(sum(H[i][j] * x[j] for j in range(len(x))) % 2) for i in range(len(H))]
    m, n = len(H), len(H[0])
    s = [0] * m
    for i in range(m):
        acc = 0
        for j in range(n):
            if H[i][j]:
                acc ^= (x[j] & 1)
        s[i] = acc
    return s

# d(C) - minimalan broj linerasno zavisnik kolona matice H
# a1v1 + a2v2 + ... + amvm = 0
# minimalan broj kolona koje su linearno nezavisne
# martice H je broj ne nula elementa neke kodne reci
def kondneReci():
    n = len(H[0])
    kodne_reci = []
    
    for i in range(2 ** n):
        bin_rec = [int(b) for b in format(i, f'0{n}b')]
        sindrom =  [sum(bin_rec[j] * H[k][j] for j in range(n)) % 2 for k in range(len(H))]
        if all(s == 0 for s in sindrom):
            kodne_reci.append(bin_rec)
    return kodne_reci

def izracunajKodnoRastojanaje(kodneReci):
    brojReci = len(kodneReci)
    min_rastojanje = float('inf')
    
    for i in range(brojReci):
        for j in range(i + 1, brojReci):
            rastojanje = hammingRastojanje(kodneReci[i], kodneReci[j])
            if rastojanje < min_rastojanje:
                min_rastojanje = rastojanje
    return min_rastojanje



def GallegerDekoderB(H, vektor, threshold_0=0.5, threshold_1=0.5, iter = 100):
    m,n = len(H), len(H[0])

    # m provara vrsta, n bitova kolona
    inicijanaPoruka = [[0] * m for _ in range(n)]
    
    for j in range(n):
        bit = vektor[j] & 1
        for i in range(m):
            if(H[i][j] == 1):
                inicijanaPoruka[j][i] = bit

    # (i,j) dobija pocetnu poruku

    x = vektor[:]

    for _ in range(iter):
        provera = [[0]*n for _ in range(m)]
        for i in range(m):
            par = [j for j in range(n) if H[i][j]]
            if not par:
                continue
            ukupnoParity = 0
            for j in par:
                ukupnoParity ^= inicijanaPoruka[j][i] # xor svih dolazih poruka iz susednih promenljivih
            for j in par:
                provera[i][j] = ukupnoParity ^ inicijanaPoruka[j][i]
        # za svaki red i racunamo xor svih dolaznih poruka iz susednih promeljivih
        # za svaku susednu promenljivu j vraca paritet bez j
        
        X = x[:]
        
        # check, x
        for j in range(n):
            nb = [i for i in range(m) if H[i][j]]
            d = len(nb)
            if d == 0:
                continue
            
            votes1 = sum(provera[i][j] for i in nb)
            vores0 = d - votes1

            thr0 = (d*threshold_0 + 0.999999999) // 1 # celi
            thr1 = (d*threshold_1 + 0.999999999) // 1

            if vores0 >= thr0: # postavi 0 za vece od granice
                X[j] = 0
            elif votes1 >= thr1: # postavi 1 za vece od granice
                X[j] = 1
            else:
                pass

        if (sum(parityCheck(H,X)) == 0): # ako je H * XT = 0 mod 2 kraj
            return X 
        
        for j in range(n):
            bit = X[j] & 1
            for i in range(m):
                if H[i][j]:
                    inicijanaPoruka[j][i] = bit

        x = X 
    return x

def greska(H, threshold_0=0.5, threshold_1=0.5):
    n = len(H[0])
    tezina = n

# ocekivana dekodirana rec kada je poslata nulta kodna rec
    dekodiranaRec = [0]*n 

    for i in range(1, n+1):
        for poz in combinations(range(n),i):
            e = [0] * n 
            for p in poz:
                e[p] = 1
        
            # primljeno
            x = GallegerDekoderB(H,e,threshold_0,threshold_1)

            if x != dekodiranaRec:
                return i, poz, e, x 
            
    return None,None,None,None


def dekodirajTabeluSindroma(y, H, sindrom_tabela):
    s = sindrom(H, y)
    # print("Sindrom:", s)
    e_hat = sindrom_tabela.get(s, [0]*len(y))
    # print("Korektor:", e_hat)
    x_hat = [yi ^ ei for yi, ei in zip(y, e_hat)]
    # print("Dekodirani vektor:", x_hat)
    return x_hat, e_hat, s
# x, ok = GallerDekoder(H, r, T = 2)#
# print("Dekodirani vektor:", x, ok)

# print("sindrom pre:", sindrom(H, r))#
# print("sindrom posle:", sindrom(H, x))

# Kreiranje kombinacija error vektora i izračunavanje sindroma
kombinacije = generisiSveKombinacijeZaKorektor(3, 15)

# test za izračunavanje sindroma
sindrom_test = izracunavanjeSindroma(H, kombinacije[3])

# print("Sindromi:", sindromi)#
sindromKorektor = sindromKorektorTabela(H) # 2 ^ 15 = 32768 kombinacija

y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # primer primljenog vektora

# out = dekodirajTabeluSindroma(y, H, sindromKorektor)
# print("Dekodirani vektor:", out[0])

kodne_reci = kondneReci() 

# kodno rastojanje
kodno_rastojanje = izracunajKodnoRastojanaje(kodne_reci)
print(f"Rastojanje koda: {kodno_rastojanje}")

random_vektor = [random.randint(0, 1) for _ in range(len(H[0]))]
#print("Random vektor: ", random_vektor)
#dekodirani_vekor = GallegerDekoderB(H, random_vektor)
#print("Dekodirani vektor:", dekodirani_vekor)

greska = greska(H)

print(f"Minimalna neuspesna tezina koju nije moguce da ispravi: {greska[0]}.\n Pozicija na kojoj se dogodila greska {greska[1]}, greska e je: {greska[2]}.\n Dekoder je vratio: {greska[3]}")
# print(parityCheck(H,greska[2])) # test

