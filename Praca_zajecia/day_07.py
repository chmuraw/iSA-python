# # MODULY

# najpierw importuje modul. w tym przypadku - plik python ktory stworzylam myModule


# wybieram z zaimportowanego modulu funkcje, ktora potrzebuje:
# trzeba pamietac o konstrukcji - najpierw from potem import (z ktorego modulu sciagam ktoras funkcje)

# Rozne sposoby wywoalywania funkcji z modulu:
# myModule.hello()
# hello()

# Przyklad na konflikt nazw: chociaz importuje funkcje to w tym programie moge ja zmieniac.
# def hello():
#     print("Dzien dobry")
# myModule.hello()
# hello()

# zeby temu zaradzic importuje funkcje z modulu ze zmieniona nazwa. Dzieki temu nie zaryzykuje zmiany w module:
# from myModule import hello as helloFromModule
# def hello():
#     print("Dzien dobry")
# myModule.hello()
# hello()
# helloFromModule()


# # drugi przyklad z modulem:

# # Teraz stwarzam nowy folder typu python packages - tu trzymam moduly zeby program latwo je znajdowal.
# Importuje to na samej gorze kodu - zeby od razu wchodzac do programu wiadomo bylo jakie moduly trzeba zaimportowac.
# importujac wskazuje sciezke do modulu, bo nie jest w folderze co plik day07

# from Praca_zajecia.modules.otherModule import add
#
# # w module funkcja zdefinowana tak, zeby wyrzucac sume dynamicznych argumentow.
# # Do nowej zmiennej przypisuje swoje argumenty do funkcji add:
# result = add(1, 2, 45, 12)
# # wyrzucam wynik zmiennej
# print(result)


# # ZADANKO: utworzyc plik na dysku i przerzucic od razu do kosza
# 1. tworze plik
# 2. przenosze go do kosza
# 3. otwieram gre saper (w linuxie saper = gnome-mines)


# prawdopodobnie na windowskie nie bedzie dzialac modul os -trzeba wowczas po bozemu stworzyc plik open("file.txt", "w")
# # kiepawo na zajeciach dziala mi sent2trash - sprawdz te funkcjonalnosc w domu
# import os
# import send2trash
# import shutil
#
# # jak sobie poradzic z tym, ze plik juz zostal utworzony wczesniej:
# try:
#     os.mknod("newfileToDelete.txt")
# except FileExistsError:
#     print("Plik juz istnieje")

# # w windowsie trzeba tradycyjnie: open("file.txt")
# send2trash.send2trash("newfileToDelete.txt")
# os.system("gnome-mines")

# # ===================================================


# # WYSYLANIE WIADOMOSCI E-MAIL

# idea maila okolo 1965 (w zakresie jednego komputera)
# protokol SMTP simple mail transfer protocole 1971 - pierwsze maile do innych

# sprawy potrzebne do wyslania maila:
# login: isapy@int.pl
# haslo: isapython;
# serwer: poczta.int.pl
# uwierzytelnienie SSL

# scenariusz zdarzen:
# 1. importuje biblioteki
# 2. mam temat wiadomosci i tresc wiadomosci
# 3. tworze mailera
# 4. witam sie z serwerem smtp - tworze polaczenie
# 5. wlaczam szyfrowanie
# 6. loguje sie
# 7. wysylam maila
# 8. koncze polaczenie z serwerem

# biblioteka ktora laczy sie z sererem i wysyla maila:
import smtplib

# modul, ktory jest do edytowania maila
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase  # moduł do wysyłania załączników
# from email import Encoders # ten takze potrzebny do zalacznika

subject = input("Prosze podac temat: ")
body = input("Prosze podac tekst wiadomosci: ")
recipient = input("Prosze podac adresata: ")

# tresc maila podajemy w parametrze
mail_body = MIMEText(body)
mail_attachement = MIME
# przygotowuje niezbedne naglowki:
mail = MIMEMultipart()  #utworzenie takie jakby wydmuszki, nizej dodaje niezbedne elementy maila
mail["Subject"] = subject
mail["From"] = "isapy@int.pl"  # mozna tez tak: "Prezyden Polski <isapy@int.pl>"
mail["To"] = recipient

# dolaczam body do maila:
mail.attach(mail_body)

# !!!!!! skopiowane z neta, przeedytuj, zeby wiadomosc mail zawierala zalacznik!!!!!!!

part = MIMEBase("application", "octet-stream")
part.set_payload(open("zalacznik.txt", "rb").read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="zalacznik.txt"')
msg.attach(part)

#przygotowuje serwer
server = smtplib.SMTP("poczta.int.pl")
server.starttls()
server.login("isapy@int.pl", "isapython;")
server.send_message(mail)
server.quit()