def Toplambolen(sayı):
    bolen = 0
    for i in range(1,sayı):
        if sayı % i == 0 :
            bolen  += i
    return bolen == sayı


for i in range(1,1001):
    if (Toplambolen(i)):
        print('Mükemmel sayı:',i)


