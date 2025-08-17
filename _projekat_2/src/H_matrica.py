import random 
n = 15
nk = 9
wr = 5
wc = 3

grupe_redova = nk // wc

H = [[0]*n for _ in range(nk)]

# generisanje I Grupe redova
for i in range(grupe_redova):
    for c in range(i*wr, (i+1)*wr):
        H[i][c] = 1

def permutacije_grupa(seed, redovi, offset):
    kolone = list(range(n))
    random.Random(seed).shuffle(kolone)

    for _r, red_ind in enumerate(redovi):
        jedinice = [j for j, v in enumerate(H[red_ind]) if v == 1]
        for j in jedinice:
            H[offset+_r][kolone[j]] = 1

# generisanje II i III Grupe redova
base = list(range(grupe_redova)) #0,1,2

permutacije_grupa(114, base,  grupe_redova)
permutacije_grupa(114, base, 2*grupe_redova)

for i, row in enumerate(H, 1):
    print(f"{i:2d}: {' '.join(map(str,row))}")