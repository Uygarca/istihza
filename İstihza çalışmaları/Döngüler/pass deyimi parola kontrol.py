

while True:
    parola = input("Parolanınızı girin\t:")

    if not parola:
        #print("Parola boş bırakılamaz.")
        pass

    elif len(parola) in range(3,8):    #8 < len(parola) < 3: #olmadı
        print("Parolanız\t:",parola)
        break

    else:
        print("Parolanın 8 karekterden uzun"
              " 3 karekterden kısa olamaz.")