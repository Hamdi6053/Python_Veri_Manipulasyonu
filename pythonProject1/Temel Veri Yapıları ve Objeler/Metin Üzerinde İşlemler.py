with open('metin.txt','w',encoding='utf-8') as file:
    file.write('Yazılım dünyası sonsuz olasılıklarla dolu bir evren! Kod satırlarıyla hayaller gerçeğe dönüşüyor, karmaşık sorunlar çözüme kavuşuyor. Her gün yeni bir dil, framework veya araç öğrenmek mümkün. Yaratıcılığın ve sürekli gelişimin ön planda olduğu bu dünya, geleceği şekillendirmeye devam ediyor.')


with open('metin.txt','r',encoding='utf-8') as file:
    print(file.read())


class dosya():
    def __init__(self, sade_kelimeler):
        with open('metin.txt', 'r', encoding='utf-8') as file:
            dosya_içeriği = file.read()
            kelimeler = dosya_içeriği.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip('\n')
                i = i.strip(' ')
                i = i.strip('.')
                self.sade_kelimeler.append(i)

    def tüm_kelimeler(self):
        kelimeler_kümesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kümesi.add(i)
        print('Tüm kelimeler......')
        for i in kelimeler_kümesi:
            print(i)
            print('************************')

    def kelime_frekansı(self):
        kelime_sözlük = dict()
        for i in self.sade_kelimeler:
            if (i in kelime_sözlük):
                kelime_sözlük[i] += 1
            else:
                kelime_sözlük[i] = 1
        for kelime, sayı in kelime_sözlük.items():
            print('{} kelimesi {} defa geçiyor......'.format(kelime, sayı))
            print('*****************************************************')


dosya = dosya(None)
print(dosya.tüm_kelimeler())
print(dosya.kelime_frekansı())






