toplam = 0
while True:
    sayı = input('Lütfen bir sayi giriniz:')
    if sayı == 'q':
        print('Program sonlandırılıyor...')
        break

    else:
        sayı = int(sayı)
        toplam += sayı
        print('Toplam:',toplam)
        continue


