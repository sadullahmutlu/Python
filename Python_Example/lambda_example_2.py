
liste_1 = [1, 2, 3, 5, 8, 10, 14, 18]
liste_2= [4, 8, 9,20,12,18,14]

#iki listenin elemanlarının keşimi
sonuc = list(filter(lambda x: x in liste_1, liste_2)) 
print ("İki listenin kesişimi =",sonuc)