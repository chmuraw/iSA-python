# coding=utf-8
# Zadanie 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie
# (wyswietlajac wzor i kolejne obliczenia)

def konwersja_temperatury():

    def konwersja(skala = None, temperatura = None):
        if skala == "C" or skala == "c":
            return "F", (temperatura * 9/5) + 32.0
            print("F = (C * 9/5) + 32")
        elif skala == "F" or skala == "f":
            return "C", (temperatura - 32) * 5/9
        else:
            print("Skala musi byc F lub C!")

    skala = input("Prosze wybrac skale (F) lub (C): ")
    temperatura = float(input("Prosze podac temperature: "))

# Przypisanie zmiennych wprowadzonych przez uzytkownika
    a, b = konwersja(skala, temperatura)
# Wyswietlenie odpowiedniego wzoru
    if skala == "C" or skala == "c":
        print("F = (C * 9/5) + 32")
    else:
        print("C = (F - 32) * 5/9")
# Podanie ostatecznego wyniku konwersji
    print(temperatura, "stopni", skala, "to", round(b, 2), "stopni", a)

# ======================================================================

# Zadanie 2. Napisz program, ktory poda pierwsza i ostatnia cyfre podanej liczby
def pierwsza_ostatnia():

    def pierwsza_cyfra(n):
        # Dzieli przez 10 az zostanie tylko pierwsza cyfra
        while n >= 10:
            n = n / 10
        return int(n)
    def ostatnia_cyfra(n):
        # Szuka reszty z dzielenia przez 10
        return (n % 10)
    n = int(input("Prosze podac liczbe: "))
    print("Pierwsza cyfra:", pierwsza_cyfra(n), ", Ostatnia cyfra:", ostatnia_cyfra(n))

# # ======================================================================

# Zadanie 3. Napisz program, ktory rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość)
# za pomocą znaków | (bok) - (góra/dół) + (wierzchołek)
def prostokat():
    wysokosc = int(input("Prosze podac wysokosc prostokata: "))
    szerokosc = int(input("Prosze podac szerokosc prostokata: "))

    # Sprawdzenie poprawnosci wprowadzonych danych
    if wysokosc <= 0 or szerokosc <= 0:
        print("Prosze podac wartosci wieksze od 0")
    # Wydrukowanie pierwszego rzedu
    else:
        print("+" + szerokosc * " -" + "+")

    for i in range(0, wysokosc):
        print("|" + szerokosc*"  " + "|")
    print("+" + szerokosc * " -" + "+")

# # ======================================================================

# Zadanie 4.  Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
def binarna_dziesietna():
    liczba_binarna = input("Prosze podac liczbe binarna: ")
    liczba_dziesietna = int(liczba_binarna, 2)
    print(liczba_dziesietna)

# # ======================================================================

# # Zadanie 5. Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

def rok_przestepny():
# Rok jest przestepny jesli jest podzielny przez 4, nie podzielny przez 100, ale podzielny przez 400
    rok = int(input("Podaj rok do sprawdzenia: "))
    if(rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0):
        print("To jest rok przestepny")
    else:
        print("To nie jest rok przestepny")

# # ======================================================================

# # Zadanie 8. Program rysujący piramidę o określonej wysokości
# # chyba zadziala w python3
# def rysuj_piramide():
#     def piramida(wysokosc):
#           for i in range (0, wysokosc):
#             for j in range(0, wysokosc - i):
#                 print(end = ' ')
#             for j in range(0, (i * 2)-1):
#                 print("#", end = " ")
#             print()
#     wysokosc = int(input("Prosze podac wysokosc piramidy: "))
#     piramida(wysokosc)

# # Poprzednia wersja
# wysokosc = int(input("Prosze podac wysokosc piramidy: "))
# for i in range (0, wysokosc):
#     for j in range(0, wysokosc - i):
#         print(end=" ")
#     for j in range(0, (i * 2)-1):
#         print("#", end=" ")
#     print()

# # ======================================================================

#  Zadanie 9
#  Kalkulator wieku psa
def wiek_psa():
    lata = int(input("Prosze podac wiek psa w latach ludzkich: "))
    if lata < 0:
        print("Pies ma 0 lat w psich latach")
        exit()
    # dwa pierwsze lata *10.5
    elif lata <= 2:
        wiek_psa = lata * 10.5
    else:
        wiek_psa = 21 + (lata - 2) * 4
    print("Pies ma {0} lat w psich latach".format(wiek_psa))

# # ======================================================================
# Zadanie 10
# Lista temeratur wg godzin

def odczyt_temp():
# Ponizszy ciag danych podzielic co 4 znaki i przypisac kolejnym godzinom
    dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

    for godzina in range(0, 24):
        poczatek_zakresu = godzina * 4
        koniec_zakresu = poczatek_zakresu + 4
        temp = int(dane[poczatek_zakresu:koniec_zakresu]) / 100
        if temp <= 20:
            tab = "\t!"
        elif temp <= 18.5:
            tab = "\t!!"
        else:
            tab = ""

        wiersz_string = f"{godzina}:00:\t {temp}\u00b0C{tab}"
        # pod u00b0 to w unicode znaczek stopni
        print(wiersz_string)

    ## w domu trzeba jeszcze dac po dwa znaki przy godzinie i po dwa znaki po przecinku dla temperatur


wybor = True
while wybor:
    print("""
    1. Przeliczanie tempertatury w skali Celsjusza na Fahrenheita i odwrotnie.
    2. Wybor pierwszej i ostatniej cyfry zadanej liczby.
    3. Narysowanie prostokata o zadanych parametrach.
    4. Przeliczenie liczby binarnej na dziestietna.
    5. Sprawdzenie czy rok jest przestepny.
    8. Narysowanie piramidy o zadanej wysokosi.
    9. Kalkulator psich lat. 
    10. Odczyt tempreatur wg godziny.
    11. Wyjscie.
    """)
    wybor = raw_input("Ktory program chcesz uruchomic? ")
    if wybor == "1":
        konwersja_temperatury()
    elif wybor == "2":
        pierwsza_ostatnia()
    elif wybor == "3":
        prostokat()
    elif wybor == "4":
        binarna_dziesietna()
    elif wybor == "5":
        rok_przestepny()
    #elif wybor == "8":
        #rysuj_piramide()
    elif wybor == "9":
        wiek_psa()
    elif wybor == "10":
        odczyt_temp()
    elif wybor == "11":
        print("Do widzenia")
    else:
        print("Prosze wybrac inny wariant.")