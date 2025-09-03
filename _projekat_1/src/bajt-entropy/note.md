## Bajt Entropija

#### Definicija izračunavanja Entorpije:
`H(x) = EI(X) = sum(p(x)I(x)) = -sim(p(x)log_2p(x))`

`H(X)` rezultat izračunacanje entropije predstavlja **srednju količinu informacija** koju nosi X (izvorni fajl 'random-ascii.bin').

#### Objasšnjenje postupka izračunavanja:
Prema ulazim podacima sačuvanim u fajlu random-ascii.bin generisanih na osnovu izvornog alfabeta A*, izračunavanjem entorpije dobili smo vrednost 
koja je ~5.95 i koja predstavlja prosećan broj bitova potrebnih za predstavljanje kodnih simbola prilikom kodiranja kodnih reči.

Prilikom računa entropije potrebno je da se svaki ulazni simbol predstavi svojom verovatnoćom. 
Verovatnoća ozačava kolika je neizvesnot pojavljivanja tog simbola u ulaznom fajlu. 

Za svaki simbol xi imamo verovatnoću p(xi) datu kao broj pojavljivanja datog simbola / ukupan broj simbola.

Rezulatat izračunavanja verovatnoće simbola xi:
- simbol čija je vrednost verovatnoće manja, označava da je zastupljenost u našim ulaznim podacima "redje"
- simbol čija je vrednost verovatnoće je velika označava da je zastupljenost u našim podacima "česta"

Alfabet koji smo koristili za kodiranje: `8qEkCTNVUpueDiWb6j5G0QxYmnLOFc17J3MwXHIAhgltszRr2v9dZKPSofB4ay`
b = 62

Granične vrednosti za srednju dužinu kodne reči u oznaci nv:
n*= inf nv

H(X) <= nv <= H(X) + 1
5.95 < n <= 6.95 