import os 
import heapq
# racunaj verovatnoce
def frekvencije(podaci):
    frekvencije = {}
    for karakter in podaci:
        if karakter in frekvencije:
            frekvencije[karakter] += 1
        else:
            frekvencije[karakter] = 1
    
    print("Frekvencije pojavljivanja karaktera: ")
    for karakter, frekvencija in frekvencije.items():
        print(f"  {chr(karakter)}: {frekvencija}")

    return frekvencije

# kreiranje Node klase
class Node:
    def __init__(self, frekvencija, slovo=None, levo=None, desno=None):
        self.frekvencija = frekvencija
        self.slovo = slovo
        self.levo = levo  
        self.desno = desno
    
    def __lt__(self, other):
        return self.frekvencija < other.frekvencija

# kreiranje min_heap-a na osnovu 
# root node je heap[0], najmanja frekvencija
def minHeapFreq(frekvencije):
    # leaf nodes
    heap = [Node(slovo=s,frekvencija=f) for s,f in frekvencije.items()]
    heapq.heapify(heap) 
    return heap

def huffmanovoStablo(podaci)->Node:
    if not podaci:
        return None
     
    heap = minHeapFreq(frekvencije(podaci))

    ## samo jedan simbol
    if len(heap) == 1:
        jedini = heapq.heappop(heap)
        roditelj = Node(slovo=None, frekvencija=jedini.frekvencija, levo=jedini, desno=None)
        return roditelj

    # vise simbola, kreiraj stablo
    while len(heap)>1:
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        sumMinimuma = Node(slovo=None, frekvencija=min1.frekvencija + min2.frekvencija, levo=min1, desno=min2)
        heapq.heappush(heap, sumMinimuma)
    
    return heapq.heappop(heap)

def generisiKodove(root:Node):
    if root is None:
        return {}
    
    kodovi = {}
    def pom(node, kod):
        if node is None:
            return
        # leaf node
        if node.slovo is not None:
            kodovi[node.slovo]=kod if kod !="" else "0"
            return
        
        pom(node.levo, kod + "0")
        pom(node.desno, kod + "1")
    pom(root, "")
    return kodovi

def dekodirajHuffmana(text,root):
    if root is None:
        return ""

    output, node = [], root

    for karakter in text:
       node = node.levo if karakter == "0" else node.desno
    #    print(node.slovo, karakter)
       if node.slovo is not None:
           output.append(chr(node.slovo))
           node = root

    return ''.join(output)

def enkodirajHuffmana(text, kodovi):
    return ''.join(kodovi[(karakter)] for karakter in text)

def upisiFajl(out_path, podaci):
    with open(out_path, 'a', encoding='utf-8') as f:
        f.write(podaci)

input_path = f"_projekat_1\\output\\random-ascii.bin"
dekodiraj_path = f"_projekat_1\\output\\huffmanov-code\\huffman-code-dekodirani.txt"
enkodiraj_path = f"_projekat_1\\output\\huffmanov-code\\huffman-code-enkodirani.txt"

with open(input_path, 'rb') as file:
    podaci = file.read()

root = huffmanovoStablo(podaci)
kodovi = generisiKodove(root)
frekvencije = frekvencije(podaci)

Lh = 0
for karakter, frekvencija in frekvencije.items():
    for slovo, kod in kodovi.items():
        if karakter == slovo:
            print(f"Karakter: {chr(karakter)}, Frekvencija: {frekvencija}, Kod: {kod}")
            Lh += frekvencija * len(kod)

print(f"Prosečna dužina Huffman kodova (Lh): {Lh / len(podaci)}")

print("Huffman kodovi:")
ch_kodovi = ""
for slovo, kod in kodovi.items():
    ch_kodovi += f"{chr(slovo)}: {kod}\n"
    print(f"  {chr(slovo)}: {kod}")

upisiFajl(enkodiraj_path,ch_kodovi)

enkodirani = enkodirajHuffmana(podaci, kodovi)
print(f"Enkodirani podaci: {enkodirani}")

dekodirani = dekodirajHuffmana(enkodirani, root)
print(f"Dekodirani podaci: {dekodirani}")

upisiFajl(enkodiraj_path, enkodirani)
upisiFajl(dekodiraj_path, dekodirani)