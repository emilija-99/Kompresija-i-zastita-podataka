##### Huffman Coding

Kodovi generisani Huffanovim algoritmom jesu kodovi koji su prefiksni i otpimalni kodovi za dati model (grupu verovatnoća).

Algoritam konstrukcije Huffman Code:
1. Ako je |A| = 2, kontruisemo V = {0,1}, ako je |A| > 2, nastavljamo
2. Sortiraje alfabeta izovora na osnovu verovatnoce p1,p2...pa
3. Spajamo slova s_a-1 i s_a u jedno s_a-1,a i formiramo novu raspodelu (A',p')
gde je A' = {s1...s_a-2,s_a-1,a} i p'(s) = pi p'(s_a-1,a) = p_a-1+p_a
4 Algoritam zatim primenjujemo rekurzivno na raspodelu (A',p')

Prosečnu dužina kodnih reći, računamo kao verovatnoću pojavljivanja simbola i pomnožimo je sa dužinom njene kodne reči.
Nakon generisanja kodnih reči, dobili smo da je *Prosečna dužina Huffman kodova (Lh): 5.967411041259766 bita po simbolu.*.

Mera efikasnosti koda je redudansa koja se računa kao razlika između entopije i prosešne dužine kodnih reci.

redudancy = H(X) - Lh = 0.012

