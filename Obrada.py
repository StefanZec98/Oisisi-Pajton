from Trie import  pretraga_stablo

import re
import os
from Set import *

def pretraga_rangiranje(recnik, reci, graf):

    s = Set()
    reci2 = reci.lower()
    listaReciBezOperanada = []
    listaReci = reci2.strip().split(" ")
    pravljenjeListe_Recnika_I_Operanada(listaReci, recnik, graf, listaReciBezOperanada)
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
            listaRecnikaIOperanada[1] = pretragaReci(recnik, listaRecnikaIOperanada[1], graf)
            recnikOR = s.pretragaOR(listaRecnikaIOperanada[0], listaRecnikaIOperanada[1])
            del listaRecnikaIOperanada[0:1]
            listaRecnikaIOperanada[0] = recnikOR


def pravljenjeListe_Recnika_I_Operanada(listaReci, recnik1, graf, prosledjeneReci):#listaReci, recnik1
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

            listaReci[brojac] = pretragaReci(recnik1, rec,graf) #od liste reci pravimo npr recnik1 and recnik 2 or recnik3...
        brojac += 1



def pretragaReci(recnik1, rec,graf):


    recnikReci = {}
    brojPojavljivanja = 0
    r=0;
    for key, value in recnik1.items():

        for k in (graf.vertList[key].connectedTo):
            try:

                brojPojavljivanja += int(pretraga_stablo(recnik1[k.id], rec)[1]) #brojPojavljivanja je broj pojavljivanja te reci u svim linkovima
            except:
                pass


        if int(pretraga_stablo(value, rec)[1]) != 0: #find_prefix(value, rec)[0] == True

            rang = pretraga_stablo(value, rec)[1] + brojPojavljivanja * 0.35 + len(graf.vertList[key].connectedTo) * 0.7
            recnikReci[key] = rang

            # ovo je pretraga ali je zakomentarisana jer smo je ukombinovali preko rangiranja
            '''     
            recnikReci[key] = int(pretraga_stablo(value, rec)[1])
            print("Naziv fajla: " + str(ispisNazivaFajla(key)) +" -> " + "broj pojavljivanja reci u fajlu ------->" + str( recnikReci[key]))
            '''
            r+=1;
            print(str(r) + ". " + "Naziv fajla: " + str(ispisNazivaFajla(key)) + " -> " + "rang ------->" + str( recnikReci[key]))

    return recnikReci #key: putanja,  vrednost: broj tj rang za tu rec na toj putanji


def ispisNazivaFajla(link):

    a = link.split("\\")
    return a[-1][:-5]