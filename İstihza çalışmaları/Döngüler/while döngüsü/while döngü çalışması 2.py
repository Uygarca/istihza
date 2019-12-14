# kullanıcıdan alınan sayıya kadar olan çşft sayıları bulma

girizgah = """
girilen sayıya kadar olan çift sayıları
gösteren program
çıkmak için q"""

print(girizgah)
sayi = input("Sayı giriniz\t:")

while sayi != "q":
    sayi = int(sayi)
    başlangıç = 0

    while başlangıç < sayi:
        başlangıç += 1

        if başlangıç % 2 == 0:
            print(başlangıç)

    sayi = input("Sayı giriniz\t:")
    
print("Program sonlandırılıyor.")