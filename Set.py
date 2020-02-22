class Set:


    def __init__(self):
        self.noviRecnik = {}


    def pretragaAND(self,prviRecnik, drugiRecnik):  # presek
        '''
        Funkcija koja vraca recnik koji je presek prosledjenih.
        Vrednosti se sabiraju.

        Args:
            prviRecnik(dict): Recnik za prvu rec
            drugiRecnik(dict): Recnik za drugu rec
        Return:
             recnikNovi
        '''

        recnikNovi={}
        for putanja1, value in prviRecnik.items():
            for putanja2, value2 in drugiRecnik.items():
                if putanja1 == putanja2:
                    recnikNovi[putanja1] = value + value2

        return recnikNovi


    def pretragaOR(self,prviRecnik, drugiRecnik):  # unija
        '''
        Funkcija koja vraca recnik koji predsatvlja uniju
        dva prosledjena recnika.

        fajlovima koji se poklapaju se sabiraju vrednosti(prioriteti),
        a ostali, koji se ne poklapaju se samo dodaju u recnik.

        Args:
            prviRecnik(dict): prvi recnik
            drugiRecnik(dict): drugi recnik

        Return:
            Novi recnik
        '''

        recnikNovi={}

        # prvo ubacujem one iz unije
        for putanja1, value in prviRecnik.items():
            for putanja2, value2 in drugiRecnik.items():
                if putanja1 == putanja2:
                    recnikNovi[putanja1] = value + value2

        # zatim ubacujemo one koji su u prvoj a nisu u drugoj
        for putanja1, value in prviRecnik.items():
            if putanja1 not in drugiRecnik:
                recnikNovi[putanja1] = value

        # zatim ubacujemo one koji su u drugoj a nisu u prvoj
        for putanja2, value in drugiRecnik.items():
            if putanja2 not in prviRecnik:
                recnikNovi[putanja2] = value

        return recnikNovi

    def pretragaNOT(self,prviRecnik, drugiRecnik):
        '''
        Funkcija koja vraca recnik u kojem se nalaze fajlovi
        koji se ne nalaze u drugom recniku.

        Args:
            prviRecnik(dict): Recnik u kojem se nalaze fajlovi za prvu rec
            drugiRecnik(dict): Recnik u kojem se nalaze fajlovi za drugu rec

        Return:
            Recnik
        '''

        recnikNovi={}

        for putanja1, value in prviRecnik.items():
            if putanja1 not in drugiRecnik:
                recnikNovi[putanja1] = value

        return recnikNovi