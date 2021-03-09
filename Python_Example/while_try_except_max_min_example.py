#Enter 7, 2 , sadullah, 4 ,10 and then exit with done input

lst = []

while True:
    num = (input("Enter a number: "))
    if num == "done" : 
        break
    try:
        deger = float(num)
    except:
        print("Invalid input")
        continue
    lst.append(num)
    
for i in range(0, len(lst)): 
    lst[i] = int(lst[i]) 

print("Maximum is", max(lst))
print("Minimum is", min(lst))