'''Proje 2
"futbolcular.txt" şeklinde bir dosya oluşturun ve içine Galatasaray,Fenerbahçe ve Beşiktaşta oynayan futbolcuları rastgele yerleştirin. Bu dosyadan herbir takımın futbolcularını ayırarak
"gs.txt" , "fb.txt", "bjk.txt" şeklinde 3 farklı dosyaya yazın.

"futbolcular.txt" dosyasının başlangıç hali şu şekilde olsun.

                Fernando Muslera,Galatasaray
                Atiba Hutchinson,Beşiktaş
                Simon Kjaer,Fenerbahçe
                           //
                           //
                           //
                           //
                           //'''
from idlelib.iomenu import encoding

'''with open ('Futbolcular.txt','w',encoding='utf-8') as file:
    print(file.write('Muslera,Beşiktaş\n'))

with open('Futbolcular.txt','a',encoding = 'utf-8') as file:
    print(file.write('Serdar Aziz,Fenerbahçe\n'))
    print(file.write('Volkan Demirel,Fenerbahçe\n'))
    print(file.write('Alex,Fenerbahçe\n'))
    print(file.write('Talisca,Beşiktaş\n'))
    print(file.write('Melo,Galatasaray\n'))
    print(file.write('Selçuk İnan,Galatasaray\n'))
    print(file.write('Onur Bulut,Beşiktas\n'))
    print(file.write('Mert Günok,Beşiktaş\n'))'''

def ayırma(satır):
    satır = satır[:-1]
    liste = satır.split(',')
    isim = liste[0]
    takım = liste[1]

    if takım == 'Fenerbahçe':








with open('Futbolcular.txt','r',encoding='utf-8') as file:
    for i in file:
        ayırma(i)













