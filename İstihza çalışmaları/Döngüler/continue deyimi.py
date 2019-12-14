#continue deyimi

while True:
    sayı = input("bir sayı girin\t:")

    if sayı == "q":
        break

    if len(sayı) <= 3:
        continue

    print("en fazla 3 rakam girebilirsiniz")