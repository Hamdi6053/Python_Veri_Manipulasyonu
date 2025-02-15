'''Proje 2
Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa
metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.
Bu sınıfı yazarken öğrendiğimiz özel
metodların hepsini tanımlamaya çalışın'''

import time
import random


class Bilgisayar():
    def __init__(self,marka,model,işlemci,ram,depolama,pc_durum = 'Kapalı',program_listesi=['Word'],ses_seviyesi=0,program='Word'):
        print('Bilgisayar sınıfının init fonksiyonu.')
        self.marka = marka
        self.model = model
        self.işlemci = işlemci
        self.ram = ram
        self.depolama = depolama
        self.pc_durum = pc_durum
        self.program_listesi = program_listesi
        self.ses_seviyesi = ses_seviyesi
        self.program = program


    def pc_ac(self):
        if self.pc_durum == 'Kapalı':
            print('Lütfen bekleyiniz bilgisayar Açılıyorrr.')
            time.sleep(1)
            self.pc_durum = 'Açık'
        else:
            print('Bilgisayar zaten AÇIK....')

    def pc_kapat(self):
        if self.pc_durum == 'Kapalı':
            print('Bilgisayar zaten KAPALI')

        else:
            print('Lütfen bekleyiniz bilgisayar Kapanıyorrr. ')
            time.sleep(1)
            self.pc_durum = 'Kapalı'
    def durum_kontrol(self):
        if self.pc_durum == 'Açık':
            print('Bilgisayar şuan AÇIK')
        else:
            print('Bilgisayar şuan KAPALI')

    def ses_kontrol(self):
        while True:
            cevap = input('Sesi azaltmak için - ,Sesi arttırmak için +, çıkmak için (q) giriniz: ')

            if cevap == 'q':
                print('Ses ayarlarından çıkış yapılıyor.')
                break

            if cevap == '-' and self.ses_seviyesi > 0:
                print('Ses seviyesi azaltılıyor..')
                self.ses_seviyesi -= 1
                print('Ses seviyesi azaltılmıştır.')
                print('Ses seviyesi:', self.ses_seviyesi)

            elif cevap == '+' and self.ses_seviyesi < 100:
                print('Ses seviyesi arttırılıyor.')
                self.ses_seviyesi += 1
                print('Ses seviyesi arttırılmıştır.')
                print('Ses seviyesi:', self.ses_seviyesi)

            else:
                print('Lütfen tekrar deneyiniz. Hatalı giriş.')

    def program_kaldır(self,program_ismi):
        if program_ismi in self.program_listesi:
            self.program_listesi.remove(program_ismi)
            print('İstenilen program kaldırılmıştır.')
        else:
            print('Program listede bulunmamaktadır.')

    def program_ekle(self,yeni_program):
        self.program_listesi.append(yeni_program)
        print('Program listeye eklenmiştir...')

    def __len__(self):
        return len(self.program_listesi)

    def program_çalıştır(self):
        uygulama = input('Lütfen açmak istediğini uygulamayı giriniz:')
        if uygulama in self.program_listesi:
            print('Lütfen bekleyiniz uygulama açılıyor...')
            time.sleep(1)
            self.program = uygulama
            print('{0} açılan uygulama.'.format(uygulama))
        else:
            print('Böyle bir program bulunmamaktadır.')

    def mevcut_program(self):
        if self.program:
            print('{0} çalışmakta olan program.'.format(self.program))
        else:
            print('Şu anda çalışan program bulunmamaktadır.')




    def bilgilerigoster(self):
        return('''
                  Marka = {}
                  
                  Model = {}
                  
                  İşlemci = {}
                  
                  Ram = {}
                  
                  Depoloma = {}
                  
                  Pc_Durum = {}
                  
                  Program_Listesi = {}
                  
                  Program = {}
                  
                  Ses_seviyesi = {}
                  
                '''.format(self.marka,self.model,self.işlemci,self.ram,self.depolama,self.pc_durum,self.program_listesi,self.program,self.ses_seviyesi))





    def kurulu_programları_goster(self):

        for eleman in self.program_listesi:
            print(eleman)

    def program_kur(self,yeni_program_kur):
        if yeni_program_kur not in self.program_listesi:
            self.program_listesi.append(yeni_program_kur)
            print('İtediğiniz uygulama kısa sürede kurulacaktır.')
            time.sleep(1)
        else:
            print('Böyle bir program zaten bilgisayarınızda bulunmaktadır.')



print(
'''

BİLGİSAYAR SINIFI

İşlemler 

1.Aç
2.Kapat
3.Durum Kontrol
4.Ses Kontrol
5.Program Kaldır
6.Program Ekle
7.Mevcut Program
8.Bilgisayar Bilgileri
9.Kurulu Programlar 
10.Program Çalıştır
11.Program Kur
    
Çıkmak için lütfen q basınız.   
'''
)
Bilgisayar = Bilgisayar('Hp','Victus','İntel i5 14.Nesil',16,1000,'Kapalı',['Word'],0,'Word')
while True:
    işlem = input('Lütfen bir işlem giriniz:')
    if işlem == 'q':
        print('Programdan çıkış yapılıyor.')
        break

    işlem = int(işlem)

    if işlem == 1:
        Bilgisayar.pc_ac()
    elif işlem == 2:
        Bilgisayar.pc_kapat()
    elif işlem == 3:
        Bilgisayar.durum_kontrol()
    elif işlem == 4:
        Bilgisayar.ses_kontrol()
    elif işlem == 5:
        program_ismi = input("Kaldırmak istediğiniz programın adını girin:")
        Bilgisayar.program_kaldır(program_ismi)
    elif işlem == 6:
        yeni_program = input('Eklemek istediğiniz programı giriniz:')
        Bilgisayar.program_ekle(yeni_program)
    elif işlem == 7:
        Bilgisayar.mevcut_program()
    elif işlem == 8:
        print(Bilgisayar.bilgilerigoster())
    elif işlem == 9:
        Bilgisayar.kurulu_programları_goster()
    elif işlem == 10:
        Bilgisayar.program_çalıştır()
    elif işlem == 11:
        yeni_program_kur = input('Lütfen kurmak istediğini programın adını giriniz: ')
        Bilgisayar.program_kur(yeni_program_kur)
    else:
        print('Hatalı giriş lütfen daha sonra tekrar deneyizz...')






















