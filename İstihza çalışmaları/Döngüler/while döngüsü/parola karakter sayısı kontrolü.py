#girilen parolanın 3 karakterden kısa
#8 karakterden uzun olmadığını kontrol etmek
#aynı zamanda parola
#tamamlanana kadar döngü olacak

while True:
    parola = input("Parolanınızı girin\t:")

    if not parola:
        print("Parola boş bırakılamaz.")

    elif len(parola) < 3 or len(parola) > 8:    #8 < len(parola) < 3: #olmadı
        print("Parolanın 8 karekterden uzun"
              " 3 karekterden kısa olamaz.")

    else:
        print("Prolanız\t:",parola)
        break