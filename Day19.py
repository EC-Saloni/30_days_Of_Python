from datetime import datetime as dt
# 'CLASS AND STATIC METHOD'

#QUESTION NO 1 - Create a Student class that stores the name and marks of a student.
                    # Use a class method to create a student from a string like "Bob-89".
                    # Use a static method to check if the given marks are valid (between 0 and 100).

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls,data_str):
        name,marks = data_str.split('-')
        marks = int(marks)
        if cls.check_valid(marks):
            return cls(name,int(marks))
        else:
            raise ValueError("Marks sould be between o and 100")

    @staticmethod
    def check_valid(marks):
        return 0<= marks <=100
    
    def display(self):
        print(f"Name : {self.name} , Marks : {self.marks}")
           

s = Student.from_string("Saloni-91")
s.display()
print(Student.check_valid(101))


#QUESTION NO 2 - Create a Temperature class that stores temperature in Celsius.
            # Add a class method to create an object using Fahrenheit.
            # Add a static method to check if water will boil at that temperature (Celsius ≥ 100).

class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls,fahrenheit):
        celsius = 5/9 * (fahrenheit -32)
        return cls(celsius)
    

    @staticmethod
    def will_boil(celsius_temp):
        return celsius_temp >=100
    
    def display(self):
        print(f"Temparature in celsius : {self.celsius:.2f}°C")
        if self.will_boil(self.celsius):
            print("Water will boil at this temparature.")
        else:
            print("Temparature is not enought to boli water.")

t = Temperature.from_fahrenheit(250)
t.display()

print(Temperature.will_boil(99))
print(Temperature.will_boil(105))
        
#QUESTION NO 3 - Make a Date class to store a day, month, and year.
                # Create a class method that returns the current date (use datetime module).
                # Write a static method that checks whether a year is a leap year.

class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def current_date(cls):
        now =  dt.now()
        return cls(now.day , now.month , now.year)
    

    @staticmethod
    def check_leap_year(l_year):
        if (l_year % 4 == 0 and l_year % 100 != 0) or (l_year % 400 == 0):
            return True
        else:
            return False
    

    def display(self):
        print(f"Date: {self.day}/{self.month}/{self.year}")
        if self.check_leap_year(self.year):
            print("The given year is a leap year.")
        else:
            print("The given year is not a leap year.")

d = Date.current_date()
d.display()

print(Date.check_leap_year(2024))





