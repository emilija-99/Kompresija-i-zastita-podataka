## Shannon-Fano
Postupak konstukcije prefiksnog koda. Shannon fano nam pokazujemo
mogućnost definisanja prefiksnog koda, ali ne garantuje nam da je taj kod
optimalan kod.

Optimalan kod se nalazi u granicama: `H(x) / log_2b <= (H(x) / log_2b) + 1`

Algoritam za kontrukciju:
1. Sortiranje simbola na osnovu njihovih frekvencija
2. Uzimamo dva simbola, na osnovu veličine verovatnoća dodeljujemo prvom kodu 0, a drugom dodeljujemo 1
3. Skup delimo na dva dela
- jedan skup čine verovatnoće od p1,.. pi, a drugi pi+1,...pn
Potrebno je da apsolutna razlika suma verovatnoća bude minimalna
3. Slovima koja se nalaze od a1...ai dodeljujemo simbol 0, a slobima od ai+1...an dodeljujemo simbol 1
4. Postupak primenjujemo na svaki od novodobijenih skupova

Primer:
    1   2   3   4   5   6
X: 0.5 0.1 0.1 0.1 0.1 0.1
A   pi      I       II      III     IV      V
1   0.5     0                           0
2   0.1     1       0       0           100
3   0.1     1       0       1           101
4   0.1     1       1       0           110
5   0.1     1       1       1       0   1110
6   0.1     1       1       1       1   1111

nv = 1 * 0.5 + 3 * 0.1 + 3 * 0.1 + 4 * 0.1 + 4 * 0.1 = 2.5
