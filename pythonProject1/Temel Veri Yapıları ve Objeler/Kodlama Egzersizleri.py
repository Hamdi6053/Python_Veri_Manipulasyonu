#Oyuncu Kaydetme Programı
#print('Oyuncu Kaydetme')

ad = input('Oyuncunun Adı: ')
soyad = input('Oyuncunun Soyadı: ')
takım = input('Oyuncunun Takımı: ')

bilgiler = [ad, soyad, takım]

print('Bilgiler kaydediliyor...')

print(('Oyuncunun Adı: {0}\nOyuncunun Soyadı: {1}\nOyuncunun Takımı: {2}\n'.format(bilgiler[0], bilgiler[1], bilgiler[2]))

print('Bilgiler kaydedildi....')

#İkinci Dereceden bir bilinmeyenli denklemin köklerini bulma

a = int(input('Lütfen bir sayi giriniz:'))
b = int(input('Lütfen bir sayi giriniz:'))
c = int(input('Lütfen bir sayi giriniz:'))
Delta = (b**2)-4*a*b*c
Kok1 = (-b-Delta ** 0.5) / (2 * a)
Kok2 = (-b-Delta ** 0.5) / (2 * a)
KokBilgileri = [Kok1,Kok2]
print('Denklemin Birinci Kökü: {0}\nDenklemin İkinci Kökü: {1}\n'.format(KokBilgileri[0],KokBilgileri[1]))

