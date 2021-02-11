#tuple oluşturmanın 2 yolu var parantezle yada direk normal olarak oluşturabiliriz

t_örnek = ("mehmet", "furkan","sadullah",1,3,5,6,9.2,11.4,[2,8,5,6,0,9,3])
t_örnek_2 = "mehmet", "furkan","sadullah",1,3,5,6,9.2,11.4,[2,8,5,6,0,9,3]

t = ("ahmet")
#adından bir tuple oluşturalım, type fonskiyonu ile baktığımzda
#tuple değil string olarak geçiyor bunu düzeltmek için sonuna bi virgül koyarak
#düzeltebiliriz
type(t)

#virgül koyup yazdığımızda tuple'a döndüğünü görmüş olduk 
t_2 = ("ahmet",)
type(t_2)

#tuple işlemleri

t_uygulama = ("mehmet", "furkan","sadullah",1,3,5,6,9.2,11.4,[2,8,5,6,0,9,3])

print(t_uygulama[1])
print(t_uygulama[0:2])
print(t_uygulama[1:3])
print(t_uygulama[2:])

#tupleler değiştirelemez olduğundan eleman ekleyemeyiz





