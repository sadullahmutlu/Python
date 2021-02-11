#Tip dönüşümleri
#kullanıcdan iki sayı alalım
birinci_Sayi = input("Bir Sayı Girin: ")
ikinci_Sayi = input("İkinci Bir Sayı Girin: ")

#aldığımız sayıların ne tür olduğuna bakalım
type(birinci_Sayi)
type(ikinci_Sayi)

#type methodu ile türlerine baktığımızda string ifadesi ile karşılaştık
#bu şekilde iki sayıyı toplarsak karşıma girilen sayıların yanyana yazılmış 
#hali gözükücektir

print("yanyana yazılış biçimi =", birinci_Sayi + ikinci_Sayi)

#eğer normal toplama işlemi yapmak istersek başına int yazarak yapabilriz

toplam = int(birinci_Sayi) + int(ikinci_Sayi)
print ("iki sayının toplamı =", toplam)

#Float bir sayıyı integer olarak yazmak için int olarak belirtebiliriz
c = 53.23549843
print("Float sayıyı integer olarak yazmak için =", int(c))

b = 35
print ("İnteger bir sayıyı float olarak yazdırmak için =", float(b))





