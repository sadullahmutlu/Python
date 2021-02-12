
meyve_fiyatlar = [2.85, 3, 5, 1.85, 4.80, 0.95, 4, 2.65, 6.45, 5.15, 7.55, 11.45, 34.75]
meyve_fiyatlar.sort()

#break komutu koşulladaki şarta gelince dur işlemini yapar
for i in meyve_fiyatlar:
    if i > 6:
        print("Bu meyveler alınabilir")
        break
    print(i)
    
    