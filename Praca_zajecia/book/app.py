from flask import Flask
from flask import render_template
from flask import request, redirect, url_for  # mozna po przecinku dodawac kolejne klasy importowane z tegoo modulu
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
    if request.method == 'POST':
        autor = request.form['autor']
        tresc = request.form['tresc']
        tytul = request.form['tytul']

        ksiega = Ksiega()
        wpis = Wpis(autor, tytul, tresc)
        ksiega.dodaj_wpis(wpis)
        ilosc_wpisow = len(ksiega)
        print(len(ksiega))

    # return redirect(url_for("lista_wpisow")) ## to po dodaniu wpisu przeniesie uzytkownika na podana strone insternetowa

    return render_template('dodaj.html')
@app.route("/lista_wpisow")
def lista_wpisow():
    ksiega = Ksiega()
    wpisy = ksiega.wpisy[::-1]
    return render_template("lista.html", wpisy_html = wpisy)


app.run(debug=True)   # to za kazdym razem wpisywalam w terminalu, zeby strona na biezaco sie odswiezala. teraz juz nei trzeba