#Sözluk oluşturma ve sözlük işlemleri
#İlk sıradakiler keydir bu keylerle elemanları çağırabiliriz
ornek_sozluk = {"RAKAM" : [0,1,2,3,4,5,6,7,8,9],
                "SAYI":["10 LUK SAYILAR",10,11,12,13,14,15,16,17,18,19],
                "YÜZ" : "yüzlük sayılar",
                "BİN" : "BİNLİK SAYILAR"}
              
ornek_sozluk

#sözlükler sırasızdır bu yüzden indexleme ile eleman seçemeyiz key error verir
#bu yüzden keylerle eleman seçebiliriz

ornek_sozluk["SAYI"]

#Sözlük içinde sözlük oluşturabiliriz

ornek_sozluk_2 = {"RAKAM" : 
                {"YÜZ1" :101,
                "İKİ1" : 201,
                "ÜÇ1" : 301},
                "SAYI":["10 LUK SAYILAR",10,11,12,13,14,15,16,17,18,19],
                "YÜZ" : "yüzlük sayılar",
                "BİN" : "BİNLİK SAYILAR"}
ornek_sozluk_2
ornek_sozluk_2["RAKAM"]
#Sözlüğün içindeki söZlükteki elemanı seçmek için 
ornek_sozluk_2["RAKAM"]["İKİ1"]


#eleman ekleme

ornek_sozluk["MTL"] = "MUTLU ADAM"
ornek_sozluk

ornek_sozluk["RAKAM"] = "RAKAMLAR"
ornek_sozluk

ornek_sozluk[53] = "RİZE"
ornek_sozluk

#sözlüklere liste ekleyemeyiz
#tupleları sözlüğe ekleyebiliriz

ornek_tuple = ("tuple",)
ornek_sozluk[ornek_tuple] = "tuple eklemesi de yaptık"
ornek_sozluk


