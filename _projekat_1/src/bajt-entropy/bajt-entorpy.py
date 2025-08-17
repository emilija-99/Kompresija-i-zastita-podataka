import os
import math 
import matplotlib.pyplot as plt

lenght = 0;
container = {}

print("Racunanje Entropije: ");

file_path = os.path.join(r"_projekat_1\src\bajt-entropy\bajt-entorpy.py")

"""
    Podaci se ucitavaju iz fajla, a zatim se broje koliko puta se pojavljuju
    pojedini bajtovi. Na kraju se racuna entropija fajla.

    Entropija se racuna kao H = -sum(p(x) * log2(p(x))), 
    gde je p(x) verovatnoca pojavljivanja bajta x.
    
    Entropija daje informaciju o nasumicnosti raspodele bajtova u fajlu.
    Ako je entropija niska, bajtovi se ponavljaju cesto,
    a ako je visoka, raspodela bajtova je nasumicna.
"""

with open(file_path, 'r') as file:
    while True:
        content = file.read(1)
        if not content:
            break
        container[content] = container.get(content,0)+1
        lenght+=1

H = 0

for freq in container.values():
    if(freq):
        Hi = freq/lenght # verovatnoca pojavljivanja bajta
        H -= Hi * math.log2(Hi) # H(X) = -sum(p(x) * log2(p(x)))

print("Entropija - Prosešna informacija po bitu iznosi: ", H , "bita.");

print("Znacenje vrednosti entropije ")
if(H <= 1):
    print("Raspodela bajtova u fajlu nije nasumicna. Informacije u vidu bajova se ponvaljaju previse cesto.")
elif(H <= 4 and H < 5):
    print("Raspodela bajtova u fajlu nije nasumicna. Informacije u vidu bajova se ponvaljaju, ali ne previse cesto.")
elif(H >=5 and H <=7):
    print("Raspodela bajtova u fajlu jeste nasumicna i veoma pogodna za kompresiju. Informacije u vidu bajtova se ponavljaju umerno.")
else:
    print("Raspodela bajtova u fajlu jeste nasumicna. Fajl je kompresovan.")

print("Prikazivanje grafika pojavljivanja informacijonih bitova i kako oni uticu na entropiju fajla.")
items = sorted(container.items(), key=lambda kv: kv[1], reverse=True)
values = [v/lenght for _, v in items]
labels = [b for b, _ in items]

plt.figure()  
plt.bar(range(len(values)), values) 
plt.xticks(range(len(values)), labels, rotation=90)
plt.title(f"Frekvencije simbola (H = {H:.4f} bita)")
plt.xlabel("Simbol")
plt.ylabel("Verovatnoća")
plt.tight_layout()
plt.show()