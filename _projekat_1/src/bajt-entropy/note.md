### Bajt Entropija

Definicija izračunavanja Entorpije: 
`H(x) = EI(X) = sum(p(x)I(x)) = -sim(p(x)log_2p(x))`

H(x) rezultat koji dobijamo ovim izračunavanjem je **srednja količina informacija** koju X nosi.

Prema ulazim podacima sačuvanim u fajlu random-ascii.bin, izracunavanjem entorpije dobili smo vrednost koja je ~5.14 sto nam da srednja količina informacija koju naši podaci nose se približno kodira sa 5 bitova.

Kodiranje simbola u zavisnosti od njihove verovatnoce:
- simboli sa manjom verovatnoćom - veća gustina pojavljivanja - manji broj
bitova za kodiranje (informacija koju dati simbol nosi u sebi je manja)
- simboli sa većom verovatnoćom - manja gustina pojavljivanja - veći broj bitova
potrebnih za kodiranje (informacija koju dati simbol nosi u sebi je veća)

Kako koristimo ascii - 256 simola, gde je log_256 = 8bita
Dobijeni rezulat od 5.16 oznacava da su podaci nasumicni, ali ne potpuno uniformni.