# =============================================================================
# şirkette maaşa göre yapılan zam oranları ile ilgili basit bir uygulama
# =============================================================================

eski_maaslar = [4200,4800,5300,7400,11700,3400,2800,4500,9800,8100]

#kontrol sonrası maaşa göre zam yapıyoruz.
def besbin_ustu(x):
    print(x*20/100 + x)
def besbin_alti(x):
    print(x*35/100 + x)
    
#alınan maşları karşılaştırıp ona göre zam yapılması için if yapısıyla kontrol
# ediyoruz
for i in eski_maaslar:
    if i >= 5000:
        besbin_ustu(i)
    else:
        besbin_alti(i)

