# # # Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)
# def konwersja_temperatury():

# def konwersja(skala = None, temperatura = None):
#     if skala == "C" or skala == "c":
#         return "F", (temperatura * 9/5) + 32.0
#         print("F = (C * 9/5) + 32")
#     elif skala == "F" or skala == "f":
#         return "C", (temperatura - 32) * 5/9
#     else:
#         print("Skala musi byc F lub C!")
#
# skala = input("Proszę wybrac skalę (F) lub (C): ")
# temperatura = float(input("Proszę podac temperaturę: "))
#
# # Przypisanie zmiennych wprowadzonych przez użytkownika
# a, b = konwersja(skala, temperatura)
# # Wyświetlenie odpowiedniego wzoru
# if skala == "C" or skala == "c":
#     print("F = (C * 9/5) + 32")
# else:
#     print("C = (F - 32) * 5/9")
# # Podanie ostatecznego wyniku konwersji
# print(temperatura, "stopni", skala, "to", round(b, 2), "stopni", a)

## ======================================================================

## Zadanie 2. Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
#def pierwsza_ostatnia():
def pierwsza_cyfra(n):
        # Dzielę przez 10 az zostanie tylko pierwsza cyfra
    while n >= 10:
        n = n/10
    return int(n)
def ostatnia_cyfra(n):
        # Szukam reszty z dzielenia przez 10
    return (n % 10)
n = int(input("Prosze podac liczbe: "))
print("Pierwsza cyfra:", pierwsza_cyfra(n), ", Ostatnia cyfra:", ostatnia_cyfra(n))


