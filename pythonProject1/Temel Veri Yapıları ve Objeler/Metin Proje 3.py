'''Elinizde "mailler.txt" adında , maillerin ve bazı yazıların bulunduğu bir dosya olsun. Bu dosyanın her bir satırını okuyun ve sadece mail formatına uygun olanları ekrana yazdırın.

                    coskun.m.murat@gmail.com
                    example@xyz.com
                    mustafa.com
                    mustafa@gmail
                    kerim@yahoo.com

                           //
                           //
                           //


*İpucu: Stringlerde bulunan endswith ve find metodlarını kullanabilirsiniz.'''

with open('mailler.txt','w',encoding='utf-8') as file:
    file.write('coskun.m.murat@gmail.com\n')


with open('mailler.txt','a',encoding='utf-8') as file:
    file.write('example@xyz.com\n')
    file.write('mustafa.com\n')
    file.write('mustafa@gmail\n')
    file.write('kerim@yahoo.com\n')
    file.write('Ahmet Ali Veli')

with open('mailler.txt','r',encoding='utf-8') as file:
    print(file.read())

with open('mailler.txt','r',encoding='utf-8') as file:
    satırlar= file.readlines()
    for satır in satırlar:
        if satır.endswith('.com\n') and '@' in satır:
            print(satır.strip())




