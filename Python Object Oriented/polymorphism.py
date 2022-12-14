# ## ... Duck typing in python

class VScode:
    
    def execute(self):
        print("compiling")
        print("running")
        
class MyEditor:
    
    def execute(self):
        print("Spell check")
        print("Convention check")
        print("compiling")
        print("running")        

class Latop:
    
    def code(self, ide):
        ide.execute()        
        

ide = VScode()

lap1 = Latop()
lap1.code(ide)

print(" ")


ide = MyEditor()

lap1 = Latop()
lap1.code(ide)


## ... Operator overloading in python

a = 10
b = 11

print(a+b)
print(int.__add__(a, b))  ## .. add operator


class Student:
    
    def __init__(self, m1, m2):
        self.m1 = m1 
        self.m2 = m2
        
    def __add__(self, other):
        m1 = self.m1 + other.m1 
        m2 = self.m2 + other.m2 
        s3 = Student(m1, m2)
        
        return s3 
    
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2 
        
        if r1>r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)
        
        
s1 = Student(58, 69)
s2 = Student(60, 65)

s3 = s1 + s2
print(s3.m2)

if s1 > s2:
    print("s1 wins")    
else:
    print("s2 wins")
    
print(s1)
print(s2)



## ..... Two types of polymorphism (1. Method overloading and 2. Method overriding)





        
