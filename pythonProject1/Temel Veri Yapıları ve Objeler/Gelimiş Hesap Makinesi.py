import math as mth


print(
'''
Gelişmiş Hesap Makineye Hoşgeldiniz.

İşlemler:

1.Kosinüs değerleri('Radyan Cinsinden')
2.Sinüs değerleri('Radyan Cinsinden')
3.Tanjant değerleri('Radyan Cinsinden')
4.Küp kök dönderme
5.Tavan değer dönderme 
6.Taban değer dönderme
7.Gamma fonksiyonu
8.10 tabanına göre logaritma
9.Öklid Mesafesi
10.Karekök alma
11.Faktöriyel Hesabı  
12.X in Y kuvvetini alma 
Lütfen çıkmak için 'q' ya basınız.

''')

işlemler = input('Lütfen bir işlem giriniz:')

if işlemler == '1':
    x = int(input('X:'))
    y = mth.acosh(x)
    print(y)

elif işlemler == '2':
    x = int(input('X:'))
    y = mth.asin(x)
    print(y)

elif işlemler == '3':
    x = int(input('X:'))
    y = mth.atan(x)
    print(y)

elif işlemler== '4':
    x = int(input('X:'))
    y = mth.cbrt(x)
    print(y)

elif işlemler == '5':
    x = float(input('X:'))
    y = mth.ceil(x)
    print(y)

elif işlemler == '6':
    x = float(input('X:'))
    y = mth.floor(x)
    print(y)

elif işlemler == '7':
    x = int(input('X:'))
    y = mth.gamma(x)
    print(y)

elif işlemler == '8':
    x = int(input('X:'))
    y = mth.log10(x)
    print(y)

elif işlemler == '9':
    # İki boyutlu noktalar için örnek
    x1 = float(input("İlk noktanın x koordinatını girin: "))
    y1 = float(input("İlk noktanın y koordinatını girin: "))
    x2 = float(input("İkinci noktanın x koordinatını girin: "))
    y2 = float(input("İkinci noktanın y koordinatını girin: "))

    p = [x1, y1]
    q = [x2, y2]
    mesafe = mth.dist(p, q)
    print(f"İki nokta arasındaki mesafe: {mesafe}")

elif işlemler == '10':
    x = int(input('X:'))
    y = mth.sqrt(x)
    print(y)

elif işlemler == '11':
    x = int(input('X:'))
    y = mth.factorial(x)
    print(y)

elif işlemler == '12':
    x = int(input('X:'))
    y = int(input('y:'))
    b = mth.pow(x,y)
    print(b)

else:
    print('Hatalı giriş:')




