# MODULE

import math #Importing the MATH MODULE(Use formathematical calculations)
import random as rd #Importing random module(USe for generating random values)
from datetime import datetime as dt #Importing datetime module(Use for manipulating date and time)
from datetime import timedelta as tdt 

#QUESTION NO 1 - Use math module to calculate square root, factorial, sin
x = int(input("Enter a number : "))
sqr_root = math.sqrt(x)
fact = math.factorial(x)
s = math.sin(x)
c = math.cos(x)
p = math.pow(x,2)
print(f"Square root of {x} is : {sqr_root}")
print(f"Factorial of {x} is : {fact}")
print(f"Sin of {x} is : {s}")
print(f"cos of {x} is : {c}")
print(f"Power of {x} is : {p}")

#QUESTION NO 2 - Generate a random number between 1 to 100
print(rd.randint(1,100)) #it generate only integer
print(rd.random()*100) #it generates both integer and float

#QUESTION NO 3 - Pick a random element from a list of colors
list = ["Yellow","Pink","Red","Blue","Black","White"]
print(rd.choice(list))

#QUESTON NO 4 - Print current date and time
now = dt.now()
print(dt.now())
print(f"Year : {now.year}") #2025
print(f"Month : {now.month}") #6
print(f"Day : {now.day}")  #1
print(f"Minute : {now.minute}") #49
print(now.strftime("%d-%m-%Y"))  # 01-06-2025
print(now.strftime("%A, %B %d, %Y"))  #Sunday, June 01, 2025

#QUESTION NO 5 - Find the date 10 days from today.
ten_days_after = now + tdt(days=10)
print(ten_days_after)

#QUESTION NO 6 - Write a program that adds 3 weeks to the current date and prints the result.
three_weeks_after = now + tdt(days=21) #1 week = 7 , 3 weeks = 7*3 = 21
print(three_weeks_after)

#QUESTION NO 7 - Display the time 5 hours and 30 minutes from now


