# karakter dizisindeki karakterlerin sayılması ilk önce
#kullanıcıdan bir har alarak o harfin karakter dizisinde kaç defa olduğunu bulmak

metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""

harf = input("sorgulamak istediğiniz harfi girin\t:")
sayaç = 0

for i in metin:
    if i == harf:
        sayaç += 1
print(harf,"harfi metinde ", sayaç,"defa geçmektedir")
