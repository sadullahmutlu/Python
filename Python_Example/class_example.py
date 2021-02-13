
class kisi_verileri():#init ile girilen değerleri herkes için farklı olarak alabiliyoruz
    def __init__(self):
        self.yas = []
        self.calisma_Durumu = ""
        
mehmet = kisi_verileri()
#appendle mehmetin yaşını ekleyelim aynı işlemi ahmet içinde yapalım
mehmet.yas.append("22")
mehmet.calisma_Durumu = "Öğrenci"
print("Mehmetin yaşı ve Çalışma Durumu =", mehmet.yas, mehmet.calisma_Durumu)

ahmet = kisi_verileri()
ahmet.yas.append("45")
ahmet.calisma_Durumu = "Memur"
print("Ahmetin yaşı ve Çalışma Durumu =", ahmet.yas, ahmet.calisma_Durumu)



