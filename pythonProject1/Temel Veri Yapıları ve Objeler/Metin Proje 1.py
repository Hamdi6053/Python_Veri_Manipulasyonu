'''Problem 1
Elinizde uzunca bir string olsun.

            "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"


Bu string içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.'''

liste = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"

class Kelime():
    def __init__(self):
        print('Kelime sınıfının init fonksiyonu.')

    def Sayma(self):
        kelime_sozluk = dict()
        for i in liste:
            if (i in  kelime_sozluk):
                kelime_sozluk[i] +=1

            else:
               kelime_sozluk[i] = 1
        for kelime,sayı in kelime_sozluk.items():
            print('{} kelimesi {} defa geçiyor......'.format(kelime, sayı))
            print('*****************************************************')

kelime= Kelime()

print(kelime.Sayma())


