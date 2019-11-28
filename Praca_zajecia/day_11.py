# # # DZIEN 11 - pola i metody klas, metody pseudo-prywatne (namespace), property (getter, setter, deleter)
#
# importuje sobie, zeby potem w kodzie wyciagnac dzisiejsza date:
from datetime import datetime

#
# class Pizza():
#     stawka_vat = 23
#     #pole prywatne (zeby bylo prywatne po prostu stawia sie dwa podkreslniki przed dekllarowana nazwa)"
#     __marza = 1.05
#
#     def __init__(self, skladnik_glowny):  #parametetr skladnik, zeby miec wplyw na rozroznianie obiektow
#         self.skladnik_glowny = skladnik_glowny
#         self.rozmiar = "30 cm"
#         self.ciasto = "cienkie"
#         self.cena = 100 * self.__marza # na tym poziomie moge korzystac z marzy.
#
#     #uzywam dekoratora do definiowania klasy:
#     @classmethod
#         #definiuje metode:
#     def Hawajska(cls):
#         return cls("ananas")
#     @classmethod
#     def Farmerska(cls):
#         return cls("kielbasa")
#
#     # # classmethod moze robic cokolwiek. nie musi byc zwiazana z obiektem:
#     # @classmethod
#     # def podaj_stawke_vat(cls):
#     #     return 23
#
#     # kolejny dekorator staticmethod
#     @staticmethod
#     def podaj_date():
#         return datetime.now().strftime("%Y-%d-%m")
#         #zwracanie daty w pythonie!!!
#         # wiecej roznych rzeczy do wyciagniecia z datetime:
#         # %j pobierze ktory to dzien roku, pozostale sa w dokumentacji ;)
#         # %U numer tygodnia w roku
#
#
# # hawajska = Pizza("ananas")
# # print(hawajska.skladnik_glowny)
# #
# # # albo tak: alternatywny konstruktor:
# # hawajska = Pizza.Hawajska()
# # print(hawajska.skladnik_glowny)
# #
# # # druga zdefiniowany obiekt:
# # inna_pizza = Pizza.Farmerska()
# # print(inna_pizza.skladnik_glowny)
# #
# # # # wywolanie stawki vat
# # # print(Pizza.podaj_stawke_vat)
# # # wywolanie zadeklarowanej na gorze wartosci - tak tez mozna, ale dobra praktyka jest zdefioniowanie sobie tego.
# # print(Pizza.stawka_vat)
# #
# # # wynik dekoratora staticmethod
# # print(Pizza.podaj_date())
#
# # trening prywatnosco:
# #publiczne bez problemu:
# # print(Pizza.stawka_vat)
# # # przez to ze odwoluje sie do tego poza klasa nie zadziala:
# # print(Pizza.__marza)
# # # ale juz gdy uzywam marzy zdefiniowanej w klasie, to moge jej uzywac:
# # pizza = Pizza.Farmerska()
# # print(pizza.cena)
#
#
# # # troche inne drukowanie. wyrzuci wszystkie elementy jeden pod drugim:
# # import pprint
# # # moge tak sprawdzic wszystko, co Pizza ma zdefiniowane:
# # pprint.pprint(Pizza.__dict__)
#
# # propertisy ustawiane na wlasciwosciach prywatnych:
#
# # getter - sluzy do zwracania wartosci ze zmiennej prywatnej self.__imie zamieniajac je na inne
# # (np jak nie chcemys ie czyms chwalic, i np stan magazynu nie jest wyrazony w ilosci sztuk,
# # tylko zwracany jako "duzo, malo" itp.
#
# # setter - zeby uzyc, to najpierw musi byc ustawiony getter. sluzy do zapisywamoa wartosci do zmiennej
# # - daje mozliwosc do kontrolowania tego, co zapisujemy
# # zeby poprawic blad uzytkownika, albo zeby sprawdzic poprawnosc, zeby do bazy danych poszlo wszytsko
# np w takim formacie jak chcemy
#
# # deleter - tez musi byc najpierw ustawiony getter. sluzy do usuwania zawartosci zmiennej w kontrolowany sposob.
#
#
# class Student():
#
#     def __init__(self):
#         self.__imie = None
#         self.nazwisko = None
#         self.data_dodania = None
#         self.data_usuniecia = None
#         self.skasowany = False
#
#
#     @property
#     def imie(self):
#         print("org: " + self.__imie)
#         return self.__imie.capitalize()
# # to wyzej to getter, pobieram wprowadzana wartosc i zmieniam pierwsza litere na wielka
#
# # ustawiam setter, zeby podmienil wartosc z wielka litera na poczatku zamiast pierwotnie wprowadzonej wartosci
#     @imie.setter
#     def imie(self, wartosc):
#         self.__imie = wartosc
# # po tym wszystkim w kodzie zostaje imie mala litera, ale do uzycia wyciagamy to zapisane wielka litera.
#
# # deleter:
#     @imie.deleter
#     def imie(self):
#         self.skasowany = True
#         self.data_usuniecia = self.pobierz_date()
#
#         # jak korzystam z czegos wiecej niz raz, to sobie definiuje:
#     @staticmethod
#     def pobierz_date():
#         return datetime.now().strftime("%Y - %m - %d")
#     # a dzieki temu, ze jest wewnatrz klasy, to moge z tego korzystac nawet wyzej (nad definicja).
#
# student = Student()
# student.imie = "lukasz"
# student.nazwisko = "falkowicz"
# student.data_dodania = datetime.now().strftime("%Y - %m - %d")
#
# print(student.imie)
# print(student.nazwisko)
# print(student.data_dodania)
#
# # del(student.imie) jak to puszcze, to student ustawi sie skasowany = true i pobierze sie data usuniecia
# print(student.data_usuniecia)
# print(student.skasowany)



# # poczatek zadania domowego z poprzednich zajec: KSIEGA GOSCI(pocztaek z dnia 6)
import pickle

entries = [
    {"title": "Pierwszy wpis", "body": "Tesc pierwszego wpisu", "author": "Lukasz", "date": "2019-11-07"},
    {"title": "Drugi wpis", "body": "Tesc pierwszego wpisu", "author": "Lukasz", "date": "2019-11-07"}
]

# program pyta użytkoniwka o tytul, tresc i imie
# dodaje wpis do ksiazki
# wyswietla informacje ile wpisow znajduje sie w ksiazce

# 1 program pyta użytkoniwka o tytul, tresc i imie
title = input("Podaj tytuł: ")
body = input("Podaj treść: ")
author = input("Podaj autora: ")
date = datetime.now().strftime("%Y-%m-%d")

# 2 tworzy słownik
new_entry = {"title": title, "body": body, "author": author, "date": date}
print(new_entry)

# 3 otwieranie pliku i odczytujemy stare wpisy
with open('book.pkl', 'wb+') as book_file: # lista to typ binarny, więc musimy dać 'wb' albo 'rb+'
    # pickle.dump(new_entry, book_file)  # dump to zapisz - trzeba to zrobić na poczatku żeby plik nie był pusty
    old_entries = pickle.load(book_file)
    print(old_entries)
    # 4 dodanie nowego wpisu
    try:
        old_entries.append(new_entry)
    except:
        old_entries = []
    print(old_entries)
    # 5 policz ilość wpisów
    counter = len(old_entries)
    # 6 połącz
    book_file.seek(0)
    pickle.dump(old_entries, book_file)  # dump to zapisz
    # 7 wyświetl ilość wpisów
    print(counter)
    # 8
    print("Dzięki")



