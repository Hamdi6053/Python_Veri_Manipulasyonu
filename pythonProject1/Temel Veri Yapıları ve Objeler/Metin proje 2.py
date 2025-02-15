'''
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.

                    Memlekete sis çökmüş bir gece
                    Usulca yanağıma sen düşüyorsun
                    Sabah saat dokuzu beş geçe
                    Terk edip bizleri gidiyorsun
                    Ayrılık bu kadar yakmamıştı içimizi
                    Farkında mısın bilmiyorum
                    Aldın beraberinde cumhuriyetimizi
                    Korkunç bir veda, sararmıştı her yer
                    Ellerini uzat tutmak istiyoruz
                    Masmavi gözleri kaybetmiş çocuk
                    Aldı bir sabah ruhumuzu
                    Lakin nasıl bölmesin yokluğun uykumuzu

Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.'''
from sys import exc_info

with open('şiir.txt', 'w', encoding='utf-8') as file:
    file.write( 'Memlekete sis çökmüş bir gece\n')

with open('şiir.txt','a',encoding='utf-8') as file:
    file.write('Usulca yanağıma sen düşüyorsun\n')
    file.write('Sabah saat dokuzu beş geçe\n')
    file.write('Terk edip bizleri gidiyorsun\n')
    file.write('Ayrılık bu kadar yakmamıştı içimizi\n')
    file.write('Farkında mısın bilmiyorum\n')
    file.write('Aldın beraberinde cumhuriyetimizi\n')
    file.write('Korkunç bir veda, sararmıştı her yer\n')
    file.write('Ellerini uzat tutmak istiyoruz\n')
    file.write('Masmavi gözleri kaybetmiş çocuk\n')
    file.write('Aldı bir sabah ruhumuzu\n')
    file.write('Lakin nasıl bölmesin yokluğun uykumuzu\n')




class dosya():
    def __init__(self):
        print('Dosya sınıfının init fonksiyonu')

    def dosya_okuma(self):
        with open('şiir.txt', 'r', encoding='utf-8') as file:
            dosya_içerik = file.read()
            print(dosya_içerik)


    def satır_bölme(self):
        with open('şiir.txt', 'r', encoding='utf-8') as file:
            satırlar = file.readlines()
            ilk_karakterler = []
            for satır in satırlar:
               ilk_karakterler.append(satır[0])
            birleşik_karakterler = ''.join(ilk_karakterler)

            print(birleşik_karakterler)


dosya = dosya()
print(dosya.dosya_okuma())
print(dosya.satır_bölme())
