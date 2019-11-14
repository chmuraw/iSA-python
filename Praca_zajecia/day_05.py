# Dzien 5 CIEZKIE ZAJECIA
# Sowniki
# Slownik tworzy sie otwierajac nawias klamrowy.
# names, surnames i city to klucze i im przypisane sa wartosci.


# # deklaruje slownik:
# contacts = {"names": ["Ala", "Ola", "Jan"], "surnames": ["Kowalski", "Malinowska", "Igrekowski"],
#             "cities": ["Warszawa", "Gdansk", "Krakow"]}


# print(type(contacts))  # sprawdzenie jaki jest to typ (czy na pewno sllownik)

# print(contacts["cities"]) # wyrzuci wszystko co jest w kluczu cities

# print(contacts["country"]) # wyrzuci blad ze nie ma takiego klucza

# contacts["cities"].append("Rumia") # appent dodaje element
# print(contacts["cities"])

# contacts.update({"countries": ["Polska", "Niemcy", "Czechy", "Polska"]})  #uaktualnienie
# print(contacts)
# update mozna zapisac tez tak:
# contacts["countries"] = ["Polska", "Niemcy", "Czechy", "Polska"]
# print(contacts)
#
# print(len(contacts))  # sprawdzi ilosc kluczy!!!!


# print(contacts.keys())   # wyrzuci nazwy wszystkich kluczy w slowniku

# print(contacts.items())  # slownik, ktory zawiera krotki z wszystkimi wartosciami kolejnych kluczy

# print(list(contacts))  # zadziala tu jak contacts.keys() - domyslnie zwroci kllucze


# Zadanie: Wydrukuj zdanie "Ala Kowalska mieszka w Warszawie (Polska)"
#                           "Ola Malinowska mieszka w Gdansk"
#                           "Jan Igrekowski mieszka w Krakow'
## przypisuje kolejnyych wartosci z kolejnych kluczy
# print(contacts)
# # enumerate zwraca pare wartosci: indeks wartosci i wartosc przypisana do tego indeksu
# for key, value in enumerate(contacts["names"]):
#     # print(key)
#     # print(value)
#     name = value
#     surname = contacts["surnames"][key]
#     cities = contacts["cities"][key]
#     countries = contacts["countries"][key]
#     print(f"{name} {surname} mieszka w {cities} ({countries})")
# ## Dzialaj malymi kroczkami! najpierw printuje key i values a potem dzialam wykorzystujac key, jako indeksowanie elementow



# # ============================================================================
# Jeszcze raz to samo, tylko inny uklad danych

# contacts = {
#     "0": {"name": "Ala", "surname": "Kowalska", "cities": "Gdansk"},
#     "1": {"name": "Ola", "surname": "Malinowska", "cities": "Warszawa"},
#     "2": {"name": "Jan", "surname": "Igrekowski", "cities": "Krakow"}
# }
#
# print(contacts)
#
# ## key jest wierszem a value kolumna
# for key, value in enumerate(contacts):
#     # print(key)
#     # print(value)
#
#     name = contacts[str(key)]["name"]
#     surname = contacts[str(key)]["surname"]
#     city = contacts[str(key)]["cities"]
#
#     # print(imie)
#     print(f"{name} {surname} mieszka w {city}")

## ====================================================================================


## Jeszcze raz to samo, ale tym razem dane zapisane w liscie:

# contacts = [
#     {"name": "Ala", "surname": "Kowalska", "cities": "Gdansk"},
#     {"name": "Ola", "surname": "Malinowska", "cities": "Warszawa"},
#     {"name": "Jan", "surname": "Igrekowski", "cities": "Krakow"}
# ]
#
# for rows in contacts:
#     # print(rows["name"])
#     name = rows["name"]
#     surname = rows["surname"]
#     cities = rows["cities"]
#
#     print(f"{name} {surname} mieszka w {cities}")

# # ====================================================================================

# # OPERACJE NA PLIKACH  - MYSL O WIRTUALNYM KURSORZE

## tworze plik tekstowy - zeby to sie udalo, musze wpisac tryb 'w'
# file = open("Pierwszy_plik.txt", "w")
# file.write("zapisz prosze do pliku jeszcze raz")
# file.close()


## jesli otwieram plik z uwzyciem with nie musze juz pamietac zeby zamknac na koncu swoj plik tekstowy
# with open("file.txt", "w") as file:
#     file.write("zapisz prosze \n")
#     file.write("i jeszcze ra \n")
#     file.write("i jeszcze jeden i jeszcze raz \n")
# z kazdym kolejnym dopisaniem przesuwa sie kursor

#    print(file.tell())  ## pokazuje w ktorym miejscu pliku tekstowego znajduje sie kursor

# to samo co wyzej, ale file.seek ustawie kursor w wybrane miejsce
# with open("file.txt", "w") as file:
#     file.write("zapisz prosze \n")
#     file.seek(5)   ## przez to nadpisze czesc tekstu, pozostawi reszte, ktora wystaje
#     file.write("i jeszcze ra \n")
#     file.write("i jeszcze jeden i jeszcze raz \n")
#
#     print(file.read())     #chces przeczytac tekst, ale w trybie "w" jest tylko zapisywanie

# # to samo co wyzej, ale jeszcze odczytujemy:
# with open("file.txt", "w+") as file:
#     file.write("zapisz prosze \n")
#     file.seek(5)   ## przez to nadpisze czesc tekstu, pozostawi reszte, ktora wystaje
#     file.write("i jeszcze ra \n")
#     file.write("i jeszcze jeden i jeszcze raz \n")
#     file.seek(0)
#     print(file.read())     # najpierw ustawiam seek na 0, zeby kursor byl na poczatku pliku. samo czytanie tekstu rowniez przesuwa kursor.


## Zadanie: Program jak sie uruchomi to ma krzyknac ile razy sie uruchomil

file = open("licznik.txt", "r+")
file.write("Plik otwarty {n} razy")
file.close()

print(file.read())

