print(
    '''
    
    Mükemmel Sayı Bulma Programı
    
    
    Çıkmak için 'q' ya basınız.    
    '''
)

while True:
    sayi = input('Lütfen bir sayi giriniz:')
    if sayi == 'q':
        print('Program Sonlandırılıyor...')
        break
    else:
        sayi = int(sayi)
        mükemmel = 0
        for i in range(1, sayi):
            if sayi % i == 0:  # Bölenleri kontrol etmek için mod operatörü kullanılıyor
                mükemmel += i  # Bölenleri topla

        if mükemmel == sayi:  # Bölenlerin toplamı sayıya eşitse mükemmel sayıdır
            print(f"{sayi} mükemmel bir sayıdır.")
        else:
            print(f"{sayi} mükemmel bir sayı değildir.")

