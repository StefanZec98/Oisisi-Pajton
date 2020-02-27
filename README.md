# Oisisi-Pajton
Idemo kroz sve fajlove na nekoj putanji i uzimamo njihove absolutne putanje.
Pozivamo parser na toj absolutnoj putanji i on nam vraca reci i linkove za tu 
putanju.Idemo kroz sve reci i linkove i popunjavamo graf i stablo.

Dodavanje reci u stablo:
	Funkcija ima parametre root - koji predstavlja koren stabla na koji dodajemo rec
zatim word - predstavlja rec koji zelimo da upisemo u stablo i html_word - koja predstavlja
putanju.
	Algoritam - prolazimo kroz sve karaktere prosledjene reci i pokusavamo da
nadjemo trenutni karakter kod node.children ukoliko nadjemo proglasavamo da je node=child
ukoliko ne nadjemo karakter kod node.children onda ga pravimo new_node = TrieNode(char)
i proglasavamo node = new_node.Na kraju ubacujemo rec u recnik - ukoliko vec postoji samo
povecavamo counter a u suprotnom setujemo na 1.Funkcija vraca broj karaktera u reci.

Trazenje reci u stablu: 
	Funkcija ima parametre root - prestavlja koren stabla kojin je dodeljen
i word - rec koju trazimo.
	Algoritam - ako cvor nema decu znaci da je prazan i vraca False,0.
Imamo 2 for petlje u prvom prolazimo kroz karaktere reci koje trazimo a u drugoj
kroz node.children ukoliko se ne pronadje karakter u drugom foru znaci da ne postoji
ta rec i vracamo False,0.Ukoliko smo uspeno prosli kroz prvi for vracamo True i broj
pronalazaka te reci. 

Pretraga:
	Funkciji su iz Main klase prosledjene reci za koje je potrebno izvrsiti pretragu
od tih reci pravimo listu reci sa tim da svako bude lower case i zatim u while petlji
gledamo koji operand je u pitnju (rec operand rec,nalazi se na [1] poziciji) i u odnosu na
njega pozivamo odgovarajucu funkciju iz Seta koji smo prethodno inicijalizovali.


Popunjavanje grafa:
       cvor je cvor na toj absolutnoj putanji. Cvor1 je cvor u foru gde idemo kroz
 sve linkove. U metodi insert_edge povezujemo ova dva cvora sa pomocnim elementom x
 kojije u ovom slucaju link.

Rangiranje:
	
	Funckija prima recnik gde je kljuc html stranica a vrednost broj reci na 
toj stranici.Idemo kroz kljuceve recnika tj html stranice koje su u ovom slucaju 
cvorovi.Uzimamo broj pojavljivanja reci na toj stranici i mnozimo sa 3. Preko 
graf.incident_edges za tu stranicu, posto je graf usmeren dobijamo broj ulaznih
ivica. U rang uvrstavamo i broj ulaznih ivica pomnozeno sa 0.15. Idemo kroz sve
ulazne ivice i dobijamo cvorove sa druge strane, tj komsije i gledamo broj
pojavljivanja reci u njima i mnozimo sa 0.15, pod uslovom da se vec nalaze u ulaznom
recniku te stranice. Tako formiramo za svaku stranicu rang. Pravimo novi recnik
gde je vrednost html stranica a vrednost rang.


Bubble sort:
	Uporedjujemo prvi i drugi elemenat - ako nisu poredjani kako se trazi, menjamo
im mesta. Onda uporedjujemo drugi i treci element, opet, ako nisu poredjani, menjamo im mesta
...
tako nastavljamo da uporedjujemo dva po dva elementa i da im menjamo mesta ako je potrebno sve dok ne doguramo do kraja
(u tom trenutku je poslednji element garantovano najveci, dok su svi ostali elementi za po malo pomereni u pravom smeru)
zatim sve to radimo ispocetka, ali ne idemo do poslednjeg već do pretposlednjeg elementa

Paginacija:
	Omogucili smo prikaz po stranicama uz pomoc django paginatora. On nam omogucava da dinamicki promenimo
prikaz stranica po rezultatu
