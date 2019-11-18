# Napisz program, który:
#
# 1. Sciagnie wszystkie obrazki ze strony glownej wallpaperlist.com do katalogu images
# 2. Zrobi miniaturki obrazkow w katalogu images/thumbs o szerokosc 64px (wysokosc prop.)
# 3. Policzy ile jesc zdjęć na stronie
# 4. Wysle maila z inforamcją ile zdjęć sciągnięto, jaki jest sumaryczny rozmiar zdjęć w MB
#    + informację ile MB zaoszczędziłem robiąc miniaturki
#    + informację jaka jest pogoda w Gdansku :)
#
# Postaraj się napisać program jak najbardziej optymalnie, czytelnie i prosto
# oraz maksymalnie zabezpieczony przed błędnymi danymi.
# Pamietaj o debuggowaniu, refaktoringu, tworzeniu funkcji i modułów w oddzielnych plikach.

#
# pip3 install beautifulsoup4
#
# sudo apt install python3-pip
import os

from bs4 import BeautifulSoup
import pip
# # tworze katalog do zapisania pobranych pozniej zdjec
# fol = os.mkdir("obrazy")
#
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import re
site = 'https://wallpaperlist.com/'
page = requests.get('https://wallpaperlist.com/')
parser = BeautifulSoup(page.content, "html.parser")
img_tags = parser.find_all('img')
urls = [img['src'] for img in img_tags]
# print(urls)

for url in urls:
    fileName = f"{site}{url}"
    # print(fileName)
    fileFormat = fileName[-3:]
    # print(fileFormat)
# # WHYYYY permission is denied?
    with open("obrazy", 'wb'):
        if fileFormat == "jpg":
            img_tags.save(f"{fileName}")
## ehhhh pomieszanie z poplataniem
    # else:
    #     print("it's not jpg")

    # with open(filename.group(1), 'wb') as pictures:
    #     response = requests.get(url)
    #     pictures.write(response.content)
    #
#
# for image in images:
#      print(image['src'])
# from PIL import Image
# from bs4 import BeautifulSoup
# import requests
# import os
# #
# #
# # tworze katalog do zapisania pobranych pozniej zdjec
# # fol = os.mkdir('images')
#

#
#
# # for picture in pictures:
# #     filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
# #     with open(filename.group(1), 'wb') as f:
# #         if 'http' not in url:
# #             # sometimes an image source can be relative
# #             # if it is provide the base url which also happens
# #             # to be the site variable atm.
# #             url = '{}{}'.format(site, url)
# #         response = requests.get(url)
# #         f.write(response.content)
