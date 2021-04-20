STEVILO_DOVOLJENIH_NAPAK = 9

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'

ZMAGA = 'W'
PORAZ = 'X'


class Igra:

    def __init__(self, geslo, crke=[]):
        self.geslo = geslo
        self.crke = crke
    

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
    