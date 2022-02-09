# Numbers Divisible By 2 And 3

n = int(input("Sayı giriniz: "))

for i in range(1, n, 1):
    if(i % 2 == 0 and i % 3 == 0):
        print(i)