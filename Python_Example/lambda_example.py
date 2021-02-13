#lambda kullanrak toplama işlemi
Sum = lambda a, b : a + b 
print("Sum a+b =", Sum(3,4))

liste = [("a",28),("c",65),("e",8),("d",21),("b",9)]
print("List sorted by index 0 = ", sorted(liste, key = lambda x: x[0]))
print("List sorted by index 1 = ", sorted(liste, key = lambda x: x[1]))



