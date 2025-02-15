import os
from datetime import datetime
#print(dir(os))

# os kütüphanesi dosyada işlemlerde kullanılır.
# dosyanın hangi dizinde olduğunu öğrenebilmek için getcwd kullanılır.

#print(os.getcwd()) #direkt dosyanın içinde bu işlemi yapıyoruz.

#os.chdir('C:/Users/user/Desktop') dizini değiştirmede kullanılır.

#print(os.listdir()) # Bulunduğu kalsördeki dosyaları getirir listeler.

#Bulunduğum dizinde klasör açmak içinde mkdir kullanılrı

#os.mkdir('Deneme1')
#eğer ki içi içe oluşturulmak istenirse örneğin deneme2 nin altında deneme3
#os.makedirs('Deneme2/Deneme3')

#klasör silmede rmdir kullanılır

#os.rmdir('Deneme2/Deneme3') # removedirs dosyaların altındkai her şeyi siler.

#os.rename('Test.txt','Test2.txt')
#dosya ismini değiştirme

print(os.stat('OS Modülü.py'))
print(os.stat('OS Modülü.py').st_mtime)
print(datetime.fromtimestamp(os.stat('OS Modülü.py').st_mtime))

#Tüm klasör ve dosyalara bakmak için ekrana yazdırmak için for ile birlikte walk fonksiyonu kullanılır.

for i in os.walk('C:/Users/hamdi/OneDrive/Masaüstü'):
    print(i)

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk('C:/Users/hamdi/OneDrive/Masaüstü'):
    print('Klasor Yolu:',klasor_yolu)
    print('Klasor İsimleri:',klasor_isimleri)
    print('Dosya İsimleri:',dosya_isimleri)

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk('C:/Users/hamdi/OneDrive/Masaüstü'):
    for i in dosya_isimleri:
        print(i)

for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk('C:/Users/hamdi/OneDrive/Masaüstü'):
    for i in dosya_isimleri:
        if i.endswith('.txt'):
            print(i)