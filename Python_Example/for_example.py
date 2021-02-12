#yapılan bi işten herkese yüzde 10 zam yapılması sonucu yeni maaşları 
# gösteren bir uygulama

eski_maaslar = [4200,4800,5300,7400,11700,3400,2800,4500,9800,8100]

#yeni maaşları fonksiyon içinde zamlarını yapıp ekrana yazdırdık
def yeni_maas(x):
    print(x*10/100 + x)

#eski maaşları alıp yeni maas adlı fonksiyona yolladık
for i in eski_maaslar:
    yeni_maas(i)
    
    
