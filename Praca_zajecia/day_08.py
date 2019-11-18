# # Debuggowanie
# # trenujemy korzystanie z debuggera, break pointa


# # Prosty programik okreslajacy ktory dzien tygodnia to weekend
# days = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
# weekend = ("sobota", "niedziela")
# for day in days:
# #    print(day)  # pierwszy sposob na debuggowanie
# # inny sposob to odpalenie zielonego robaczka w prawym gornym
#     if day in weekend:
#         print("It's weekend!")
#     else:
#         print("You need to go to work")


# # obsluga plikow
# from PIL import Image
# image : Image.Image = Image.open('kot.jpeg')
# jesli tu blad sciezki, to sprawdz dokladnie gdzie jest ten plik.
# jak jest w tym samym folderze co plik py, to nie trzeba wpisywac sciezki.

# image.show()
## ctr + najechanie na funkcje wyswietla dokumentacje! to bardzo cenne

# zmiana rozmiaru i inne modyfikacje obrazu wymaga zapisanie nowej wersji:
# image = image.resize((5000, 1000))
# image.save("kot64.jpeg")

# image = image.rotate(90)
# image.save("kot_rotate.jpeg")


# # ogarnianie roznych rzeczy z neta
## cos tu kurde nie dziala -  chyba mam zly api_key - sprawdz w domu!!
# import requests
#
# wp_page = requests.get("https://wp.pl")
# print(wp_page)
# api_key = "800101cc05e0bcd5b88c816246c988ff"
# api_host = "https://openweathermap.org/data/2.5/weather"
# city = "Gdansk"
# result = requests.get(f"{api_host}?appid={api_key}&q={city}")
# dict = result.json()
# print(result)
#
# dict = result.json()
# print(f"temperatura: {dict['main']['temp']}")
# print(f"wind: {dict['wind']['speed']} m/s")
#
# pass



# # parsowanie - wyszukiwanie rzeczy w jakims zrodle - sprawdz definicje
## parser - wyszukuje kontent stron internetowych
# # sciaganie obrazkow


# from bs4 import BeautifulSoup
# import requests
#
# page = requests.get('https://wallpaperlist.com/')
# parser = BeautifulSoup(page.content, "html.parser")
#
# images = parser.find_all('img')
# for image in images:
#     print(image['src'])


# # 1. Sciagnij wszystkie obrazki ze strony glownej wallpaperlist.com do katalogu images
# # 2. zrob miniaturki obrazkow w katalogu images/thumbs o szerokosci 64px (wysokosc proporcjonalnie)
# # 3. Policz ile jest zdjec na stronie
# # 4. Wyslij maila z informacja ile zdjec sciagnieto, jaki jest sumaryczny rozmiar zdjec w MB i ile miejsca zaoszczedzilam robiac miniaturki
# # 5. Dopisz w mailu jaka jest pogoda w gdansku.

# # 1
from PIL import Image
# from bs4 import BeautifulSoup
# import requests
# import os
#
#
# # tworze katalog do zapisania pobranych pozniej zdjec
# # fol = os.mkdir('images')
#
# #
# page = requests.get('https://wallpaperlist.com/')
# parser = BeautifulSoup(page.content, "html.parser")
#
# pictures = parser.find_all('img')
# for image in pictures:
#     image.show()

# https://www.geeksforgeeks.org/working-images-python/ tu szukaj rozwiazan!!!

from urllib import urlopen
from PIL import Image
import cStringIO

imgdata = urlopen('https://wallpaperlist.com/').read()
img = Image.open(cStringIO.StringIO(imgdata))
img.save("pic1" + ".png")



## rozwiazanie z stackoverload
import re
import requests
from bs4 import BeautifulSoup

site = 'http://pixabay.com'

response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]


for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    with open(filename.group(1), 'wb') as f:
        if 'http' not in url:
            # sometimes an image source can be relative
            # if it is provide the base url which also happens
            # to be the site variable atm.
            url = '{}{}'.format(site, url)
        response = requests.get(url)
        f.write(response.content)

        ## do przerobienia!!!
        https: // stackoverflow.com / questions / 18408307 / how - to - extract - and -download - all - images -
        from

        -a - website - using - beautifulsoup