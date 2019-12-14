#Örnek uygulama
#Kullanıcıdan alınan kullanıcı adı ve parolanın 40
#karakteri geçip geçmediğini kontrol etmek için
# if çalışması

kullanıcı_adı = input("Kullanıcı adını giriniz\t:")
sifre = input("Şifrenizi giriniz\t:")

toplam_uzunluk = len(kullanıcı_adı) + len (sifre)

if toplam_uzunluk > 40:
    print("Kullanıcı adı ve şifre 40 karakteri geçemez.")
else:
    print("Sisteme hoş geldiniz")
