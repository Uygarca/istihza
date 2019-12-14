#break deyimi örnek

while True:
    parola = input("Parola giriniz\t:")

    if len(parola) < 5:
        print("Parola 5 karakterden az olamamalı!")

    else:
        print("Parola belirlendi = ",parola)
        break