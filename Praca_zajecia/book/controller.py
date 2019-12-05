from book.model import Wpis
from book.model import Ksiega
import book.view as View

View.menu()
opcja = input("Moj wybor: ")

if opcja == "1":
    autor = input("Prosze podac imie: ")
    tytul = input("Prosze podac tytul wpisu")
    tresc = input("Prosze podac tresc wpisu")
    data = input("Prosze podac date: ")

    wpis = Wpis(autor, tytul, tresc)
    ksiega = Ksiega()
    ksiega.dodaj_wpis(wpis)
    rozmiar = len(ksiega)
    View.pokaz_rozmiar(rozmiar)

# kontroler ma pobiera wpisy i wyswietla je (w dowolnej formie) -- do dokonczenia w domu!!!!
elif opcja == "2":
    ksiega = Ksiega()
    print(ksiega.wpisy)


else:
    View.blad()
r