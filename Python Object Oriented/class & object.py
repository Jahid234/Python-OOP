## ....... Class and object

class Computer:     #................class
    
    def config(self):
        print("i7, 16gb, 1TB")
        
        
com1 = Computer()   #................object
com2 = Computer()   #................object

Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()



## ...............  _init_method

class Computer:    #class
    
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    
    def config(self):
        print("Config is: ", self.cpu, self.ram)
        
        
com1 = Computer("i5", 8) 
com2 = Computer("Ryzen 8", 16) 

com1.config()
com2.config()



##................... Constructor, self


class Computer:
    
    def __init__(self):
        self.name="Jahid"
        self.age = 22
        
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
        
c1 = Computer()
c1.age = 28
c2 = Computer()
    
if c1.compare(c2):
    print("They are same")
else:
    print("They are different")  
    
print(c1.name)
print(c2.name)



# ## ................. Inner Class in Python

class Student:     # ............. Outer class
    
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
        
        
        
    class laptop:      #.......... Inner class
        
        def __init__(self):
            self.brand = "HP"
            self.ram = 8
            self.cpu ="i5"
            
        def show(self): 
            print(self.brand, self.ram, self.cpu)
        

s1 = Student("Jahid", 29)
s2 = Student("Alam", 28)

s1.show()

lap1 = s1.lap
lap2 = s2.lap

print(id(lap1))
print(id(lap2))
