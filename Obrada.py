import operator
from locale import atoi
from Pomocna import *
from Trie import trazi_rec
import re
import os
from Set import *
from django.core.paginator import Paginator


def pretraga_rangiranje(recnik, reci, graf,root):

    s = Set()
    reci2 = reci.lower()
    listaReciBezOperanada = []
    listaReci = reci2.strip().split(" ")
    pravljenjeListe_Recnika_I_Operanada(listaReci, recnik, graf, listaReciBezOperanada,root)
    listaRecnikaIOperanada = listaReci #[recnik1 and recnik2 or recnik3....]

    while len(listaRecnikaIOperanada) != 1:
        if listaRecnikaIOperanada[1] == 'and':
            recnikAND = s.pretragaAND(listaRecnikaIOperanada[0], listaRecnikaIOperanada[2])
            del listaRecnikaIOperanada[0:2]
            listaRecnikaIOperanada[0] = recnikAND
        elif listaRecnikaIOperanada[1] == 'or':
            recnikOR = s.pretragaOR(listaRecnikaIOperanada[0], listaRecnikaIOperanada[2])
            del listaRecnikaIOperanada[0:2]
            listaRecnikaIOperanada[0] = recnikOR
        elif listaRecnikaIOperanada[1] == 'not':
            recnikNOT = s.pretragaNOT(listaRecnikaIOperanada[0], listaRecnikaIOperanada[2])
            del listaRecnikaIOperanada[0:2]
            listaRecnikaIOperanada[0] = recnikNOT
        else:
            recnikOR = s.pretragaOR(listaRecnikaIOperanada[0], listaRecnikaIOperanada[1])
            del listaRecnikaIOperanada[0:1]
            listaRecnikaIOperanada[0] = recnikOR
    ispisRangiranePretrage(listaRecnikaIOperanada[0],listaReciBezOperanada)

def pravljenjeListe_Recnika_I_Operanada(listaReci, recnik1, graf, prosledjeneReci,root):#listaReci, recnik1
    '''
        Funkcija koja menja listu tako da je svaka rec u stvari recnik
        u kojem je kljuc putanja fajla, a vrednost broj pojavljivanja.
        Lista je mutable tako da nije potreban return

        Args:
            listaReci(list): lista reci
            recnik1(recnik): recnik kojem je kljuc putanja a vrednost trie
    '''

    brojac = 0
    for rec in listaReci:
        if rec != 'and' and rec != 'or' and rec != 'not':
            prosledjeneReci.append(rec)

            if(trazi_rec(root,rec)[1]==0):
                return
            pronadjenRecnik=trazi_rec(root,rec)[2]

            #for item in pronadjenRecnik.items():
               # print(item)

            listaReci[brojac] = odrediRang(pronadjenRecnik,graf) #od liste reci pravimo npr recnik1 and recnik 2 or recnik3...
        brojac += 1




def odrediRang(ulazniRecnik,graf):
    rangRecnik = {}
    for key in ulazniRecnik.keys():

        rang = ulazniRecnik[key] * 3 #broj reci na toj stranici tj tom cvoru
        linkovi = graf.incident_edges(key, False) #posto je graf usmeren vraca linkove koji ulazi u cvor
        rang += len(linkovi) * 0.15

        for edge in linkovi:
            prekoputa = edge.opposite(key) #Vraća čvor koji se nalazi sa druge strane čvora v ove ivice.

            if prekoputa in ulazniRecnik.keys():
                rang += ulazniRecnik[prekoputa] * 0.25 #reci preko puta cvora
        rangRecnik[key.element()] = rang #formira recnik gde je vrednost rang
    return rangRecnik


def ispisRangiranePretrage(krajnjiRecnik, prosledjeneReci):
    '''
        Metoda koja od recnika pravi niz objekata, sortira ga i kasnije ispisuje sve rezultate.

        Args:
            krajnjiRecnik(dict): Recnik putanja i vrednosti
        '''

    nizObjekata = []
    try:
        for key, value in krajnjiRecnik.items():
            o=Objekat(key,value)
            nizObjekata.append(o) #niz objekata sa linkovima i rangovima
    except:
        print("Došlo je do greške-uneli ste rec koja ne postoji, pokušajte ponovo!")

    sortiranjePoRangu(nizObjekata) #sortiramo niz objekata po rangu

    broj = 0

    for i in reversed(nizObjekata):
        broj += 1
        print(str(broj) + ": " + "Naziv fajla: " + ispisNazivaFajla(str(i.link)))
        print("Prioritet fajla : " + str(i.rang))

#-------------------PAGINACIJA

    while True:

        N = input("Broj stranica na jednoj stranici: ")
        if N.isdigit():
            N = atoi(N)
            if N > 0:
                paginacijaStranica(nizObjekata, N)
                break
            else:
                break
        else:
            break



def ispisNazivaFajla(link):

    a = link.split("\\")
    return a[-1][:-5]




def sortiranjePoRangu(nizObjekata):  #ovo je bubble_sort
    n = len(nizObjekata)
    if (len(nizObjekata) == 0):
        print("Greska niz je prazan i ne moze da se sortira")

    for i in range(n):
        for j in range(0, n - i - 1):
            if nizObjekata[j].rang > nizObjekata[j + 1].rang:
                nizObjekata[j], nizObjekata[j + 1] = nizObjekata[j + 1], nizObjekata[j]





def paginacijaStranica(nizObjekata, N):
    p = Paginator(nizObjekata, N)
    currentPage = p.page(1)
    while True:
        l = 1
        print("************************")
        for file in currentPage.object_list:
            print(l, ") ", file.link)
            print(l, ") ", file.rang)
            l+=1
        print ("************************")
        pr = False
        if currentPage.has_previous():
            pr = True
            print("Prev", end=" ")
        start = 1
        end = p.num_pages
        if p.num_pages > 10:
            end = 10
            if currentPage.number > 6 :
                start = currentPage.number - 5
                end = currentPage.number + 4
                if end > p.num_pages:
                    start = start - (end - p.num_pages)
                    end = p.num_pages       #sada treba prikazati vise stranica pre ove, posto ima mesta
        for page in range(start, end+1):
            if page == currentPage.number:
                CRED = '\033[91m'
                CEND = '\033[0m'
                print(CRED + str(page) + CEND, end=" ")
            else:
                print(page, end=" ")
        n = False
        if currentPage.has_next():      #zeza kod poslenje stranice, pogledati sta je frka
            n = True
            print("Next")
        print('')
        print("Izaberite neki od brojeva da prikazete naredne stranice na tom broju ")

        print("Stisnite 0 za izlaz")


        option = input("Izaberite broj: ")

        if option == "0":
            break
        if pr == True:
            if option == "Brojevi":
                currentPage = p.page(currentPage.previous_page_number())
        for i in range(1, p.num_pages+1):
            if option == str(i):
                currentPage = p.page(i)
                break
        if n == True:
            if option == "Dalje":
                currentPage = p.page(currentPage.next_page_number())

        if option == "N":
            numFiles = input("Unesite novi broj fajlova po stranici: ")
            p = Paginator(nizObjekata, numFiles)
            currentPage = p.page(1)