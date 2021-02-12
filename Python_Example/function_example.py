#fonksiyon

def toplama(x, y):
    print("toplama işlemi =", x+y, "\n")
toplama(4,12) 

def cikarma(x, y):
    print("çıkarma işlemi =", x-y, "\n")
cikarma(5,2)

def carpma(x, y):
    print("çarpma işlemi =", x*y, "\n")  
carpma(3,2)

def bolme(x, y):
    print("bölme işlemi =", x/y, "\n")
bolme(8,2)

def kare_alma(x):
    print("kare alma işlemi =", x**2, "\n")
kare_alma(3)

def toplama_bolme(x, y, z):
    return (x+y)/z
islem_ornek = toplama_bolme(8,12,3)
print(islem_ornek)
