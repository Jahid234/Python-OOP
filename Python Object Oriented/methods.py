# ### .............. Types of methods

class Student:
    
    school = "ABC"
    
    def __init__(self, m1, m2, m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    def get_m1(self):
        return self.m1
    
    def set_m1(self, value):
        self.m1 = value
        
     
    #..... class methods
    
    @classmethod    
    def get_school(cls):
        return cls.school
    
    
    
    #.......static method
    
    @staticmethod
    def info():
        print("This is a static method, I have seen.")
    

s1 = Student(34, 67, 32)
s2 = Student(39, 45, 78)

print(s1.avg())
print(s2.avg())
print(s1.m1)
print(Student.get_school())
Student.info()

