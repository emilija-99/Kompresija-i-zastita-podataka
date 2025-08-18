##### LZ77

*!Prva implementacija LZ77 bila je pogodna sa malom količinom podataka. Nakon izmene veličine fajla koji se kodira, vreme za kodiranje i
dekodiranje je postalo različito od optimalnog.*
Algoritam kompresije bez gubitaka koji mapira podatke zamenjujući
duplikatne delove podataka metapodacima (offset, length, ch)

Search_buffer: predstavlja istoriju obradjenih podataka zankova fiksne dužine u kojoj algoritam
pretražuje dupliate segmenta.

Lookahead_buffer: Bafer za unapred pretraživanje je skup znakova
fiksne dužune gde algoritam traži najduže podudaranje

Sliding_window: Obuhvata search_buffer, lookahead i poziciju ulaznog karaktera

abcbbcbaaaaaa

search_buffer = 6
lookahead = 5
coding position = 0
[a b c b b c b a a a a a a]

sliding_window
[a b c b b c]
[0 1 2 3 4 5]

[0,0,a]

sliding_window
[a  b c b b c a]
[-1 0 1 2 3 4 5]

[0,0,b]

[a   b c b b c a a]
[-2 -1 0 1 2 3 4 5]

[0,0,c]

[a   b c  b b c a a a]
[-2 -1 -3 0 1 2 3 4 5]

2 karaktera, na prvoj poziciji sliding_widowa, karakter
[2,1,b] dva ponavljanja karaktera b koji se nalazi na poziciji 1
[3,2,a] dva karaktera 3:3+2
[1,5,''] 5 karaktera sa pozicije 1

abcbbcbaaaaa


source: https://dev.to/vincent_corbee/lz77-compression-in-javascript-4nec