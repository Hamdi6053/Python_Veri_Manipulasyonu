print(
'''*********************


Atm Makinesine hoşgeldiniz.

İşlemler;

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' ya basın.

**************************


''')

Bakiye = 1000

while True:
    işlem = input('lütfen bir işlem seçiniz:')

    if (işlem == 'q'):
        print('Yine bekleriz...')
        break
    elif (işlem == '1'):
        print('Bakiyeniz {0} tl dir.'.format(Bakiye))
    elif (işlem == '2'):
        miktar = int(input('Miktarı giriniz:'))
        Bakiye += miktar
    elif (işlem == '3'):
        miktar = int(input('Miktarı giriniz:'))

        if (Bakiye<miktar):
            print('Böyle bir miktar çekemezsiniz...')
            continue

    else:
        print('Geçersiz işlem...')






