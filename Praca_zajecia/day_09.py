# OBIEKTOWOSC

# definiuje klase
# class Krzeslo():
# oraz konstruktor:
# tego init nigdy jawnie nie wykonujemy.
#     def __init__(self, kolor_siedziska="czerwony"):
#         # print("Tworze obiekt")  # nie za bardzo robi sie printy tak w srodku definiowania. tutaj tylko przykladowo!
#         # ustawiam domyslne cechy obiektu:
#         # wszystkie cechy sa takie same u wszystkich krzesel.
#         # to co je wyroznia to kolor siedziska (przez to ze w definicji zapisany za self)
#
#         self.kolor_siedziska = kolor_siedziska   #tutaj zostawiam przestrzen do deklarowania koloru -nie ma domyslnego
#         self.ilosc_kol = 5
#         self.wysokosc = "90 cm"
#         self.szerokosc = "40 cm"
#         self.glebokosc = "40 cm"
#         self.regulacja_wysokosci = True # ma albo nie ma
#         self.regulacja_podlokietnikow = False
#         self.material = "100% cotton"

    # pass
#  # python automagicznie wywoluje ta metode (wydrukuje nam powyzszego printa)
#  # powolujac obiekt klasy krzeslo uzywam wlasciwosci zdefioniowanych dla calej klasy.
# # pierwsze krzeslo
#
# # tutaj jest inny kolor siedziska niz zadeklarowany domyslnie
# obiekt = Krzeslo(kolor_siedziska="niebieski")
# # po kropeczce mam juz dostep do wlasciwosci obiektu
# print(obiekt.kolor_siedziska)
# # drugie krzeslo
# obiekt = Krzeslo()
# print(obiekt.kolor_siedziska)
# # trzecie krzeslo
# obiekt = Krzeslo()
# print(obiekt.kolor_siedziska)
#
# # to sa krzesla o takich samych wlasciwosciach, ale sa to trzy odrebne krzesla (zajmuja w pamieci trzy miejsca)


# ta metode wywoluje sie gdy nasz program poprosi graficzna reprezentacje obiektu do wyswietlenia:
#     def __str__(self):
#         return f"Krzeslo koloru: {self.kolor_siedziska}"
# obiekt = Krzeslo()
# print(obiekt)
# print(obiekt.kolor_siedziska)
#
# # zdefiniowana metoda __str__ ma doste do selfa i wyciaga wlasciwosci obiektow.


# # ==============================================================================================================
# # Zajecia 10
# # tworze obiekt do porownaniaia z krzeslem
# class Stol():
#     def __init__(self):
#         self.ilosc_nog = 4
#     def __add__(self, other):
#         return self.ilosc_nog + other.ilosc_nog
#
# class Krzeslo():
# # oraz konstruktor:
# # tego init nigdy jawnie nie wykonujemy.
#     def __init__(self, kolor_siedziska="czerwony", cena = 100):
#         # print("Tworze obiekt")  # nie za bardzo robi sie printy tak w srodku definiowania. tutaj tylko przykladowo!
#         # ustawiam domyslne cechy obiektu:
#         # wszystkie cechy sa takie same u wszystkich krzesel.
#         # to co je wyroznia to kolor siedziska (przez to ze w definicji zapisany za self)
#
#         self.kolor_siedziska = kolor_siedziska   #tutaj zostawiam przestrzen do deklarowania koloru -nie ma domyslnego
#         self.ilosc_kol = 5
#         self.ilosc_nog = 5  #dla przykladu do porownania ze stolem
#         self.wysokosc = 90
#         self.szerokosc = 40
#         self.glebokosc = 40
#         self.regulacja_wysokosci = True # ma albo nie ma
#         self.regulacja_podlokietnikow = False
#         self.material = "100% cotton"
#         self.cena = cena
#         self.vat = 23
#
#
#     def __str__(self):
#         return f"Krzeslo koloru: {self.kolor_siedziska}"
#
#     def __len__(self):
#         return self.wysokosc * self.szerokosc * self.glebokosc
#
#     def pobierz_cene_netto(self):
#         return self.cena
#
#     def pobierz_cene_brutto(self):
#         return self.cena * (1 + self.vat/100)


# # Sprawdzam sobie te definicje na stworzonych obiektach:
#
# # obiekt = Krzeslo("niebieski")
# # # print(obiekt.kolor_siedziska)
# # print(obiekt.pobierz_cene_netto())
# # print(obiekt.pobierz_cene_brutto())
# # # print(print(obiekt))
# # # print(len(obiekt))
#
# # tworze sobie kolejny obiekt
# obiekt_2 = Krzeslo("zielone", 120)
# obiekt_2.pobierz_cene_netto()
# print(obiekt_2.pobierz_cene_netto())
# print(obiekt_2.pobierz_cene_brutto())
# # mozna tez tradycyjnie, ale nalezy korzystac z metod wbudowanych (i to jest hermetyzacja!)
# # ukladamy klasy w ten sposob, ze tylko w klasie nadrzednej wprowadzamy zmiany (np. w tym przypadku jak zmieni sie vat
# # to wystarczy na gorze kodu zmienic wartosc vat, a nie we wszystkich miejscach kodu)
# # print(obiekt_2.cena * 1.23) <- lepiej skorzystac z rozwiazania powyzszych zdefioniowanych dla obiektow metod.


# # tworze sobie obiekty do porownania:
# krzeslo = Krzeslo()
# print(krzeslo)
# stol = Stol()
# print(stol)
#
# # to chcemy zrobic:
# print(stol + krzeslo)
# # zeby to zrobic zgodnie ze sztuka u gory definiujemy wszystko w kllasach. dzieki temu wyliczy ze lacznie maja 9 nog.
# # definiuje sume w klasie obiektu po lewej stronie rownania.
# # zeby dodac (krzeslo + stol) to definicja musi byc wewnatrz definicji klasy krzeslo

# # DZIEDZICZENIE
# # Trzeba pamietac, ze pierwsza stworzona klasa dziedziczy po bazowej klasie pythonowskiej (object)
# # W tym przypapdku zwierze jest nadrzedna klasa.
# # W kodzie klasa nadrzedna musi byc napisana wyzej niz podrzedna

# class Zwierze():
#    def __init__(self):
#        self.ilosc_oczu = 2
#        self.wlosy = True
#
#    def __str__(self):
#         return f"Oczy: {self.ilosc_oczu}, wlosy: {self.wlosy}"
#
# class Czlowiek(Zwierze):
#     def dajglos(self):
#         print("Heee?")
#
# class Student(Czlowiek):
#     def dajglos(self):
#         print("Siema jestem student")
#
# class Dresiarz(Czlowiek):
#     def dajglos(self):
#         super().dajglos() # wykonanie dajglos klasy nadrzednej
#         print("Masz jakis problem?")
#
# # # mozna zmienic "dziedzictwo" nadpisujac definicje:
# #     def __init__(self):
# #         self.wlosy = False
# # # ale mozna to ominac odwolujac sie do klasy wyzej poprzez funkcje super:
#     def __init__(self):
#         super().__init__()
#         self.wlosy = False
#
# class Kot(Zwierze):
#     def dajglos(self):
#         print("Miauuu")
#
# class Pies(Zwierze):
#     def dajglos(self):
#         print("Hauuu")
#
# class Bokser(Pies):
#     pass
#
# class Jamnik(Pies):
#     pass
#
# # to teraz tworze obiekty zeby posprawdzac dzialanie klas:
# #
# zwierze = Zwierze()
#
# czlowiek = Czlowiek()
# czlowiek.dajglos()
# print(czlowiek.ilosc_oczu)
#
# kot = Kot()
# kot.dajglos()
# print(kot.ilosc_oczu)
#
# pies = Pies()
# pies.dajglos()
# print(pies.ilosc_oczu)
#
# # chociaz w jamniku nie definiowalam jaki da glos, to odziedziczyl od swojej nadrzednej klasy - od psa.
# jamnik = Jamnik()
# jamnik.dajglos() # ta wlasciwosc jest dziedziczona z psa
# print(jamnik.ilosc_oczu) # ta wlasciwosc jest dziedziczona ze zwierzecia
#
# dresiarz = Dresiarz()
# dresiarz.dajglos()
# print("Nie mam")
# # print wyrzuci ilosc oczu dziedziczona od zwierzecia, ale wlosy mu trzeba zdefiniowac jego wlasne (wyzej, w def. klasy)
# print(dresiarz)


# # I TO WSZYSTKO TRZEBA SKUMAC, BO TO JEST NAJWAZNIEJSZE W TEMACIE PARADYGMATOW PROGRAMOWANIA.
# # ABSTRAKCJA TO NASZ SCHEMAT OD ZWIERZECIA DO GATUNKU, Z TAKA SZCZEGOLOWOSCIA JAK POTRZEBOWALISMY.
# # DZIEDZICZENIE - CECHY ZWIERZECIA PRZEJMUJE DRESIARZ I JAMNIK ;) POZZA TYMI, KTORE DEFINIUJE SIE KONKRETNIE DLA NICH


# # KOLEJNA KWESTIA: DZIEDZICZENIE OD WIELU RODZICOW KLASY MOGA DZIEDZICZYC PO WIELU KLASACH.
# # DZIEDZICZENIE DIAMENTOWE/PO ROMBIE/


# # CO TU SIE WYDARZA: definiuje A, b dziedziczy po A, c tez dziedziczy po A, D dziedziczy po B i C,
# # czyli najpierw szuka w B, a jak nie znajdzie to dalej szuka w C
# class A(object):
#     def hi(self):
#         print("A")
#
# class B(A):
#     pass
#
# class C(A):
#     def hi(self):
#         print("C")
#
# class D(B, C):
#     pass
#
# A().hi()
# B().hi()
# C().hi()
# D().hi()

# # A TERAZ PRZYKLAD NIECO BARDZIEJ ZYCIOWY:
;;