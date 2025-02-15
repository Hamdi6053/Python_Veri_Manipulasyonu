islem = input('Lütfen bir islem giriniz:')
a = float(input('Lütfen bir değer giriniz:'))
b = float(input('Lütfen bir değer giriniz:'))

if islem == '+':
    print('İki sayinin toplami:',a+b)
elif islem == '-':
    print('İki sayinin farki:',a-b)
elif islem == '*':
    print('İki sayinin carpimi:',a*b)
elif islem == '/':
    print('İki sayinin bölmesi:',a/b)
else:
    print('GEÇERSİZ İŞLEM')

