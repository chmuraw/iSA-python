## Listy referencyjne

# lista = [1, 2, 3]
# nowa_lista = lista    ## zmianiamy wartosc tylko na podstawowej liscie, ale przez to ze sa referencyjne, to w nowa lista wartosc rowniez bedzie zmieniona (uzywaja tego samego adresu w pamieci)
#
# kopia_listy = lista.copy() ## wyrzuci pierwsza wartosc bez zmian (oryginalna liste)
#
# lista[0] = 'x'
# print(lista)
# print(nowa_lista)
# print(kopia_listy)

# import copy    #importuje, zeby moc uzyc glebokiego kopiowania (to nie jest wbudowana funkcja)
#
#
# lista = [1,
#          2,
#          3,
#          ['A', 'B', 'C']
#          ]
#
# nowa_lista = lista
# kopia_listy = lista.copy() # wezmie bez zmian pierwsza czesc listy, ale zmieni w zagniezdzeniu - troche misz masz w pamieci
# gleboka_kopia_listy = copy.deepcopy(lista)
# lista[0] = 'x'
# lista[3][0] = 'y'     #zamieni A (zagniezdzone listy - szuka pozycji zero z trzeciego elementu, czyli z tej zagniezdzonej)
#
# print(lista)
# print(nowa_lista) # to dziala referencyjnie w kazdym przypadku - zawsze odnoscik do glownej listy
# print(kopia_listy)  # pierwszy poziom jest kopiowany bez zmian, a druga czesc jest zmieniona
# print(gleboka_kopia_listy) # skopiowana "doglebnie" cokolwiek zrobie z pierwotna lista. nie wprowadzi zadnych zmian ani w pierwszej liscie ani w zagniezdzonej

## !!!! Referencja powoduje ze mamy zapisany adres do pamieci, a nie kopiujemy samych wartosci !!!!
# jezeli pracujemy na jakichs danych, ktorych zrodla nie mozemy zmieniac, to korzystamy z kopii albo glebokich kopii. dla pewnosci, zeby nie modyfikowac bez potrzeby i zeby nie przechowywac w pamieci duzej ilosci danych



##=================================================================

## FUNKCJE!

# #definiuje funkcje, ktora ma drukowac komunikat.
# def witaj():
#     print('Czesc, jestem twoim nowym programem.')
# hi = witaj   # tutaj przypisuje funkcje do zmiennej. potem moge wywolac ja wywolujac zmienna.
# #wywolanie funkcji
# #witaj()
# hi()

## jezeli napisalabym tak: hi = witaj()  <--- to juz w tym momencie interpreter bedzie chcial wywolac funkcje. wiec przypisze wynik funkcji.
## print(hi) - ciekawe, bo wyswietli po prostu adres funkcji. nie wyswietli przypisanej wartosci





## zdefioniowane argumenty funkcji

# def do_nothing(x, y, imie="Ola", wiek=22):
#     pass  #uzywam tego, zeby interpreter przeszedl dalej, kiedy wiem ze funkcja bedzie uzywana dalej.
   # print("Not implemented yet")   # zamiennie do pass

#do_nothing(1)   #trzeba podac drugi argument!
#do_nothing(1,2, "Iza") #bez problemu
#do_nothing(1,2, imie = "Iza", 22) #nie zadziala bo trzeba by bylo nazwac tez argument wiek
#do_nothing(1, 2, imie = Iza", wiek=14) #tu rozkmin bo cos sie nie zgadza
#do_nothing(1,2, wiek=22, imie = "Iza") # tu dziala bez problemu

# dobra zasada jest wprowadzanie argumentow zgodnie z kolejnoscia z definiowania funkcji.

## ================================================================

## RETURN   #funkcja zwraca sprawy na zewnatrz. bez returna wszystko co sie dzieje w funkcji - zostaje w funkcji



## imie pozostanie bez zmian, bo funkcja dziala w swoim obrebie (do czasu uzycia return)
# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
# print(imie)
# zmien_imie()
# print(imie)

# #dopiero jak uzyje return i przypisze funkcje do zmiennej to zmieni to imie na teresa
# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
#     return imie
# print(imie)
# imie = zmien_imie()
# print(imie)


# imie = "Jola"
# def zmien_imie():
#     imie = "Teresa"
#     return [imie]    #mozna sobie zwrocic liste jak w tym przypadku, ale tez krotke i w sumie cokolwiek
# print(imie)
# imie = zmien_imie()
# print(imie)


##
# def zmien_imie(imie):
#     imie = "Teresa"
#     if imie == "Teresa":
#         return "To twoje imie"
#     else:
#         return "To nie jest twoje imie"
#
# imie = zmien_imie("Teresa")
# print(imie)



## Przyklady z zadania domowego

## Zadanie 10

dane = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

# czytamy tegor stringa co 4 znaki - mamy tu 24 odczyty. sprawdzamy 24 razy tego stringa zeby po kolei wyciagnac temperatury
##Recznie wyciagalabym to tak:
   #  temp = dane[0:4] #0
   #  temp = dane[4:8] #1
   #  temp = dane[8:12] #2
   #  temp = dane[12:16] #3


for godzina in range(0, 24):  #co prawda liczy od zera, ale przedzial niedomkniety wiec 24 a nie 23
    poczatek_zakresu = godzina * 4
    koniec_zakresu = poczatek_zakresu + 4
    temp = int(dane[poczatek_zakresu:koniec_zakresu]) / 100
    if temp <= 20:
        tab = "\t!"
    elif temp <= 18.5:
        tab = "\t!!"
    else:
        tab = ""   #mozna to zrobic dwojako: albo elsem na koncu, albo z gory zdefiniowac jeszcze przed ifem  tab=""

    wiersz_string = f"{godzina}:00:\t {temp}\u00b0C{tab}"   #pod u00b0 siedzi w unicode znaczek stopni
    print(wiersz_string)

## w domu trzeba jeszcze dac po dwa znaki przy godzinie i po dwa znaki po przecinku dla temperatur


