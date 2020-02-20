import re
import os

from Parser import Parser
from Graf import Graph
from time import time



if __name__ == '__main__':
    parser = Parser()
    rootdir = 'C:\\Users\\stefan\\Desktop\\Drugi projekat oisisi\\python-2.7.7-docs-html'

    brojac = 0
    graf = Graph()
    pocetnoVreme = time()
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            # if file.endswith(".html"):
            if os.path.join(subdir, file).strip()[-4:] == 'html':

                putanja = os.path.abspath(subdir + os.sep + file).lower()
                reci = parser.parse(putanja)[1]
                linkovi = parser.parse(putanja)[0]
                for i in linkovi:
                    graf.addEdge(putanja, os.path.abspath(i).lower())


   # print(graf.__str__())

    print(graf.getVertices())

    krajnjeVreme = time()
    Vreme_popunjavanja = krajnjeVreme - pocetnoVreme
    print("Vreme popunjavanja: " + str(Vreme_popunjavanja) + " sekudni.")
