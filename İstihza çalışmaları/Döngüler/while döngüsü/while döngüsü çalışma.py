# kullanıcıdan alınan sayıya kadar olan çşft sayıları bulma

girizgah = """
girilen sayıya kadar olan çift sayıları
gösteren program
çıkmak için q"""

print(girizgah)

while True:
    sayi = input("Sayı giriniz\t:")

    if sayi == "q":
        print("Program sonlandırılıyor")
        break
    else:
        sayi = int(sayi)
        başlangıç = 0

        while başlangıç < sayi:
            başlangıç += 1

            if başlangıç % 2 == 0:
                print(başlangıç)