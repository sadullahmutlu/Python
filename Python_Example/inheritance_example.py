#başka bir zaman başka bir class tanımladığımızda başka classdan bir şey kullanmak
#istiyorsak miras yapısını kullanırız

class Employees():
    def __init__(self):
        self.Name = ""
        self.Age = ""
        self.Adress =""
        
class Developer(Employees):
    def __init__(self):
        self.Programming_Language = ""
    
Developer_1 = Developer()
Developer_1.Name = "Sadullah"
Developer_1.Age = 22
Developer_1.Adress = "Rize"
Developer_1.Programming_Language = "Python"
print("Developer_1 =", Developer_1.Name, Developer_1.Age, Developer_1.Adress,Developer_1.Programming_Language)

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

Salesman = Marketing()
Salesman.Name = "Ahmet"
Salesman.Age = 25
Salesman.Adress = "Bursa"
Salesman.StoryTelling = "Oratory"
print("Salesman =", Salesman.Name, Salesman.Age, Salesman.Adress,Salesman.StoryTelling)