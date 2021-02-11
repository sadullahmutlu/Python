#set sorgu işlemi 

kume_1 = set ([4,5,6,8,9])
kume_2 = set ([2,3,4,5,6,7,8,9,10])
kume_3 = set ([6,7,8])

#iki kümenin keşisimi olup olmadığını sorgulama işlemi
print("iki kümenin keşişimi vardır =", kume_1.isdisjoint(kume_2), "\n")

#bir kümenin bütün elemanlarının başka kümede yer alıp almadığı
print("kume_3 ün elemanları kume_1 de vardır =", kume_3.issubset(kume_1))
print("kume_3 ün elemanları kume_2 de vardır =", kume_3.issubset(kume_2), "\n")

#bir küme diğer kümeyi kapsayıp kapsamadığı
print("kume_1 kume_3 ü kapsıyor =", kume_1.issuperset(kume_3))
print("kume_2 kume_3 ü kapsıyor =", kume_2.issuperset(kume_3))