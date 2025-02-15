import random
import time
print(
'''
******************

Sayı Tahmin Oyunu Programına Hoşgeldiniz.
1 ile 40 arasında sayıyı tahmin edin.
Lütfen çıkış işlemi için q ' ya basınız.
******************
''')

rastgele_sayı = random.randint(1,40)
tahmin_hakkı = 7

while True:
    tahmin = (input('Tahmininiz:'))

    if tahmin == 'q':
        print('Oyundan çıkıldı.')
        break
    tahmin = int(tahmin)

    if (tahmin<rastgele_sayı):
        print('Bilgiler Sorgulanıyor...')
        time.sleep(1)
        print('Daha yüksek bir sayı söyleyin.')
        tahmin_hakkı -= 1

    elif (rastgele_sayı<tahmin):
        print('Bilgiler Sorgulanıyor...')
        time.sleep(1)
        print('Daha düşük bir sayı söyleyin.')
        tahmin_hakkı -= 1

    else:
        print('Bilgiler Sorgulanıyor...')
        time.sleep(1)
        print('Tebrikler! Sayımız',rastgele_sayı)
        break

    if (tahmin_hakkı==0):
        print('Tahmin hakkınız bitmiştir.')
        print('Tebrikler! Sayımız', rastgele_sayı)
