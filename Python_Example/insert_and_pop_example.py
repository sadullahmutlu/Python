#insert ve pop methodlarıyla eleman ekleme silme 

sayilar = [10,20,30,40,50,60]

#insert
#2.ci indekse 25 ekle diyoruz
sayilar.insert(2, 25)
print(sayilar)
print(len(sayilar))

#6.ci indekse 55 eklemesi yapıyoruz
sayilar.insert(6,55)
print(sayilar)
print(len(sayilar))

sayilar.insert(len(sayilar),"65")
print(sayilar)
print(len(sayilar))

#pop 
#0.ci indeksteki elemanı silelim
sayilar.pop(0)
print(sayilar)
print(len(sayilar))

#7.ci indeksteki elemanı silelim
sayilar.pop(7)
print(sayilar)
print(len(sayilar))

