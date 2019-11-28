import book.tools as tools
import pickle
from datetime import datetime

class Ksiega():
    # najpierw definiuje konstruktor. potem, jesli cos nowego pojawi sie w metodzie, to tez tu musze dodac
    def __init__(self):
        self.nazwa = "Ksiega gosci"
        self.plik = "book.pkl"
        self.wpisy = []
        self.odczyt()


# definiuje metode:
    def dodaj_wpis(self, wpis):
        self.wpisy.append(wpis)
        self.zapisz()

    def zapisz(self):
        with open(self.plik, "rb+") as plik_ksiegi:
            plik_ksiegi.seek(0)
            pickle.dump(self.wpisy, plik_ksiegi)

    def odczyt(self):
        # sprawdzam czy jest plik book.pkl. jesli nie, to go tworze, jesli tak, to go otwieram.
        try:
            plik_ksiegi = open(self.plik, "rb+")
            self.wpisy = pickle.load(plik_ksiegi)
        except:
            plik_ksiegi = open(self.plik, "wb+")
            self.wpisy = []

        plik_ksiegi.seek(0)
        plik_ksiegi.close()

    def __len__(self):
        return len(self.wpisy)

class Wpis():
    def __init__(self, autor, tytul, tresc, data = None):
        self.autor = autor
        self.tytul = tytul
        self.tresc = tresc
        if data is None:
            self.data = tools.dzis()
        else:
            self.data = data
