##### Huffman Coding
Huffmanov algritam nam služi za kreiranje optimalnog koda.

Algoritam konstrukcije optinalnog koda:
1. Ako je |A| = 2, kontruisemo V = {0,1}, ako je |A| > 2, nastavljamo
2. Sortiraje alfabeta izovora na osnovu verovatnoce p1,p2...pa
3. Spajamo slova s_a-1 i s_a u jedno s_a-1,a i formiramo novu raspodelu (A',p')
gde je A' = {s1...s_a-2,s_a-1,a} i p'(s) = pi p'(s_a-1,a) = p_a-1+p_a
4 Algoritam zatim primenjujemo rekurzivno na raspodelu (A',p') 

Entropija: 
H(X) = ~5.14

Prosečna dužina Shannon-Fano kodova (Ls): 5.7875
Prosečna dužina Huffman kodova (Lh): 5.76875

(5.14) <= 5.77 <= 5.79 < (5.14 + 1)
