#yapılan girişte türköe karakter kullanılmaması
#için for ile denetleme
#while tam döngü yapıldı tekrar tekrar çalıştırmamak için


tr_harfler = "çğıöşüİ"

while True:

    parola = input("Parolanızı girin\t:")

    if parola == "q":
        break

    else:
        for harf in parola:
            if harf in tr_harfler:
                print("Türkçe karakter kullanamazsınız")