##### LZW Kompresija

Inicijalizuje se tabela od svih 8-bit ulaznih vrednosti

Kodiranjem LZW algoritmom obradjuju se podaci sa leva na desno, pronalazeći 
najduži niz podataka koji odgovara unosu u tabeli. Kada se pronadje podudaranje,
ispiše se odgovarajući kod i dodaje se sledeći ulazni simbol nizu, a zatim se
dodaje novi niz u tabelu.

Dekodiranje koristi istu tabelu kako bi isti postupak ponovili, unazad.
