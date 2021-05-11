import json

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'

ZACETEK = 'Z'


class Vislice:
    datoteka_s_stanjem = 'stanje.json'

    def __init__(self):
        self.igre = {}
    
    def prost_id_igre(self):
        if self.igre:
            return max(self.igre) + 1 #self.igre gre direkt čez ključe
        else:
            return 0
    
    def nova_igra(self):
        igra = nova_igra()
        id = self.prost_id_igre()
        self.igre[id] = (igra, ZACETEK)
        return id

    def ugibaj(self, id_igre, crka):
        igra, stanje = self.igre[id_igre]
        stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, stanje)
    

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem, encoding='utf8') as f:
            igre = json.load(f)
        for id_igre in igre:
            geslo = igre[id_igre]['geslo']
            crke = igre[id_igre]['crke']
            stanje = igre[id_igre]['stanje']

            igra = Igra(geslo)
            igra.crke = crke

            self.igre[int(id_igre)] = (igra, stanje)

    def zapisi_igre_v_datoteko(self):
        igre = {}
        for id_igre in self.igre:
            igra, stanje = self.igre[id_igre]
            igre[id_igre] = {'geslo': igra.geslo, 'crke': igra.crke, 'stanje': stanje}
        with open(self.datoteka_s_stanjem, 'w', encoding='utf8') as f:
            json.dump(igre, f)


class Igra:

    def __init__(self, geslo):
        self.geslo = geslo
        self.crke = []
    

    def napacne_crke(self):
        return [c for c in self.crke if c.upper() not in self.geslo.upper()]

    def pravilne_crke(self):
        return [c for c in self.crke if c.upper() in self.geslo.upper()]

    
    def stevilo_napak(self):
        return len(self.napacne_crke()) #če kličemo metodo mormo povedat na čem je uporabljena
    

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def zmaga(self):
        return not self.poraz() and len(self.pravilne_crke()) == len(set(self.geslo))
    #tle je še neki naredu..

    def pravilni_del_gesla(self):
        pravilno = ''
        for crka in self.geslo.upper():
            if crka in self.crke:
                pravilno += crka
            else:
                pravilno += '_'
        return pravilno
    
    # return ''.join([c if c in self.crke else '_' for c in self.geslo.upper()])

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())
    
    
    def ugibaj(self, crka):
        crka = crka.upper()

        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo.upper():
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA



with open("besede.txt", encoding='utf-8') as f:
    bazen_besed = f.read().split()

#read vrne niz tega vsega, split pa razdeli po vseh 'praznih prostorih', ki se nahajajo..

import random 

def nova_igra():
    geslo = random.choice(bazen_besed)
    return Igra(geslo)

