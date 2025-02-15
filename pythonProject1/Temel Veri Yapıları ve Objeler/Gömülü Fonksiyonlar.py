'''Problem 1
Elinizde bir dikdörtgenin kenarlarını ifade eden sayı çiftlerinin bulunduğu bir liste olsun.

         [(3,4),(10,3),(5,6),(1,9)]

Şimdi kenar uzunluklarına göre dikdörtgenin alanını hesaplayan bir fonksiyon yazın ve bu listenin her bir elemanına bu fonksiyonu uygulayarak ekrana şöyle bir liste yazdırın.

         [12, 30, 30, 9]
'''

print(list(map(lambda x: x[0]*x[1], [(3,4),(10,3),(5,6),(1,9)])))


'''Problem 2
Elinizde şöyle bir liste bulunsun.

    [1,2,3,4,5,6,7,8,9,10]

Bu listenin içindeki çift sayıların toplamını ekrana yazdıran bir fonksiyon yazın.

*Not: İlk önce filter() fonksiyonu ile çift sayıları ayıklayın. Daha sonra reduce() fonksiyonunu kullanın.*'''

from functools import reduce
print(reduce(lambda x ,y : x+y ,list(filter(lambda x: x % 2 == 0,[1,2,3,4,5,6,7,8,9,10]))))

'''Problem 3
Elinizde isimlerin ve soyisimlerin bulunduğu iki tane liste olsun.

        isimler -----> ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

        soyisimler -----> ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

Bu isimleri ve soyisimleri sırasıyla eşleştirin ve ekrana alt alta isimleri ve soyisimleri yazdırın.'''

isimler =  ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
liste = list(zip(isimler,soyisimler))
for isim,soyisim in liste:
    print('{0} {1}'.format(isim,soyisim))

'''Problem 4
    Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

         [(3,4,5),(6,8,10),(3,10,7)]

    Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

         [(3, 4, 5), (6, 8, 10)]

*** Not: filter() fonksiyonunu kullanmaya çalışın. ***'''

print(list(filter(lambda x: x[0]**2+x[1]**2==x[2]**2, [(3,4,5),(6,8,10),(3,10,7)])))