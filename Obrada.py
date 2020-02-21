from Trie import  pretraga_stablo

import re
import os

def pretraga_rangiranje(recnik, reci, graf):

    reci2 = reci.lower()
    listaReciBezOperanada = []
    listaReci = reci2.strip().split(" ")
    pravljenjeListe_Recnika_I_Operanada(listaReci, recnik, graf, listaReciBezOperanada)
    listaRecnikaIOperanada = listaReci #[recnik1 and recnik2 or recnik3....]


def pravljenjeListe_Recnika_I_Operanada(listaReci, recnik1, graf, prosledjeneReci):#listaReci, recnik1

    brojac = 0
    for rec in listaReci:
        if rec != 'and' and rec != 'or' and rec != 'not':
            prosledjeneReci.append(rec)

            listaReci[brojac] = pretragaReci(recnik1, rec)
        brojac += 1



def pretragaReci(recnik1, rec):


    recnikReci = {}

    for key, value in recnik1.items():

        if int(pretraga_stablo(value, rec)[1]) != 0: #find_prefix(value, rec)[0] == True

            recnikReci[key] = int(pretraga_stablo(value, rec)[1])
            print("Naziv fajla: " + str(ispisNazivaFajla(key)) +" -> " + "broj pojavljivanja reci u fajlu ------->" + str( recnikReci[key]))

    return recnikReci #key: putanja,  vrednost: broj


def ispisNazivaFajla(link):

    a = link.split("\\")
    return a[-1][:-5]