from abc import ABC,abstractmethod 

# "POLYMORPHISM (many forms)"
#QUESTION NO 1 -  Function Overriding: Create a Shape class with a method area().
                # Then create two subclasses Circle and Rectangle that override the area()-
                #  method to compute the area of a circle and a rectangle, respectively.

class Shape:
    def area(self):
        pass

class Rectangle():
    def area(self,l,w):
        self.l = l
        self.w = w
        return l*w
    
class Circle:
    def area(self,r):
        self.r = r
        return 2*3.14*(r**2)
    
r = Rectangle()
c = Circle()
print(f"Area of rectangle : {r.area(12,5)}")
print(f"Area of circle : {c.area(100)}")

#QUESTION NO 2 - Polymorphism with Built-in Functions:
                # Use the len() function with a string, list, and dictionary. Explain why this is an example of polymorphism.

s = input("Enter a string: ")
l = [5,7,16,"apple",3.14,900,True]
dic = {"a":1,"b":2,"c":3,"d":4}
print(f"Length of string : {len(s)}")
print(f"Length of list : {len(l)}")
print(f"Length of dictionary : {len(dic)}")
#This is a example of polymorphism because len() function do different work here.

#QUESTION NO 3 - Operator Overloading:  # Define a Vector class.
                # Override the + operator so that you can add two vectors.

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x+other.x , self.y+other.y)
        
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    
v1 = Vector(4,3)
v2 = Vector(6,8)
print(f"Vector v1: {v1}")
print(f"Vector v2: {v2}")
print(f"After addition :{v1+v2}")


#QUESTION NO 4 - Duck Typing:  # Create two classes, Writer and Singer, each with a method perform().
                # Write a function stage_show(artist) that calls perform() without checking the type of the object.
                # Test it with both Writer and Singer.
                        
class Writer:
    def perform(self):
        print("I can write an amezing story!.")

class Singer:
    def perform(self):
        print("I can sing a great song!")

def stage_show(artist):
    artist.perform()

w = Writer()
s = Singer()
w.perform()
s.perform()
                    

#QUESTION NO 5 -  Abstract Base Class:
            # Use the abc module to create an abstract base class Employee with an abstract method calculate_salary().
            # Then create two concrete classes FullTimeEmployee and PartTimeEmployee that implement calculate_salary() differently.

class Employee:
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee:
    def calculate_salary(self,salary,allowances):
        self.salary = salary
        self.allowances = allowances
        return salary+allowances

class PartTimeEmployee:
    def calculate_salary(self,hour,sal_per_h):
        self.hour = hour
        self.sal_per_h = sal_per_h
        return hour*sal_per_h
    
f = FullTimeEmployee()
p = PartTimeEmployee()
print(f"Salary of full time employee: {f.calculate_salary(50000,12000)}")
print(f"Salary of part time employee: {p.calculate_salary(5,3000)}")





