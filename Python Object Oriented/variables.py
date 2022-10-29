#Types of variable in python

# variable (Instance variable, Classic Variable)

class Car:
    
    wheels = 4            ### ............ class variables
    
    def __init__(self):
        self.mil = 10     ## ............................ Instance variables
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8
Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)