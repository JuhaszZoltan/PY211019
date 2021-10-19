pin = 1234
puk = 12345678

probalkozasok = 3
proba = 0000
while probalkozasok != 0 and pin != int(input('kerem a PIN kodot: ')):
    probalkozasok -= 1
if probalkozasok  == 0:
    print('3x is elrontottad :( kérem a PUK kódot!')
    probalkozasok = 3
    while probalkozasok != 0 and puk != int(input('kerem a PUK kodot: ')):
        probalkozasok -= 1
    if probalkozasok == 0: print('csak a 112 hívható')
    else: print('ok, beléptél')
else: print('ok, belépték')

