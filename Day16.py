from abc import ABC,abstractmethod 

#  "INHERITANCE"


#Simple Inhertance
#QUESTION NO 1 - Create a class `Vehicle` with attributes `brand` and `year`.  
                # Create a subclass `Car` that adds an attribute `number_of_doors`.  
                # Create an object of `Car` and print all attributes.

class Vehicle:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year,no_of_doors):
        super().__init__(brand, year)
        self.no_of_doors = no_of_doors

    def print(self):
        print(f"Brand : {self.brand}")
        print(f"Year : {self.year}")
        print(f"Number of doors : {self.no_of_doors}")

c = Car("BMW",2024,2)
c.print()
    
#QUESTION NO 2 - Create a class `Employee` with method `get_role()` that returns "Employee".  
                # Create a subclass `Manager` that overrides `get_role()` to return "Manager".  
                # Print roles of both an `Employee` object and a `Manager` object.
#Method overriding
class Employee:
    def get_role(self):
        return f"I am a Employee"
    
class Manager(Employee):
    def get_role(self):
        return f"I am a Manager"
    
e = Employee()
m = Manager()
print(e.get_role())
print(m.get_role())


#QUESTION NO 3 - Create two classes `Writer` and `Editor`, each with a method `show_role()`.  
                # Create a subclass `ContentCreator` that inherits from both.  
                # Call `show_role()` from `ContentCreator` and explain which one is called.

#Multiple Inheritance
class Writer:
    def show_role(self):
        return f"Please hire me.I can write your content."
    
class Editor:
    def show_role(self):
        return f"Please hire me. I can edite your content videos and photos."
    
class ContentCreator(Writer,Editor):
    def show_role(self):
        return super.show_role() #Super calls only first parent class
        # return Editor.show_role(self) #It call the method by class name

cc = ContentCreator()
print(cc.show_role())


# QUESTION NO 4 - Create an abstract base class `Shape` with abstract method `area()`.  
                # Create subclasses `Rectangle` and `Circle` that implement `area()`.  
                # Write code to calculate area of both shapes.

class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle:
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
print(f"Area of rectangle : {r.area(11,8)}")
print(f"Area of circle : {c.area(5)}")


#QUESTION NO 5 - Create a class `Account` with a protected member `_balance`.  
                # Create a subclass `SavingsAccount` that accesses `_balance`.  
                # Demonstrate how a subclass can use protected members.

class Account:
    def __init__(self,_balance):
        self._balance = _balance

class SavingAccount(Account):
     def __init__(self, _balance):
         super().__init__(_balance)

     def deposit(self,amo):
        self.amo = amo
        self._balance = self._balance+amo
        return self._balance
     
sa = SavingAccount(10000)
print(f"Total balance : {sa._balance}")
print(f"Total balance after deposite : {sa.deposit(3000)}")

        