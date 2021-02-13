#map:verilen bir nesnenin üzerinde tanımlanacak bir fonskiyonu çalıştırma imkanı verir
liste = [2,4,6,8,10]
print(list(map(lambda x: x+10, liste)))

#filter: iteratif bir nesne alır ve başka bir nesne oluşturur nesne içinde 
#aradığı tüm elemanlar filtrelenir

liste_2 = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x % 2 == 0, liste_2)))


#reduce:İndirgeme işleme yapar

from functools import reduce

liste_3 = [1,2,3,4,5,6]
print(reduce(lambda a,b: a + b, liste_3))
