from flask import Flask
from flask import render_template
from flask import request
from model import Wpis
from model import Ksiega

# # tworze aplikacje (app jest obiektem mojej aplikacji):
app = Flask(__name__)

# # bierzemy flaskowy dekorator:
@app.route("/")
def index():  # chociaz konwencja nakazuje nazwac to index()
    return render_template("index.html")

@app.route("/hello2") # mozna tu zadeklarowac wszystkie warianty wpisywania do przegladarki, zeby odpallic strone
@app.route("/hello") # tu po slashu jest to co trzeba wpisac w przegladarce zeby wyswietlic ta funkcje
def hello():
    return "Hello Kasia"

# wersja z parametrem - to co wpisze sie po slashu w adresie wyslietli sie w przegladarce po slowie Hi
@app.route("/hi/<imie>")
def hi(imie):
    return "Hi " + imie

@app.route("/dodaj_wpis", methods = ["GET", "POST"])
def dodaj_wpis():
    return render_template("dodaj.html")
    autor = request.form["autor"]
    tytul = request.form["tytul"]
    tresc = request.form["tresc"]

    ksiega = Ksiega()
    wpis = Wpis(autor, tytul, tresc)
    ksiega.dodaj_wpis(wpis)
    rozmiar = len(ksiega)
    View.pokaz_rozmiar(rozmiar)

@app.route("/lista_wpisow")
def lista_wpisow():
    return render_template("lista.html")

### ZAdanie domowe - zrobic wyswietlanie listy :D :D :D
## mozna dorobic wyszukiewarke wpisow

