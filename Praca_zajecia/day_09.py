# OBIEKTOWOSC

# definiuje klase
class Krzeslo():
# oraz konstruktor:
# tego init nigdy jawnie nie wykonujemy.
    def __init__(self, kolor_siedziska="czerwony"):
        # print("Tworze obiekt")  # nie za bardzo robi sie printy tak w srodku definiowania. tutaj tylko przykladowo!
        # ustawiam domyslne cechy obiektu:
        # wszystkie cechy sa takie same u wszystkich krzesel.
        # to co je wyroznia to kolor siedziska (przez to ze w definicji zapisany za self)

        self.kolor_siedziska = kolor_siedziska   #tutaj zostawiam przestrzen do deklarowania koloru - nie ma domyslnego
        self.ilosc_kol = 5
        self.wysokosc = "90 cm"
        self.szerokosc = "40 cm"
        self.glebokosc = "40 cm"
        self.regulacja_wysokosci = True # ma albo nie ma
        self.regulacja_podlokietnikow = False
        self.material = "100% cotton"

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
    def __str__(self):
        return f"Krzeslo koloru: {self.kolor_siedziska}"
obiekt = Krzeslo()
print(obiekt)
print(obiekt.kolor_siedziska)

# zdefiniowana metoda __str__ ma doste do selfa i wyciaga wlasciwosci obiektow.