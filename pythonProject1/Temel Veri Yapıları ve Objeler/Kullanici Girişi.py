
print('****************Kullanici Girişi*******************')
sys_Kullanıcı_Adı = 'Murat'
sys_parola='12345'

kullanici_adi = input('Lütfen kullanici adini giriniz:')
parola = input('Lütfen parolanızı giriniz:')

if (kullanici_adi == sys_Kullanıcı_Adı and sys_parola!=parola):
    print('Parola Yanlış.')
elif (kullanici_adi != sys_Kullanıcı_Adı and sys_parola!=parola):
    print('Yanlış kullanici adi.')
elif (kullanici_adi != sys_Kullanıcı_Adı and sys_parola!=parola):
    print('Yanlış Kullanici Adi ve Parola.')
else:
    print('Hoşgeldiniz doğru kullanici adi ve parola.')