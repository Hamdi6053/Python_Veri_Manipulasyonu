
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

url = "https://www.doviz.com/"
while True:
    response = requests.get(url)
    html_icerik = response.content
    soup = BeautifulSoup(html_icerik, "html.parser")
    altın_fiyat = soup.find("span", {"data-socket-key": "gram-altin", "data-socket-attr": "s"})
    doların_fiyatı = soup.find("span", {"data-socket-key": "USD", "data-socket-attr": "s"})
    euronun_fiyatı = soup.find("span", {"data-socket-key": "EUR", "data-socket-attr": "s"})


    if altın_fiyat:
        print("Gram altının fiyat:{}".format(altın_fiyat.text.strip()))
        time.sleep(10)

    if doların_fiyatı:
        print("Doların fiyatı:{}".format(doların_fiyatı.text.strip()))
        time.sleep(10)

    if euronun_fiyatı:
        print("eouronun fiyatı:{}".format(euronun_fiyatı.text.strip()))
        time.sleep(10)

    else:
        print("Hata")
