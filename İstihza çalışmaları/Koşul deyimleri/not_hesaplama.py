#girilen puana  göre notu hesaplayan program
#if, elif, else ve bool işleçleri çalışması

print("Puana göre not hesaplayan programa hoş geldiniz.")

notlar = int(input("lütfen puanınızı giriniz\t:"))

if notlar > 100 or notlar < 0:
    print("Notunuz 0'dan küçük 100'den büyük olamaz.")
    
elif 90 <= notlar <= 100:
    print("A aldınız")
    
elif 80 <= notlar <= 89:
    print("B aldınız")
    
elif 70 <= notlar <= 79:
    print("C aldınız")
    
elif 60 <= notlar <= 69:
    print("D aldınız")
    
elif 0 <= notlar <= 59:
    print("F aldınız")
