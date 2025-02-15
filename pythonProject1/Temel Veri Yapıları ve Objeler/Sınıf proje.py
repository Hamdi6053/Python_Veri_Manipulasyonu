'''Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin
toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından
miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait
ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından
miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait
ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından
miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait
ek özellikler ve metodlar ekleyin.'''


class Hayvan():
    def __init__(self,Yas,Tür,Beslenme,Kilo):
        print('Hayvan sınıfının init fonksiyonu.')
        self.Tür = Tür
        self.Yas = Yas
        self.Beslenme = Beslenme
        self.Kilo = Kilo

class Köpek(Hayvan):

    def __init__(self, Yas,Tür, Beslenme, Kilo, Renk):
        print('Köpek Sınıfının init fonksiyonu.')
        super().__init__(Yas, Tür, Beslenme, Kilo)
        self.Renk = Renk


    def __str__(self):
        print(
        '''
        Yas = {0}
        
        Tür = {1}
        
        Beslenme = {2}
        
        Kilo = {3}
        
        Renk = {4}
        '''
        .format(self.Yas,self.Tür,self.Beslenme,self.Kilo,self.Renk))

class Kus(Hayvan):


    def __init__(self,Yas,Tür,Beslenme,Kilo,Renk,Kanat):
        print('Kus sınıfının init fonksiyonu')
        super().__init__(Yas,Tür,Beslenme,Kilo)
        self.Renk = Renk
        self.Kanat = Kanat

    def __str__(self):
        return(
            '''
            Yas = {0}

            Tür = {1}

            Beslenme = {2}

            Kilo = {3}

            Renk = {4}
            
            Kanat = {5}
            '''
            .format(self.Yas, self.Tür, self.Beslenme, self.Kilo, self.Renk,self.Kanat))

class At(Hayvan):
    def __init__(self,Yas,Tür,Beslenme,Kilo,Renk,Koşu_mesafesi):
        super().__init__(Yas,Tür,Beslenme,Kilo)
        self.Renk = Renk
        self.Koşu_mesafesi = Koşu_mesafesi

    def __str__(self):
        return(
            '''
            Yas = {0}

            Tür = {1}

            Beslenme = {2}

            Kilo = {3}

            Renk = {4}

            Koşu_mesafesi = {5}
            '''
            .format(self.Yas, self.Tür, self.Beslenme, self.Kilo, self.Renk, self.Koşu_mesafesi))

    def hesap(self):
        return self.Koşu_mesafesi

    def yarış(self,digerAt):
        print('{} {} ile yarışıyor!.'.format(self.Tür,digerAt.Tür))
        if self.Koşu_mesafesi > digerAt.Koşu_mesafesi:
            print('{} yarışı kazandı.'.format(self.Tür))
        else:
            print('{} yarışı kazandı.'.format(digerAt.Tür))





kopek1 = Köpek(20,'Alman','Etcil',50,'Siyah')

kus1 = Kus(13,'Baykuş','Etcil',5,'Kahverenkli','Kırık')
print(kus1)

At1 = At(23,'Arap','Otçul',200,'Siyah',1500)
print(At1)
At2 = At(3, "İngiliz Atı", "Arpa", 500, "Siyah", 150)
mesafe1 = At1.hesap()
print('Koşu Mesafesi:',mesafe1)

mesafe2 = At2.hesap()
print('Koşu Mesafesi:',mesafe2)

At1.yarış(At2)

print(At2)

