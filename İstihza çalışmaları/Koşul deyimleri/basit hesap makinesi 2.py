#basit hesap makinesi v2.0
#döngü eklendi

giriş = """
1 topla
2 çıkar
3 çarp
4 böl
5 karesini hesapla
6 kare kök hesapla

çıkış için q 
"""
print(giriş)
islem = input("Yapmak istediğiniz işlemi seçiniz\t:")

while islem != "q":
    if not islem:  # hiç bir giriş yapılmamasına karşı oluşturuldu
        print("Giriş yapmalısınız")
        print("Aşağıdaki seçeneklerden birisiniz seçmelisini", giriş)

    elif islem == "1":
        print("toplama işlemini seçtiniz")
        sayı1 = int(input("1. sayı\t:"))
        sayı2 = int(input("2. sayı\t:"))
        print("{} + {} = {}".format(sayı1, sayı2, (sayı1 + sayı2)))

    elif islem == "2":
        print("çıkarma işlemini seçtiniz")
        sayı1 = int(input("1. sayı\t:"))
        sayı2 = int(input("2. sayı\t:"))
        print("{} - {} = {}".format(sayı1, sayı2, (sayı1 - sayı2)))

    elif islem == "3":
        print("çarpma işlemini seçtiniz")
        sayı1 = int(input("1. sayı\t:"))
        sayı2 = int(input("2. sayı\t:"))
        print("{} * {} = {}".format(sayı1, sayı2, (sayı1 * sayı2)))

    elif islem == "4":
        print("bölme işlemini seçtiniz")
        sayı1 = int(input("1. sayı\t:"))
        sayı2 = int(input("2. sayı\t:"))
        print("{} / {} = {}  ".format(sayı1, sayı2, (sayı1 / sayı2)))

    elif islem == "5":
        print("karesini hesaplama işlemini seçtiniz")
        sayı1 = int(input("1. sayı\t:"))
        print("{}^{} = {}  ".format(sayı1, 2, (sayı1 ** 2)))

    elif islem == "6":
        print("karekök hesaplama işlemini seçtiniz")
        sayı1 = int(input("1. sayı\t:"))
        print("{} karekökü = {}  ".format(sayı1, (sayı1 ** 0.5)))

    else:  # seçeneklerin dışında kalan tüm durumlar için oluşturuldu
        print("Aşağıdaki seçeneklerden birisiniz seçmelisini", giriş)

    islem = input("\nYapmak istediğiniz işlemi seçiniz\t:")