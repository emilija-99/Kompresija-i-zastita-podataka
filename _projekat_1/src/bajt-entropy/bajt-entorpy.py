import os
import math 
import matplotlib.pyplot as plt

lenght = 0;
container = {}

print("Izačunavanje entropije: ");

file_path = os.path.join(r"_projekat_1\output\random-ascii.bin")
with open(file_path, 'r') as file:
    while True:
        content = file.read(1)
        if not content:
            break
        container[content] = container.get(content,0)+1
        lenght+=1

print("Broj jedinstvenih simbola u fajlu: ", len(container.keys()))

for simbol, pojavljivanje in container.items():
    print(f"Simbol: {simbol}, broj pojavljivanja: {pojavljivanje}, verovatnoca za simbol: {pojavljivanje/lenght}")

H = 0
for freq in container.values():
    if(freq):
        Hi = freq/lenght # verovatnoca pojavljivanja karaktera - velicina informacija koju poruka nosi p(x)
        H -= Hi * math.log2(Hi) # H(X) = -sum(p(x) * log2(p(x))) ili EI[x] matematicko ocekivanje slusajne promenljive I(x)

print("Entropija - Prosešna informacija po bitu iznosi: ", H , "bita.");

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