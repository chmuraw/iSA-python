#wiek = input("ile masz lat? ")
#zwierzak = input("ile masz zwierzazt? ")

#wiek = 2
#zwierzak = 5
#zdanie: Ala ma 2 lata i 5 kotow

#zdanie = "ala ma " +str(wiek) + " lata i posiada" + str(zwierzak)""
#zdanie = f"Ala ma {wiek} lata i posiada {zwierzak} kotow"
#zdanie = "Ala ma {} lata i posiada {} kotow".format(wiek, zwierzak)
#zdanie = "Ala ma  {a} lata i posiada {b} kotow".format(a=wiek, b=zwierzak)




# FORMATY LICZB
# liczba = 1.234
# print("liczba: %s" % liczba)
# print("liczba: %0.10f" % liczba)  # %wartosc przed f ocznacza dokladnosc do ilosci 0 po przecinku
# print("liczba: %d" % liczba)




#INDEKSOWANIE  liczymy ZAWSZE od 0!!!!!
        #012345678901
# zdanie = "encyklopedia"
# print(zdanie[4])
# print(zdanie[-3])
# print(zdanie[2:8])   #znaki <2,8)
# print(zdanie[:7])   #od poczatku do 7 znaku <0,7)
# print(zdanie[8:])   #od 8 do konca)
# print(zdanie[::-1])   #znaki od 0 do konca, podaje od tylu - jest to najlatwierjszy sposob na odworcenie stringa
# print(zdanie[::-2])   #znaki od 0 do konca, podaje od tylu co drugi znak



# WARUNKI!

# print("Start")
#
# #if "1" == "1":     #wydrukuje start prawda koniec
# #if "1" == "2":     #wydrukuje start koniec
# #if 1 == "1":    #1int i 1str to sa inne wartosci. wydrukuje start koniec
#
# if 1 == "1":  # 1int
#
#     print("Prawda")
# else:
#     print("Bzdura")
# print("Koniec")



#JAK SPRAWDZIC CZY LICZBA JEST PARZYSTA PRZY UZYCIU -   % MODULO   -
# print("Sprawdzanie parzystosci")
# liczba = int(input("Podaj liczbe"))
#
# if liczba % 2 == 0:
#     print("liczba jest parzysta")
# else:
#     print("liczba jest nieparzysta")



#Sprawdzenie podzielnosci przez 3 i 5 - MOJE PIERWSZE NAPISANE SAMODZIELNIE!!!!!!
# liczba = int(input("Podaj liczbe"))
#
# if liczba % 3 == 0 and liczba % 5 == 0:
#
#     print("Liczba jest podzielna przez 3 i 5")
# elif liczba % 3 == 0 and liczba % 5 != 0:
#     print("Liczba jest podzielna przez 3 i nie jest podzielna przez 5")
# elif liczba % 3 != 0 and liczba % 5 == 0:
#     print("Liczba jest podzielna przez 5 i nie jest podzielna przez 3")
# elif liczba %3 != 0 and liczba % 5 != 0:
#     print("liczba nie jest podzielna przez 5 ani przez 3")



#OPERACJE NA RANGE, LISTACH I TUPLACH

#RANGE() - to nie jest funkcja, sekwencyjny, niemutowalny typ danych, zawsze to liczby calkowite
#LIST[] - to nie funkcja, mutowalny typ danych, mozna indeksowac, slice'owac
#TUPLE()

#To jest krotka(tuple), wyskoczy blad, bo nie mozna zmieniac jej elementow
# wyrazy = ("raz", "dwa", "trzy")
# wyrazy[0] = "jeden"
# print(wyrazy)

#list("dwa") to jest to samo co:
# wyraz = "dwa"
# list(wyraz)

#to jest lista dlatego moge podmienic dany element
# wyrazy = ["raz", "dwa", "trzy"]
# wyrazy[0] = "jeden"
# print(wyrazy)

# liczby_parzyste = range(0, 20, 2)   #najprostszy sposob generowania liczb parzystych
# if 10 in (liczby_parzyste):
#     print("Prawda")

# liczby_parzyste = range(0, 20, 2)
# if 40 in (liczby_parzyste):
#     print("Prawda")

# lista_liczby_parzyste = list(range(0,20,2))
# print(lista_liczby_parzyste)

# lista_liczby_parzyste = tuple(range(0,20,2))
# print(lista_liczby_parzyste)

#lista6 = list(1) #elementy list musza byc iterowalne. liczby calkowite nie sa, wyskoczy blad

# napis = "dwa"
# lista5 = list(napis)
# #print(lista5)
#
# lista5[0] = 'a'
# print(lista5) #lista jest iterowalna, wiec pierwszy znak zmieni na 'a'

# napis[0] = 'a'
# print(lista5) #

#DWA SPOSOBY ZAPISU LISTY:
#lista = list("pierwszy")
#lista = ['p', 'i', 'e', 'r', 'w', 's', 'z', 'y']
#print(lista)

#LISTA ZAKUPOW NA GRILLA
zakupy = ["cukinia", "piwko", "chipsy", "wegiel", "kubeczki"]
# print(zakupy)
# #
# # zakupy.append("talerzyki")
# # print(zakupy)
#
# zakupy.insert(0, "grill")       #insert doda wyrazenie do listy na zadane miejsce (bez podmiany elementu
# print(zakupy)
#
# zakupy[0] = "elektryczny grill"      #odwolanie do indeksu i podmiana elementu
# print(zakupy)
#
# zakupy.remove("piwko")      #usuwanie obiektu z listy (nie trzeba wiedziec na ktorej pozycji jest dany obiekt)
# print(zakupy)
#
# if "vodka" in zakupy:
#     zakupy.remove("vodka")          #sprawdzi czy obiekt jest na liscie i go usunie
# print(zakupy)
#
# del(zakupy[0])
# print(zakupy)           #usuwa zerowy obiekt listy

# zakupy.sort()       #posortuje alfabetycznie
# print(zakupy)

# lista = [[1,2,3],[4,5,6],[7,8,9]]
# lista[1][2]=9
# print(lista[1][2])    # jak w ukadzie wspolrzednych: wyrzuci z indeksu1 element 2 (liczymy od 0)



#PETLE
# print("Start")
# while False:
#     print("Jestem w petli")
# print("Koniec")

# print("Start")
# while True:
#     print("Jestem w petli")
# print("Koniec")   #bedzie dzialac w nieskonczonosc, bo PRAWDA



# print("start")
#
# zapytaj_ponownie = "T"
#
# while zapytaj_ponownie == "T":
#     zapytaj_ponownie = input("Czy moge zpaytac ponownie? [T/N]")
#     print("Odpowiedziales: " + zapytaj_ponownie)
# print("koniec")     #dopoki bedzie sie wpisywac T to bedzie wykonywac petle i ciagle zadawac pytanie ponownie, a jak sie wpisze cos innego, to skonczy petle i wydrukuje "koniec"



for przedmiot in zakupy:
    if przedmiot == 'piwko':
        znak ='[x]'
    else:
        znak = '[]'
print(znak + przedmiot)

    #print("kupic: " + przedmiot)
    #print("[] " + przedmiot)