import random

szam = random.randint(1, 100)
tipp = -1
tippek_szama = 0

print('Gondoltam egy számra, találd ki!')

while szam != tipp:
    tipp = int(input("mi a tipped? "))
    if tipp < szam:
        print('nagyobb számra gondoltam!')
    elif tipp > szam:
        print('kisebb számra gondoltam!')
    tippek_szama += 1

print(f'gratulálok valóban a {szam}-ra gondoltam!')
print(f'ezt {tippek_szama} próbálkozással találtad ki!')
print('ügyes vagy! <3 :3 :)')