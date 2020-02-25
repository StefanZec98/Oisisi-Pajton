import re
import os
from Parser import Parser
from Graf import Graph
from time import time
from Trie import *
import  copy
from Obrada import  pretraga_rangiranje

if __name__ == '__main__':

    print("Popunjavanje grafa i stabla...")

    parser = Parser()
    rootdir ='C:\\Users\\stefan\\Desktop\\Oisisi-projekat2\\Oisisi-Pajton\\python-2.7.7-docs-html'
    recnik = {}  # recnik u koji kao kljuc ide putanja a kao vrednost ide trie svih reci
    brojac = 0
    graf = Graph()
    pocetnoVreme = time()
    root=TrieNode("*")

    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # if file.endswith(".html"):
            if os.path.join(subdir, file).strip()[-4:] == 'html':

                putanja = os.path.abspath(subdir + os.sep + file).lower()
                reci = parser.parse(putanja)[1]
                linkovi = parser.parse(putanja)[0]

                cvor = graf.insert_vertex(putanja)
                for i in linkovi:
                    cvor1 = graf.insert_vertex(i)
                    graf.insert_edge(cvor, cvor1, i)
                for rec in reci:
                    add(root, rec.lower(), cvor)
                recnik[putanja] = root

    krajnjeVreme = time()
    Vreme_popunjavanja = krajnjeVreme - pocetnoVreme
    print("Vreme popunjavanja: " + str(Vreme_popunjavanja) + " sekudni.")

    #print(graf.vertex_count())

#----------------------------------------------------------------
    unet_tekst = ""
    while unet_tekst.lower() != 'izlaz':

        print("\n")
        print("Odradice se pretraga rangiranje i ispis rezultata istovremeno")
        print("Nakon toga ce te imati mogucnost paginacije rezultata pretrage\n")
        print("Ukucajte rec ----IZLAZ----- za gasenje programa\n")
        print("--------  REC--OPERATOR--REC!! || REC--REC--REC...  ----------")

        unet_tekst = input(">>> ")
        if unet_tekst.lower() == 'izlaz':
            break

        pretraga_rangiranje(recnik, unet_tekst, graf,root)






