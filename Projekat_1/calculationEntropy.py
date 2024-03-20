import os
import math 

lenght = 0;
container = {}

file_path = os.path.join("C:\\Users\\EliteBook 830 G6\\Desktop\\FAX\\Kompresija i zastita podataka", "file.txt")
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
        Hi = freq/lenght
        H -= Hi * math.log2(Hi)

print("Entropy of file is:", H);



