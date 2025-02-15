'''Elinizde 2 tane liste bulunsun.
Bu listelerden isim ve soyisimleri birleştirerek ,
ekrana isim ve soyisimleri *isimlere*
göre sıralı bir şekilde yazdırmaya çalışın.

        isim -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisim ------> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]'''

liste =["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
liste1 = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

liste3 = list(zip(liste,liste1))
liste3.sort()
for i,j in liste3:
    print(i,j)