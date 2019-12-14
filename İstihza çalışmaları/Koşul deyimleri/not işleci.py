#not işlecinin çalışma  mantığını daha iyi anlamak için
#yapılan bir koşul deyimi çalışması
#veri girilmedin giriş yapılması sorun çıkartır.
#not operatörü ile bunu hataya yer bırakmadan
#çözümleyeceğiz

print("Hoş geldiniz.")
kullanıcı_adı = input("Kullanıcı adınızı giriniz:")
parola = input("Şifrenizi giriniz\t:")

if not kullanıcı_adı:
    print("kullanıcı adı boş bırakılamaz")
if not parola:
    print("parola boş bırakılamaz")