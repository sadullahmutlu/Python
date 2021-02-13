#bir fonksiyon kullanılarak istediğimiz zaman direk olarak ekleme yapabilmek için
# kullanımı 
class calisanlarin_Ozellikleri():
    def __init__(self):
        self.yas = ""
        self.saglik_durumu = []
    def durum_ekle(self, yeni_durumu):
        self.saglik_durumu.append(yeni_durumu)
        
        
serhat = calisanlarin_Ozellikleri()
serhat.yas = 22

zafer = calisanlarin_Ozellikleri()
zafer.yas = 31

yakup = calisanlarin_Ozellikleri()
yakup.yas = 45

#append fonkisyonu kullanmadan direk olarak durumu ekleyrbiliriz
serhat.durum_ekle("Sağlıklı")
zafer.durum_ekle("Bacağı kırılmış")
yakup.durum_ekle ("Korona olmuş")

print("Serhatın yaşı ve Sağlık Durumu =", serhat.yas, serhat.saglik_durumu)
print("Zaferin yaşı ve Sağlık Durumu =", zafer.yas, zafer.saglik_durumu)
print("Yakupun yaşı ve Sağlık Durumu =", yakup.yas, yakup.saglik_durumu)

