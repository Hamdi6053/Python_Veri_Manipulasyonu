import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"

while True:
    response = requests.get(url)
    html_icerik = response.content
    soup = BeautifulSoup(html_icerik, "html.parser")


    borsa_adı = soup.find_all("div",{"class":"cname"})
    borsa_fiyat = soup.find_all("td",{"class":"text-bold"})

    if borsa_adı and borsa_fiyat:
        for i, j in zip(borsa_adı, borsa_fiyat):

            print(f"Borsa adı: {i.text.strip()} ve fiyatı: {j.text.strip()}")
    else:
        print("Hata: Veriler bulunamadı.")

