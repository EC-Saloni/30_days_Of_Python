# "CLASS"

#QUESTIN NO 1 - Create a Student class, Attributes: name, roll_no, marks
            #    Method: is_passed() → returns True if marks >= 40, else False.

class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def is_passed(self):
        if self.marks >= 40 :
            return True
        else:
            return False
        
ob = Student("Saloni",48,95)
print(ob.is_passed())

#QUESTION NO 2 - Create a Rectangle class ,Attributes: length, width ,
                # Methods:
                # area() → returns area 
                # perimeter() → returns perimeter

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length*self.width)
    
    def perimeter(self):
        return (self.length+self.width)/2
    
r = Rectangle(5,9)
print(f"Area of rectangle : {r.area()}")
print(f"Perimeter of rectangle : {r.perimeter()}")

# QUESTION NO 3 -  Create a BankAccount class ,Attributes: account_number, balance
                # Methods:
                # deposit(amount) → increases balance
                # withdraw(amount) → decreases balance if enough money
                # display_balance() → prints current balance
                        
class BankAccount:
    def __init__(self,accNo,bal):
        self.accNo =accNo
        self.bal = bal
    
    def deposit(self,amo):
        self.amo = amo
        self.bal = self.bal+amo
        return self.bal
    
    def withdraw(self,amo):
        self.amo = amo
        if self.bal >=amo:
            self.bal = self.bal - amo
            return self.bal
        else:
            return "You have not enough balance to withdraw"
        
    def display_balance(self):
        return self.bal
    
b = BankAccount(100,5000)
print(f"Your total balance after deposite : {b.deposit(1500)}")
print(f"Your balance after withdraw : {b.withdraw(700)}")
print(f"Your total balance : {b.display_balance()}")
        

#QUESTION NO 4 - Create a Laptop class with private attribute ,Attributes: __price, brand, model
                # Methods:
                # set_price(price) → sets price
                # get_price() → returns price

class Laptop:
    def __init__(self,brand,model): #Private attributes
        self.__price = 0
        self.__model = model
        self.__brand = brand

    def set_price(self,price):
        if 10000<= price <= 500000:
            self.__price = price 
            return price
        else:
            print("Invalid input.Price must be between 10000 to 500000")

    def get_price(self):
        return self.__price

lap = Laptop("HP","hp255")
print(f"Price of the laptop : {lap.set_price(40000)}")   
print(f"Display the price : {lap.get_price()}")     

#QUESTION NO 5 - Create a ShoppingCart class ,Attributes: list of items
                # Methods:
                # add_item(item) → adds item to cart
                # remove_item(item) → removes item from cart
                # view_cart() → displays current items

class ShoppingCart:
    def __init__(self,my_list):
        self.my_list = my_list

    def add_item(self,item):  #adds item to cart
       return self.my_list.append(item)
    
    def remove_item(self,item):  #removes item from cart
        if item in self.my_list:
           return self.my_list.remove(item)
        else:
            print(f"{item} not exist in the list.Please enter valid item!!!")
    
    def view_cart(self): #displays current items
        print(self.my_list)

s = ShoppingCart(["apple","Banana","Bread","Milk"])
s.add_item("jam")
s.view_cart()
s.remove_item("apple")
s.view_cart()
             


        