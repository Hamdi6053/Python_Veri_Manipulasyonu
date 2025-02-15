#Problem 1
#Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın

a = int(input('Lütfen bir sayi giriniz:'))
b = int(input('Lütfen bir sayi giriniz:'))
c = int(input('Lütfen bir sayi giriniz:'))
carpim = a*b*c
print('Bu sayilerin carpimi: {0}'.format(carpim))

#Problem 2
#Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

#Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)

boy = float(input('Lütfen boyunuzu giriniz:'))
kilo = float(input('Lütfen Kilonuzu giriniz:'))

beden_kitle_indeksi = kilo / (boy ** 2)

print(beden_kitle_indeksi)

#Problem 3
#Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı
#bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.

yakıt_miktari = int(input('Lütfen kilometrede yakılan yakit miktarini litre cinsinden giriniz:'))
yapılan_yol = int(input('Lütfen aracın ne kadar kilometre yaptığını giriniz:'))
yakıt_fiyati = float(input('Lütfen yakıt fiyatını giriniz:'))
toplam_ödeme = yapılan_yol*yakıt_miktari
print('Toplam ödenen Ücret:',toplam_ödeme)

#Problem 4
#Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = str(input('Lütfen bir ad giriniz:'))
soyad = str(input('Lütfen bir soyad giriniz:'))
numara = int(input('Lütfen bir soyad giriniz:'))

#print('Adınız: {0}\nSoyadınız: {1}\nNumaranız: {2}\n'.format(ad,soyad,numara))
print(ad,soyad,numara, sep='\n')
#Problem 5
#Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.

a = int(input('Sayi giriniz:'))
b = int(input('Sayi giriniz:'))
liste = [a,b]
a,b = liste[1],liste[0]
print(a,b)



#Problem 6
#Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

#Hipotenüs Formülü: a^2 + b^2 = c^2

a = int(input('Sayi giriniz:'))
b = int(input('Sayi giriniz:'))
f = a**2 + b**2
print('Hipotenüs Uzunluğu:',f)