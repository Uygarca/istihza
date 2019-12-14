#mükemmel sayı denemesi

print("1'den 1000'e kadar asal sayılar")

for i in range(1,1001):
    bölenler = []
    toplam = 0

    for j in range(1,i):

        if i % j == 0:
            bölenler.append(j)
            toplam += j

    if i == toplam:
        print(i,"= mükemmel sayı")
        print(bölenler)