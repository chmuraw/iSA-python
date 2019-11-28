# # WYCIAGANIE CZASU LOKALNEGO
#
# import locale
# import datetime
#
# locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
# print(datetime.datetime.now().strftime("%A %B %H:%M:%S"))
#
# # LC znajduje nie tylko lokalny czas, moze tez np walute i inne: locale.LC_ i dalej nie podpowiada
# # Jesli nie ustawie locale to bedzie wyrzucac wszystko systemowo.


# ZADANIE Z GSIEGA GOSCI FROM SCRATCH

import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME, "pl_PL.utf8")

# definiuje 2 klasy: Ksiega i Wpis

class Ksiega():
    def __init__(self):
        self.nazwa = "Ksiega gosci"
        self.plik = "book.pkl"

# klasa wpis nie dziedziczy po zadnej innej klasie
class Wpis():
    def __init__(self, autor, tytul, tresc, data = None):
        self.autor = input("Prosze podac imie: ")
        self.tytul = input("Prosze podac tytul wpisu")
        self.tresc = input("Prosze podac tresc wpisu")
        if data is None:
            self.data = datetime.now()

