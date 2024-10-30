from itertools import product
def generate_all_codewords(length):
    return [''.join(code) for code in product('01', repeat=length)]

def generate_bn_sets(V,n):
    bn_sets = []
    for i,v in enumerate(V, start = 1):
        codewords = generate_all_codewords(n)
        print(codewords)
        if len(v) < n:
            codewords = [code + 'X' * (n - len(v)) for code in codewords]
        bn_sets.append(set(codewords))
        print(bn_sets)
    return bn_sets

V = {'01','10','1110'}
n = max(len(v) for v in V)

Bn_sets = generate_bn_sets(V,n)

total_words = sum(len(Bn_sets) for set in Bn_sets)
print("Total count of words: ", total_words)
print('2^n: ', 2**n)