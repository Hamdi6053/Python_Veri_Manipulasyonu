birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

def okunus(sayı):

    birbas = sayı % 10
    onlarbas = sayı // 10

    return onlar[onlarbas] + ' ' + birler[birbas]


sayı = int(input('Sayi:'))
print(okunus(sayı))

while True:
    sayı = input('sayı')
    if sayı == 'q':
        print('son..')
        break
    else:
        sayı = int(sayı)
        print(okunus(sayı))

