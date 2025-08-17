import sys
from itertools import combinations
sys.path.insert(1, 'Kompresija-i-zastita-podataka\\_projekat_2\\src')
import H_matrica as H

H = H.H

# generisanje simbola dato je: s^t:=H_y^t
def tabelaSindromaKorektora(H, v):
    m, n = len(H), len(H[0])
    out = {}
    for w in range(0, v+1):
        for pozicije in combinations(range(n), w):
            e = [0] * n
            for p in pozicije:
                e[p] = 1
            sindrom = tuple(sum(H[i][j] * e[j] for j in range(n)) % 2 for i in range(m))
            if sindrom not in out:
                out[sindrom] = (e,w)
    return out

tabelaSindromKorektor = tabelaSindromaKorektora(H, 3)
for i, (s, (e, w)) in enumerate(tabelaSindromKorektor.items()):
    print("s =", ''.join(map(str,s)), "-> wH(e):", w, " sT:", [k+1 for k,b in enumerate(e) if b])