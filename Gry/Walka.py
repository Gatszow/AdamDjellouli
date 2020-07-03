import random
from time import sleep

class Wojownik():
    def __init__(self, imie="Charles", zycie = 0, pAtaku = 0, pObrony = 0):
        self.imie = imie
        self.zycie = zycie
        self.pAtaku = pAtaku
        self.pObrony = pObrony

    def atak(self):
        return random.randint(0, self.pAtaku)*(random.randint(2,5))

    def obrona(self):
        return random.randint(0, self.pObrony)

    def straconeZycie(self, ilosc):
        if ilosc > 0:
            self.zycie -= ilosc
            if self.zycie <= 0:
                print(self.imie, " poległ w walce :(")
        else:
            print(self.imie, "uniknął ciosu")

    def czyZywy(self):
        if self.zycie <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.imie

def walka(malpa, rycerz):

    i = 1

    while (malpa.czyZywy() and rycerz.czyZywy()):
        print('Runda nr: ', i)
        wyswietlStaty(malpa, rycerz)

        if random.randint(0,1) == 0:
            pojedynek(malpa, rycerz)

        else:
            pojedynek(rycerz, malpa)

        print('')
        i += 1
        sleep(5)

    if rycerz.czyZywy():
        print('Wygrana rycerza!!!')
    else:
        print("Wygrana małpiego wojownika!!!")


def pojedynek(x,y):
    print(x, 'został zaatakowany przez', y)
    obrazenia = y.atak() - x.obrona()
    if obrazenia > 0:
        print(x, 'stracił', obrazenia, 'punktów życia')
    else:
        print(x, "nie stracił punktów życia")
    x.straconeZycie(obrazenia)

def wyswietlStaty(x,y):
    for i in (x,y):
        print(i, "ma", i.zycie, "punktów życia")

rycerz = Wojownik("Rycerz", random.randint(100, 1000), random.randint(10, 50), random.randint(5, 20))

malpa = Wojownik("Małpi Wojownik", random.randint(100, 1000), random.randint(10, 50), random.randint(5, 20))

walka(malpa, rycerz)