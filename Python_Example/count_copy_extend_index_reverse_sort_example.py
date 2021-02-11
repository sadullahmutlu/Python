#count methodu listedeki elemanların hangisinden kaç adet olduğunu saymamızı sağlar

sayilar = [10,50,20,60,40,10,80,10,40,20,50,70,30,80,30,10,60,30,80,50,20,10,60]
print("listede kaç tane 10 elemeanı var = ", sayilar.count(10))
print("listede kaç tane 20 elemeanı var = ", sayilar.count(20))
print("listede kaç tane 30 elemeanı var = ", sayilar.count(30))
print("listede kaç tane 40 elemeanı var = ", sayilar.count(40))
print("listede kaç tane 50 elemeanı var = ", sayilar.count(50))
print("listede kaç tane 60 elemeanı var = ", sayilar.count(60))
print("listede kaç tane 70 elemeanı var = ", sayilar.count(70))
print("listede kaç tane 80 elemeanı var = ", sayilar.count(80),"\n")

#copy methodu elimindeki mevcut listeyi kopyalamak için kullanabliriz
#sayilar listesini sayılar_kopyala adında ayrı bir listeye koyladık
sayilar_kopyala = sayilar.copy()
print("Kopyalanan dosya = ", sayilar_kopyala, "\n")

#extend methodu iki listeyi birleştirmek için kullanırız
#extend içinde yeni bir liste yaparak sayilar listesine ekledik
sayilar.extend([80,90,100,70,50,90,20,50,30])
print("Extend içinde oluşturulan listeyle eklenen hali =", sayilar ,"\n")

#listeyi ilk haline getirdik
del sayilar[23:]
print("Listenin ilk hali = ", sayilar,"\n")

#yeni bir liste oluşturalım ve onu sayılara ekleyelim
ekleme_Sayilar = [70,40,20,30,70,60,40,10,100,30,10,20,90,70] 
sayilar.extend(ekleme_Sayilar)
print("ekleme_Sayilar ile birleştirelen liste = ", sayilar,"\n")

#index methodu elemanın hangi indekste olduğunu gösterir bize
print("100 elemanının indeksi =", sayilar.index(100),"\n")

#reverse methodu elemanları terse çevirir

sayilar.reverse()
print(sayilar,"\n")
print("100 elemanının indeksi =", sayilar.index(100), "\n")

#sort methodu sıralama için kullanılır

sayilar.sort()
print(sayilar, "\n")
print("100 elemanının indeksi =", sayilar.index(100))





