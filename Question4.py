sonuc, a, b = 0, 1, 2

while a <= 4e6:
    if a % 2 == 0:
        sonuc += a
    a, b = b, a+b

print(sonuc)