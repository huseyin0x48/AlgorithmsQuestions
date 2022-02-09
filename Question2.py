# Numbers Comporasion Demo

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

if(sayi1 > sayi2):
    sonuc = "Birinci sayı ikinci sayıdan büyüktür."

elif(sayi1 == sayi2):
    sonuc = "Birinci sayı ikinci sayıya eşittir."

else:
    sonuc = "Birinci sayı ikinci sayıdan küçüktür."

print(sonuc)