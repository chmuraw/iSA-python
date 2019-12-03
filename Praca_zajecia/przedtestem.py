# system binarny = dwojkowy (zera i jedynki)

# algorytm skonczony zestaw polecen potrzebnych do wykonania zadania

# zlozonosc algorytmiczna (obliczeniowa) - poziom skomplikowania algorytmu
# (im mniejsza tym lepiej - jak najmniej opercaji, jak najmniej petli itd)

# input() - metoda do pobrania czegos od uzytkownika

# print() - metoda wyswietlania czegos uzytkownikowi w konsoli

# zmienna - nazwany obszar pamieci

# deklarowanie zmiennej (pojedynczy znak rownosci)
# dom = "bialy"

# typy danych w pythonie: int, str, float, bool, tuple, dict, list, set(ale o tym nie mowilismy)

# tworzenie listy:
# litery = ["A", "B", "C", "D", "E"]
# litery = list("ABCDE")
# print(litery)
# ITEROWALNY - mozna go rozlozyc na czesci. str jest iterowalny

# wyraz = "wyraz"
# for litera in wyraz:
#     print(litera, end =" ") # wyswietli wszystkie litery w jednej linii
#     print(litera) #wyswietli litery jedna pod druga

# slownik z imineiem i nazwiskiem (wszystko w klamrach i klucze w cudzyslowiach)
# osoba = {"imie": "Jan", "nazwisko" : "Kowalski", "wiek": 18}
# print("Kowalski"[2:6:1])  # wals !!! jedynka na koncu dla sciemy, bo i tak jest domyslna

# print("Kowalski"[1:1:1] # nic nie wyjdzie.

# z czego sklada sie funkcji: minimalistycznie - potrzebna jest tylko nazwa ;)
# def nazwa():
#     pass
# # poza nazwa moze miec parametry domyslne lub niedomyslne - pozycyjne (kolejnosc definiowania jest wazna)
# def nazwa(arg1, arg2, arg3 = "war3", *args, **kwargs): #arg3 - parametr nazwany, args i kwargs moga miec jakies nazwy
#     # jedna gwiazdka oznacza nieskonczona ilosc pozycyjnych argumentow, a ** nieskonczona ilosc key walues - przechodzi w slownik
#
# # no i zmienna musi miec jakies cialo:
#     zmienna = 1
#     inna_zmienna = 2
#     return "ala ma kota"
#     # jak funkcja nie ma returna to zwraca None

# def funkcja(*args):
#     print(args)
# funkcja(1, 3, 6, 7, 8.2,"ala ma kota", "grudzien")  # dzieki args moge te wszystkie rozne elementy miec w swojej funkcji
# funkcja("2019")


# def funkcjakwargs(**kwargs):
#     print(kwargs)
# funkcjakwargs(param = "grudzien", arg = 2)  # dzieki args moge te wszystkie rozne elementy miec w swojej funkcji
# funkcjakwargs(rok = "2019")
# mozna mieszac args i kwargs, alle w definiowaniu najpierw args potem kwargs


# mutowalny - mozna zmieniac, niemutlowany - nie mozna zmieniac

# robimy cos pod warunkiem: najmniejsyz mozliwy if sklada sie z warunku :)

#else jest tylko jeden, a elifow moze byc nieskonczenie wiele
# zmienna = "2"
# if zmienna == "1":
# elif zmienna == "2":
# elif zmienna =="3":
# else:
#     pass

# operatory w ifach:
# >, <, => itd
# in - czy jeden element jest w innym elemencie
# is - do sprawdzenia typu, albo true or false
# not - zaprzeczenie

# print(False and True and not False) = print(False and True and True)
# and z jakakolwiek false da wynik false (tablica prawdy)


# otwieranie plikow: open("nazwa/sciezka", "tryb")
# w - jezeli plik istnieje, to zostanie wyczyszczony i zapisuje nowe, ewentualnie tworzy nowy plik jesli nie istnieje i zapisuje
# wb - to samo, w trybie binarnym (zipy, obrazki, pikle)
# r - odczyt. nie zapisuje, nie utworzy pliku jesli go nie ma.
# r+ - odczyta i zapisze. nie utworzy pliku jesli go nie ma.
# a - ??? - do sprawdzenia w domu

# modul w pythonie - wyodrebniona czesc kodu do osobnego skryptu/pliku


# importowanie modulow zewnetrznych:
#import modul - importuje caly modul
#from modul import klasa - importuje tylko czesc modulu
# from modul import klasa as inna_nazwa - zaimportuje i bede uzywac pod inna nazwa
# from katalog.podkatalog.modul import klasa as moja_nazwa

# paradygmaty: enkapsulacja, polimorfizm, abstrakcja, dziedziczenie
# dziedziczenie: tworzenie obiektu od ogolo do szczegolu. obiekt podrzedny przejmuje cechy wspolne nadrzednego (jesli nie deklaruje sie inaczej)
# class Pies(zwierze) - klasa pies dziedziczy po zwierze

# abstrakcja: zdefioniowany poziom szczegolowosci obiektow jesli chodzi o ich wlasciwosci i metody.

# polimorfizm: definiowanie wspolnych metod dla roznefgo typu obiektow. (__xxx__)

# enkapsulacja(hermetyzacja): definiowanie metod do dostepu do wlasciwosci obiektu
# getter, setter, deletter na przyklad.

# w pythonie wystepuja metody pseudoprywatne: ustawia sie to tak: self.__nazwa
# self.__nazwa - wlasciwosc
# def __nazwa(): pass - metoda

# klasa vs obiekt - klasa to plan budowy domu a obiekt to ten dom
# klasa to zdefiniowany plan/schemat, a obiekt to "namacalny byt" stworzony na podstawie tego planu.

# wyjatek - nazwane bledy programu, ktore mozna "przeskoczyc"
# try:
#     dzielenie = 9/0
# except ZeroDivisionError:
#     print("Blad")
# else:
#     print("Gdy nie ma wyjatku")
# finally:
#     print("Zawsze")

# # jak zdefiniowac metode klasy: (cls!!!)
# def Klasa():
#     @classmethod
#     def metodaklasy(cls):
#         pass
#
# # jak zdefiniowac klase obiektu:
#     def metodaobiektu(self):
#         pass
#
# #metoda statyczna (niepowiazana ani z obiektem ani z klasa)
#     @staticmethod
#     def metodastatyczna():
#         pass

# # konstruktor klasy:
#     def __init(self):
#         self.cecha = 1
#         self.inna_cecha = "bialy"

# getter:
#     @property
#     def cecha():
#         return self.__cecha
#
#     # setter: zeby moc setter i deletter musi najpierw byc getter
#     @cecha.setter
#     def cecha(self, nowa_wartosc):
#         self.__cecha = nowa_wartosc
#
#     @cecha.deleter
#     def cecha(self):
#         self,__cecha = None
#
# dziedziczenie:
# class A():
#     def f(self):
#         print("A")
# class B(A):
#     def f(self):
#         print("B")
# class C(A):
#     def f(self):
#         print("C")
# class D(A):
#     pass
#
# A().f() #wyswietli A
# B().f() # wyswietli B (bo napisalismy)
# C().f() # wyswietli C
# D().f() # wyswietli A