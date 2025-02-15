print('''***********
     
    
    
Kullanıcı Girişi Programı
      
      
*************''')

sys_Kullanici_adi = 'Hamdi'
sys_parola = '12345'
giriş_hakkı = 3

while True:
    Kullanici_adi = input('Lütfen kullanici adi giriniz:')
    Kullanici_parola = str(input('Lütfen parolanızı giriniz:'))
    if (sys_Kullanici_adi != Kullanici_adi) and (sys_parola == Kullanici_parola):
        print('Kullanici Adı Hatalı.....')
        giriş_hakkı -= 1

    elif (sys_Kullanici_adi == Kullanici_adi) and (sys_parola != Kullanici_parola):
        print('Parola Hatalı.....')
        giriş_hakkı -= 1

    elif (sys_Kullanici_adi != Kullanici_adi) and (sys_parola != Kullanici_parola):
        print('Parola ve Kullanici Adi Hatalı.....')
        giriş_hakkı -= 1
    else:
        print('Sisteme başarıyla giriş yaptınız:')
        break
    if (giriş_hakkı == 0):
        print('Girişiz Hakkınız Bitti.....')

