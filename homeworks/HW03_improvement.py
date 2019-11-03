## Zadanie 1 : konwersja z Cel na Fah

def konwersja(skala = None, temperatura = None):
    if skala == "C":
        return "F", (temperatura * 9/5) + 32.0
    elif skala == "F":
        return "C", (temperatura - 32) * 5/9
    else:
        print("Skala musi byc F lub C!")

skala = input("Proszę wybra skalę (F) lub (C): ")
temperatura = float(input("Proszę podac temperaturę: "))
