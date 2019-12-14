# Karekater dizilerinin içeriğini karşılaştırma
# ilk dizide olan ikinci dizide olmayan karakterleri bulmak

# ilk aklıma gelen yöntem ilk dizideki her bir karakteri
# ikinci dizideki karakterler ile karşılaştırmak

ilk_dizi = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_dizi = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"

for i in ilk_dizi:
    if not i in ikinci_dizi:
        print(i)

print(30 * "-")

for i in ikinci_dizi:
    if not i in ilk_dizi:
        print(i)

fark =""

for i in ikinci_dizi:
    if not i in ilk_dizi:
        if not i in fark:
            fark += i
print(fark)