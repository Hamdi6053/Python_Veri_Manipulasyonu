'''boy = float(input('Lütfen boyunuzu giriniz:'))
kilo = float(input('Lütfen kilonuzu giriniz:'))
BKİ = kilo / (boy ** 2)

if  BKİ < 18.5 :
    print('Zayıf')
elif 18.5 <= BKİ < 25:
    print('Normal')
elif 25 <= BKİ < 30:
    print('Fazla Kilolu')
else:
    print('Obez')'''

'''a = int(input('Lütfen bir sayi giriniz:'))
b = int(input('Lütfen bir sayi giriniz:'))
c = int(input('Lütfen bir sayi giriniz:'))

if (a >= b) and (a >= c):
    print(a)
elif (b >= a) and (b >= c):
    print(b)
elif (c >= a) and (c >= b):
    print(c)
else:
    print('Hatalı Giriş')'''

Vize1 = int(input('Lütfen vize notunuzu giriniz:'))
Vize2 = int(input('Lütfen vize notunuzu giriniz:'))
final = int(input('Lütfen final notunuzu giriniz:'))

ToplamNot = Vize1 * 0.3 + Vize2 * 0.3 + final * 0.4

if ToplamNot >= 90:
    print('AA')
elif 85<=ToplamNot<90:
    print('BA')
elif 80<=ToplamNot<85:
    print('BB')
elif 75<=ToplamNot<80:
    print('CB')
elif 70<=ToplamNot<75:
    print('CC')
elif 65<=ToplamNot<70:
    print('DC')
elif 60<=ToplamNot<65:
    print('DD')
elif 55<=ToplamNot<60:
    print('FD')
else:
    print('FF')

'''soru = input('Üçgen mi Dörtgen mi?')

if soru == 'Dörtgen':
    a = int(input('Kenar Giriniz:'))
    b = int(input('Kenar Giriniz:'))
    c = int(input('Kenar Giriniz:'))
    d = int(input('Kenar Giriniz:'))

    if a == b == c == d:
        print('Kare.')
    else (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
        print('Diktörtgen.')

else soru == 'Ücgen'
    if '''