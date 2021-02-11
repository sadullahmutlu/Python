#Listeler
#oluşturuluş bir listeyi başka bir nesnede çağırabiliyoruz 
rakamlar = [0,1,2,3,4,5,6,7,8,9]
sayılar = [rakamlar,10,11,12,13,14,15,16,17,18,19,20]

print("rakamlar listesinin uzunluğu =", len(rakamlar))
print("sayılar listesinin uzunluğu =", len(sayılar))
 
print("rakamlar listesinin 3.cü indexteki değeri =" ,rakamlar[3])
print("sayılar listesinin 0.ci indexteki değeri =" ,sayılar[0])

print("sayılar listesinin 0.ci indexteki değerinin türü =" , type(sayılar[0]))
print("rakamlar listesinin 0.ci indexteki değerinin türü =" , type(rakamlar[0]))
print("sayılar listesinin 1.ci indexteki değerinin türü =" , type(sayılar[1]))

print("rakamlar listesinin 0.ci indexten 6.cı indexe kadarki değerleri =" ,rakamlar[0:6])
print("sayılar listesinin 0.ci indexten 3.cü indexe kadarki değerleri =" ,sayılar[0:3])

print("rakamlar listesinin ilk indexten indexten 4.cü indexe kadarki değerleri =" ,rakamlar[:4])
print("sayılar listesinin 1.ci indexten en son indexe kadarki değerleri =" ,sayılar[1:])


print("sayılar listesinin 0 inci indexindeki listenin 2.ci indexsindeki eleman=" ,sayılar[0][2])


#listede eleman değiştirme 
isimler = ["ahmet", "mehmet","cenk", "berke", "hamit","cansu", "yasemin", "elif","hilal"]

#listenin ikinci indexindeki cenk ismini cengiz ile değiştirebiliriz
isimler[2] = "cengiz"

#listeyi ekrana yazdıralım
print(isimler)

#ilk indeksten 2.ci indekse kadar olan isimleri değiştirelim
isimler[:2] = "sadullah", "yavuz"
print(isimler)

#listeye eleman ekleme
cisimler = ["masa", "koltuk", "kanepe", "ayna", "televizyon", "koltuk", "sandelye"]
print(cisimler)

#listeye 3 tane daha cisim ekleyelim
cisimler = cisimler + ["bilgisayar","ps4","ajanda"]

print(cisimler)

#eleman silme
del cisimler[6:] #listedeki 6.ci indeksten sonrası silmesini istedik
print(cisimler)










