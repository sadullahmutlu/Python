
liste_1 = [1, 2, 3, 5, 7, 8, 9, 10]
liste_2= [1, 2, 4, 8, 9]

#iki listenin elemanlarının keşimi
sonuc = list(filter(lambda x: x in liste_1, liste_2)) 
print ("İki listenin kesişimi =",sonuc)