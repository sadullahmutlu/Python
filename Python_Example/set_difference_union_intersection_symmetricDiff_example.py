
# =============================================================================
# #difference ,intersection , union ve symmetric_difference işlemleri kumeler 
# üzerinde gerçekleştiriyoruz.
# =============================================================================

kume_1 = set ([1,2,3])
kume_2 = set ([2,3,4])
kume_3 = set ([3,4,5])

#difference işlemiyle kümelerdeki farklı olan elemanları bulruz
print("kume_1 in kume_2 den farkı =" ,kume_1.difference(kume_2))
print("kume_2 nin kume_1 den farkı =" ,kume_2.difference(kume_1))
print("kume_2 nin kume_3 den farkı =" ,kume_2.difference(kume_3))
print("kume_3 ün kume_2 den farkı =" ,kume_3.difference(kume_2), "\n")

#symmetric_difference işlemi ile ikisine aynı anda bakabiliyoruz
print("kume_1 ve 2 deki farklı elemanları =" ,kume_1.symmetric_difference(kume_2))
print("kume_2 ve 3 teki farklı elemanlar =" ,kume_2.symmetric_difference(kume_3), "\n")

#diğer bir şekilde
print("kume_1 in kume_2 den farkı =" ,kume_1 - kume_2)
print("kume_2 nin kume_1 den farkı =" ,kume_2 - kume_1)
print("kume_2 nin kume_3 den farkı =" ,kume_2 - kume_3)
print("kume_3 ün kume_2 den farkı =" , kume_3 - kume_2, "\n")

#intersection keşisim işlemi
print("kume_1 ile kume_2 nin keşismesi =" ,kume_1.intersection(kume_2))
print("kume_2 ile kume_3 nin keşismesi =" ,kume_2.intersection(kume_3),)
print("kume_1 ile kume_2 nin keşismesi =" ,kume_1 & kume_2)
print("kume_2 ile kume_3 nin keşismesi =" ,kume_2 & kume_3, "\n")

#union birleşim işlemi
print("kume_1 ile kume_2 nin birleşmesi =" ,kume_1.union(kume_2))
print("kume_2 ile kume_3 nin birleşmesi =" ,kume_2.union(kume_3))


