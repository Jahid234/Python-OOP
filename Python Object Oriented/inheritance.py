# ## ....... Inheritance in python

class A:
    
    def feature1(self):
        print("feature 1 is working")  ## ... Super class
        
    def feature2(self):
        print("feature 2 is working") ## ... Parent class
    
    
        
class B():   
    
    def feature3(self):
        print("feature 3 is working") ## ... sub class
        
    def feature4(self):
        print("feature 4 is working") ## ... child class
        

class C (A, B):  # ...... class c inherites A, B ............ multiple inheritance
    
    def feature5(self):
        print("feature 5 is working")
        
a1 = A()
a1.feature1()
        
b1 = B()
b1.feature4()

c1 = C()
c1.feature5()


### ..... Constructor in inheritance

class A:
    
    def __init__(self):
        print("init  A")
    
    def feature1(self):
        print("feature 1 is working")  
        
    def feature2(self):
        print("feature 2 is working") 
    
    
        
class B():
    
    def __init__(self):
        super().__init__()
        print("init B")   
     
    
    def feature3(self):
        print("feature 3 is working") 
        
    def feature4(self):
        print("feature 4 is working") 
        

class C(A, B):  
    
    def __init__(self):
        super().__init__()
        print("init c")
    
    def feature5(self):
        print("feature 5 is working")
    
    
    def feat(self):
        super().feature2()
        
a1 = C()

a1.feature2()
        


